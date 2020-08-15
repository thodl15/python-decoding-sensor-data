# STL Imports
import csv
import os

# 3rd Party Imports
import glob

def load_sensor_data():
    sensor_data = []
    sensor_files = glob.glob(os.path.join(os.getcwd(), "datasets", "*.csv"))

    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            data_reader = csv.DictReader(data_file, delimiter=',')
            # Typo in step 5:
            # Should be `data_readeer`, not `data_file`
            for row in data_reader:
                sensor_data.append(row)
    
    return sensor_data
