import csv

def csv_to_list_of_dicts(file_path):
    result_list = []

    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            for row in csv_reader:
                result_list.append(row)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error: {e}")

    return result_list