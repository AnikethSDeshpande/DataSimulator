import csv

from output_handler import OutputHandler


class CSV(OutputHandler):
    def __init__(self, metadata, data, file_path=None) -> None:
        metadata['file_path'] = file_path
        self.sink(metadata, data)

    def sink(self, metadata, data):
        file_path = metadata.get('file_path')

        if not file_path:
            raise Exception(f'Expected file path to sink to csv file')
        
        with open(file_path, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            csv_writer.writerows(data)