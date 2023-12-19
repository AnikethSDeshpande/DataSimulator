import uuid
import random
from abc import ABC, abstractmethod

from template import Template
from record import Record


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
            if record.record_type == 'int':
                generators.append(IntegerGenerator(record.record, self.number_of_records).generate())
            if record.record_type == 'float':
                generators.append(FloatGenerator(record.record, self.number_of_records).generate())
            if record.record_type == 'str':
                generators.append(StringGenerator(record.record, self.number_of_records).generate())
        
        records = zip(*generators)

        return records


class Generator(ABC):

    @abstractmethod
    def generate(self):
        pass


class IntegerGenerator(Generator):
    def __init__(self, record_info: Record, number_of_records: int) -> None:
        self.record_info = record_info
        self.number_of_records = number_of_records
    
    def generate(self):
        for iteration in range(self.number_of_records):
            yield random.randint(self.record_info.min, self.record_info.max)        


class FloatGenerator(Generator):
    def __init__(self, record_info: Record, number_of_records: int) -> None:
        self.record_info = record_info
        self.number_of_records = number_of_records
    
    def generate(self):
        for iteration in range(self.number_of_records):
            record = round( 
                random.uniform(
                        self.record_info.min, 
                        self.record_info.max
                    ),  self.record_info.decimal_pts
            )

            yield record


class StringGenerator(Generator):
    def __init__(self, record_info: Record, number_of_records: int) -> None:
        self.record_info = record_info
        self.number_of_records = number_of_records
    
    def generate(self):
        for iteration in range(self.number_of_records):
            if self.record_info.uuid:
                yield str(uuid.uuid4())
            
            else:
                suffix_number = random.randint(self.record_info.suffix_min, 
                                               self.record_info.suffix_max)
                yield self.record_info.string_prefix + str(suffix_number)


if __name__ == '__main__':
    template = '''
        invoice_id, int, 1000, 1005
        customer_name, str, true 
        item_id, str, false, itm-, 001, 999
        price, float, 1000, 9999
    '''

    template = Template(template)
    generator = Generate(template).generate(10)
    
    for i in generator:
        print(i)
