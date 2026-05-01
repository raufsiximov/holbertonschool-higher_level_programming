#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    CSV faylını oxuyur və məlumatları data.json faylına yazır.
    """
    try:
        data = []
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            # CSV faylını lüğət formatında oxuyur
            reader = csv.DictReader(csv_f)
            for row in reader:
                data.append(row)

        # Məlumatları JSON faylına yazır
        with open('data.json', mode='w', encoding='utf-8') as json_f:
            json.dump(data, json_f, indent=4)
        
        return True
    except FileNotFoundError:
        return False
