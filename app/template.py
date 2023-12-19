from typing import List

from record import Record


class Template:
    def __init__(self, template: str) -> None:
        self.template = self.preprocess(template)
    
    def preprocess(self, template: str) -> List:
        records = template.strip().split('\n')
        return [Record(record) for record in records]
    
    def __str__(self) -> str:
        string = ''
        for record in self.template:
            string += '<' + str(record) + '>\n'

        return '<' + string + '>'


if __name__ == '__main__':

    template = '''
        invoice_id, int, 1000, 9999
        customer_name, str, true 
        item_id, str, false, itm-, 001, 999
        price, float, 1000, 9999
    '''

    template = Template(template)
    print(type(template))

    for t in template.template:
        print(t.record.__dict__)


