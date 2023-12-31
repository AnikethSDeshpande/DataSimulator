from output_handler.console import Console
from output_handler.csv import CSV
from output_handler.kafka import Kafka

from template import Template
from generate import Generate
from stream import Stream


default_settings = {
    'author': 'simulator-001',
    'project': 'simulation-001',
    'output': Console
}

class Simulator:
    def __init__(self, **settings):
        self.author = settings.get('author', default_settings['author'])
        self.project = settings.get('project', default_settings['project'])
        self.output = settings.get('output', default_settings['output'])

        self.metadata = {'author': self.author, 'project': self.project}
        self.stream_params = {'duration': 5, 'frequency': 1}

    def template(self, template):
        self.template = Template(template)

    def simulate(self, number_of_records=None, output=None, stream_params=None, **kwargs):
        if not number_of_records:
            raise Exception('number_of_records not specified.')
        
        if not self.template:
            raise Exception('Template not specified.')
        
        self.number_of_records = number_of_records

        if output:
            self.output = output
        
        metadata = self.metadata
        data = Generate(self.template).generate(self.number_of_records)

        if not stream_params:
            self.output(metadata, data, **kwargs)
            return

        Stream(self.output, 
               metadata=metadata, 
               _generate=Generate(self.template),
               number_of_records=self.number_of_records,
               stream_params=stream_params, 
               **kwargs
            )

    def __str__(self) -> str:
        s = f'''author: {self.author}, project: {self.project}'''
        return s


if __name__ == '__main__':

    template = '''
        invoice_id, int, 1000, 9999
        billing_date, datetime, 2023-10-01, 2023-10-30
        customer_name, str, true 
        item_id, str, false, itm-, 001, 100
        price, float, 1000, 9999
    '''

    sim = Simulator(author='Aniket', project='sample-simulation')
    sim.template(template)
    
    # sink to csv
    sim.simulate(50, output=CSV, file_path='/Users/ani/tempmetadata/test_data.csv')
    
    # sink to console
    sim.simulate(50, output=Console)
    
    # stream to kafka
    sim.simulate(
        number_of_records=5, 
        output=Kafka, 
        bootstrap_servers='localhost:9092', 
        topic='sample',
        stream_params={'duration': 10, 'frequency': 5},
        users=4
    )
