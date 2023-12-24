import uuid
import random
from datetime import timedelta
from abc import ABC, abstractmethod


from record import Record


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


class  DateTimeGenerator(Generator):
    def __init__(self, record_info: Record, number_of_records: int) -> None:
        self.record_info = record_info
        self.number_of_records = number_of_records
        
    def generate(self):
        time_delta = self.record_info.end_date - self.record_info.start_date

        for iteration in range(self.number_of_records):
            random_days = random.randint(0, time_delta.days)
            yield self.record_info.start_date + timedelta(days=random_days)
