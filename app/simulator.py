from output_handler.console import Console
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

        self.metadata = {'author': self.author,'project': self.project}

    def template(self, template):
        self.template = Template(template)

    def _generate(self):
        if not self.template:
            raise Exception('Template not specified.')
        
        return Generate(self.template, self.number_of_records)

    def simulate(self, number_of_records=None, output=Console):
        if not number_of_records:
            raise Exception('number_of_records not specified.')
        
        self.number_of_records = number_of_records

        if output:
            self.output = output
        
        metadata = self.metadata

        self.output(metadata, [{'a': 1}, {'b':2}])
    

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
    sim.simulate(5)