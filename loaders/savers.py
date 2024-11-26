import json
import csv

class UnitOfWork:
   
    @staticmethod
    def save_to_json(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    
    @staticmethod
    def save_to_csv(data, filename, fieldnames):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def save_to_txt(data, filename):
        with open(filename, 'w') as file:
            for line in data:
                file.write(f"{line}\n")