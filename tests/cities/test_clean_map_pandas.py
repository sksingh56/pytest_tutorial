import pytest
import pandas as pd 
from conftest import file_location,process_pandas
from scripts import file_reader


def test_file_row_col(process_pandas):
    df = process_pandas(file_name='clean_map.csv')
    assert df.shape == (180,6)



@pytest.mark.parametrize("file_name_to_be_used",[('clean_map.csv'),],indirect=False)
def test_filter_condition(process_pandas, file_name_to_be_used):
    df = process_pandas(file_name=file_name_to_be_used)
    assert len(df[df['Country'] == 'Andorra']) == 7


@pytest.mark.parametrize("file_name_to_be_used",[('clean_map.csv'),])
def test_filter_city_at_altitude_for_country(process_pandas, file_name_to_be_used):
   df = process_pandas(file_name=file_name_to_be_used)
   assert len([df['City'] == 'Córdoba']) ==1


