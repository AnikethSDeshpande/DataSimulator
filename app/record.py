from typing import List


class Record:
    def __init__(self, record: str) -> None:
        self.record = self.preprocess(record)

    def preprocess(self, record: str) -> List:
        record = [r.strip() for r in record.split(',')]

        self.record_type = record[1]

        if self.record_type == 'int':
            return IntegerRecord(record)

        if self.record_type == 'float':
            return FloatRecord(record)
        
        if self.record_type == 'str':
            return StringRecord(record)
        
        raise Exception('UNSUPPORTED_DATA_TYPE')
    
    def __str__(self) -> str:
        return str(self.record)
    

class IntegerRecord:
    def __init__(self, record: list) -> None:
        self.record = self.preprocess(record)

    def preprocess(self, record):
        self.name = record[0]
        self.type = record[1]
        self.min = int(record[2])
        self.max = int(record[3])

        return [self.name, self.type, self.min, self.max]

    def __str__(self) -> str:
        return ', '.join([str(r) for r in self.record])


class FloatRecord:
    def __init__(self, record: list) -> None:
        self.record = self.preprocess(record)

    def preprocess(self, record):
        self.name = record[0]
        self.type = record[1]
        self.min = int(record[2])
        self.max = int(record[3])
        self.decimal_pts = int(record[4]) if (len(record)>4 ) else 2

        return [self.name, self.type, self.min, self.max, self.decimal_pts]

    def __str__(self) -> str:
        return ', '.join([str(r) for r in self.record])


class StringRecord:
    def __init__(self, record: list) -> None:
        self.record = self.preprocess(record)

    def preprocess(self, record):
        self.name = record[0]
        self.type = record[1]

        self.uuid = True if (record[2]).lower()=='true' else False

        string_record = [self.name, self.type, self.uuid]

        if not self.uuid:
            self.string_prefix = record[3]
            self.suffix_min = int(record[4])
            self.suffix_max = int(record[5])
            string_meta_info = [self.string_prefix, self.suffix_min, self.suffix_max]
            
            string_record += string_meta_info

        return string_record
    
    def __str__(self) -> str:
        return ', '.join([str(r) for r in self.record])


if __name__ == '__main__':
    rec = 'invoice_id, int, 1000, 9999'
    # record = 'customer_name, str, true'
    # record = 'customer_name, str, false, cust-, 001, 999'
    
    r = Record(rec)
    print(r.record.__dict__)