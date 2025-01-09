import csv

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
            return len(self.data)
        except FileNotFoundError:
            print("Error: File not found.")
            return 0