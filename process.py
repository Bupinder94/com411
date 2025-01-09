import csv
import json

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

    def filter_reviews_by_park(self, park_name):
        return [row for row in self.data if row['Branch'] == park_name]

    def count_reviews_by_location(self, park_name, location):
        return sum(1 for row in self.data if row['Branch'] == park_name and row['Reviewer_Location'] == location)

    def average_rating_by_year(self, park_name, year):
        ratings = [int(row['Rating']) for row in self.data if row['Branch'] == park_name and row['Year_Month'].startswith(str(year))]
        return sum(ratings) / len(ratings) if ratings else 0

    def average_score_per_location(self):
        park_location_scores = {}
        for row in self.data:
            key = (row['Branch'], row['Reviewer_Location'])
            if key not in park_location_scores:
                park_location_scores[key] = []
            park_location_scores[key].append(int(row['Rating']))
        return {key: sum(scores)/len(scores) for key, scores in park_location_scores.items()}
