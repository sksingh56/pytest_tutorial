import pytest
from scripts import file_reader
from conftest import file_location,process_data_csv

def test_csv_row_count(process_data_csv):
    data = process_data_csv(file_name='clean_map.csv')
    assert len(data) == 180

def test_csv_check_header(process_data_csv):
    data = process_data_csv(file_name='clean_map.csv')
    header_actual = list(data[0].keys())
    header_expected = ['Country', 'City', 'State_Or_Province', 'Lat', 'Long', 'Altitude']
    assert header_actual == header_expected

def test_data_type_for_data(process_data_csv):
    data = process_data_csv(file_name='clean_map.csv')
    for row in data: 
        assert isinstance(row['Lat'],float) == True 
        assert isinstance(row['Long'],float)== True
        assert isinstance(row['Altitude'],float) == True
