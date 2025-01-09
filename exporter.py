import csv
import json
class DataExporter:
    def __init__(self, data):
        self.data = data

    def aggregate_data(self):
        park_data = {}
        for row in self.data:
            park = row['Branch']
            if park not in park_data:
                park_data[park] = {
                    'total_reviews': 0,
                    'positive_reviews': 0,
                    'total_rating': 0,
                    'countries': set()
                }
            park_data[park]['total_reviews'] += 1
            park_data[park]['total_rating'] += int(row['Rating'])
            if int(row['Rating']) > 3:
                park_data[park]['positive_reviews'] += 1
            park_data[park]['countries'].add(row['Reviewer_Location'])
        for park in park_data:
            park_data[park]['average_rating'] = park_data[park]['total_rating'] / park_data[park]['total_reviews']
            park_data[park]['countries'] = len(park_data[park]['countries'])
        return park_data

    def export_to_txt(self, file_path):
        data = self.aggregate_data()
        with open(file_path, 'w') as file:
            for park, details in data.items():
                file.write(f"{park}:\n")
                for key, value in details.items():
                    file.write(f"  {key}: {value}\n")
                file.write("\n")

    def export_to_csv(self, file_path):
        data = self.aggregate_data()
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Park", "Total Reviews", "Positive Reviews", "Average Rating", "Countries"])
            for park, details in data.items():
                writer.writerow([park, details['total_reviews'], details['positive_reviews'], details['average_rating'], details['countries']])

    def export_to_json(self, file_path):
        data = self.aggregate_data()
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)