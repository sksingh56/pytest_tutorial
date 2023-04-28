import csv
import os
import pandas as pd


def csv_file_reader_text(file_path):
    #breakpoint()
    with open(file_path) as fp:
        content = csv.DictReader(fp)
        data = [line for line in content]
        for row in data:         
                row['Lat'] = float(row['Lat'])
                row['Long'] = float(row['Long'])
                row['Altitude'] = float(row['Altitude'])
    return data


def read_csv_using_pandas(file_path):
    df = pd.read_csv(file_path)
    return df
