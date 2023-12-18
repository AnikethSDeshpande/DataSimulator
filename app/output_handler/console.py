class Console:
    def __init__(self, metadata, data):
        if metadata:
            print(metadata, '\n', '='*100,'\n')
        
        for d in data:
            print(d)
    
