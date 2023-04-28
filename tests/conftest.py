import pytest
from scripts import file_reader
import os

@pytest.fixture(scope='session')
def file_location():
    return 'tests/resources/cities/'

@pytest.fixture(scope='session')
def process_pandas(file_location):
   files = os.listdir(file_location)

   def _specify_file(file_name):
      for file in files:
        if file_name==file:
            df =  file_reader.read_csv_using_pandas(file_location+file)
            return df  
   yield _specify_file


@pytest.fixture(scope='module')
def process_data_csv(file_location):
    files = os.listdir(file_location)

    def _specify_file(file_name):
        for file in files:
            if file == file_name:
                data = file_reader.csv_file_reader_text(file_location+file)
        return data 
    yield _specify_file
