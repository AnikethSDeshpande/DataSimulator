import time
import concurrent.futures


def stream_worker(func=None, **kwargs):
    duration = kwargs['stream_params'].get('duration')
    frequency = kwargs['stream_params'].get('frequency')
    number_of_records = kwargs['number_of_records']
    generator = kwargs['_generate']
    
    kwargs.pop('stream_params')
    kwargs.pop('_generate')
    kwargs.pop('number_of_records')

    start_time = time.time()

    current_time = time.time()
    
    while (duration == 0) or (current_time - start_time < duration):
        current_time = time.time()
        print(f'current_time - start_time_holder[0]: {current_time - start_time}')
        print(f'duration: {duration}')

        exec_start = time.time()
        kwargs['data'] = generator.generate(number_of_records)
        func(**kwargs)
        exec_end = time.time()
        
        if duration == 0:
            break
        
        exec_time = exec_end - exec_start

        if exec_time < frequency:
            time.sleep(frequency - exec_time)
    
    print('streaming completed...')


def Stream(func=None, **kwargs):
    workload = 1
    if 'users' in kwargs:
        workload = kwargs.get('users')
        kwargs.pop('users')
    
    max_workers = min(8, workload)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(stream_worker, func, **kwargs) for i in range(workload)]
        concurrent.futures.wait(futures)
    