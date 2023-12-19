from output_handler.console import Console
from output_handler.csv import CSV
from output_handler.kafka import Kafka

from template import Template
from generator import Generate


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

    def template(self, template):
        self.template = Template(template)

    def _generate(self):
        if not self.template:
            raise Exception('Template not specified.')
        
        return Generate(self.template).generate(self.number_of_records)

    def simulate(self, number_of_records=None, output=None, **kwargs):
        if not number_of_records:
            raise Exception('number_of_records not specified.')
        
        self.number_of_records = number_of_records

        if output:
            self.output = output
        
        metadata = self.metadata
        data = self._generate()

        self.output(metadata, data, **kwargs)
    

    def __str__(self) -> str:
        s = f'''author: {self.author}, project: {self.project}'''
        return s


if __name__ == '__main__':

    template = '''
        invoice_id, int, 1000, 9999
        customer_name, str, true 
        item_id, str, false, itm-, 001, 999
        price, float, 1000, 9999
    '''

    sim = Simulator(author='Aniket', project='ample-simulation')
    sim.template(template)
    
    # sink to csv
    sim.simulate(50, output=CSV, file_path='/Users/ani/tempmetadata/test_data.csv')
    
    # sink to console
    sim.simulate(50, output=Console)
    
    # sink to kafka
    sim.simulate(50, output=Kafka, bootstrap_servers='localhost:9092', topic='ample')
