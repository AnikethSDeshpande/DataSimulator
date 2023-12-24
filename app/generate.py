from template import Template
import generator


GENERATORS = {
    'int': generator.IntegerGenerator,
    'float': generator.FloatGenerator,
    'str': generator.StringGenerator,
    'datetime': generator.DateTimeGenerator
}

class Generate:
    def __init__(self, template: Template, number_of_records=None):
        self.template = template
        self.number_of_records = number_of_records
    
    def generate(self, number_of_records=None):
        if not (self.number_of_records or number_of_records):
            raise Exception('number_of_records is not specified.')
        
        self.number_of_records = number_of_records
        
        generators = []
        for record in self.template.template:
            generators.append(
                GENERATORS[record.record_type](record.record, self.number_of_records).generate()
            )
        records = zip(*generators)

        return records


if __name__ == '__main__':
    template = '''
        invoice_id, int, 1000, 1005
        billing_date, datetime, 2023-10-01, 2023-10-30
        customer_name, str, true 
        item_id, str, false, itm-, 001, 999
        price, float, 1000, 9999
    '''

    template = Template(template)
    generator = Generate(template).generate(10)
    
    for i in generator:
        print(i)
