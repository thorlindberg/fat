# Parse input arguments

import argparse

parser = argparse.ArgumentParser(description='Process tracking data')
parser.add_argument('--input', help='Input CSV file path', required=True)
parser.add_argument('--output', help='Output directory path', required=True)
args = parser.parse_args()

# Read input file

from csv_to_list_of_dicts import csv_to_list_of_dicts

csv_file_path = args.input
measurements = csv_to_list_of_dicts(csv_file_path)

# Add calorie expenditure

for day in range(len(measurements)):
    weight = float(measurements[day]['Weight'])
    height = float(measurements[day]['Height'])
    age = int(measurements[day]['Age'])

    basal_metabolic_rate = {
        'Male': 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age),
        'Female': 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    }

    minutes_in_a_day = 24 * 60
    intake_calories = int(measurements[day]['Intake calories'])
    active_calories = int(measurements[day]['Active calories'])
    active_minutes = int(measurements[day]['Active minutes'])
    passive_minutes = minutes_in_a_day - active_minutes
    passive_calories = basal_metabolic_rate[measurements[day]['Sex']] / minutes_in_a_day * passive_minutes
    measurements[day]['Calorie expenditure'] = (intake_calories - active_calories - passive_calories) * -1

# Create graphs

from plot_graph import plot_graph

output_folder_path = args.output

for current_day in range(len(measurements)):
    title = f'{current_day + 1}'
    labels = ['Weight in kilograms (kg)', 'Time in days']

    weights = []
    days = []
    predictions = []
    increases = []
    decreases = []
    for previous_day in range(current_day + 1):
        weight = float(measurements[previous_day]['Weight'])
        weights.append(weight)
        days.append(previous_day + 1)
        loss = 1 / 7700 * measurements[previous_day]['Calorie expenditure']
        predictions.append(weight - loss)
        increase = 1 / 7700 * (measurements[previous_day]['Calorie expenditure'] - 500)
        increases.append(weight - increase)
        decrease = 1 / 7700 * (measurements[previous_day]['Calorie expenditure'] + 500)
        decreases.append(weight - decrease)

    plot_graph(title, weights, predictions, increases, decreases, days, labels, output_folder_path)

    last_day = current_day == len(measurements) - 1
    if last_day:
        plot_graph('continuous', weights, predictions, increases, decreases, days, labels, output_folder_path)