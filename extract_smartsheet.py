import json
import csv
import requests
import os

def get_smartsheet_data():
    """Fetch data from a SmartSheet using API token and Sheet ID from environment variables."""
    bearer_token = os.environ.get('BEARER')
    sheet_id = os.environ.get('SHEET_ID')

    if not bearer_token or not sheet_id:
        raise ValueError("Environment variables 'BEARER' and 'SHEET_ID' are required.")

    headers = {
        'Authorization': bearer_token,
        'Accept': 'text/csv',
    }

    response = requests.get(f'https://api.smartsheet.com/2.0/sheets/{sheet_id}', headers=headers)
    response.raise_for_status()
    return response.text

def process_csv_to_json(csv_text):
    """Convert CSV text to formatted JSON string."""
    data = []
    reader = csv.DictReader(csv_text.splitlines(), delimiter=',')
    for row in reader:
        data.append(row)
    return json.dumps(data, indent=4)

if __name__ == "__main__":
    csv_data = get_smartsheet_data()
    json_output = process_csv_to_json(csv_data)
    print(json_output)
