from output_handler import OutputHandler


class Console(OutputHandler):
    def __init__(self, metadata, data):
        self.sink(metadata, data)
    
    def sink(self, metadata, data):
        if metadata:
            print(metadata, '\n', '='*100,'\n')
        
        for d in data:
            print(d)
