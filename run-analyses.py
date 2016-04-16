import os
import csv_reader
import summarizer

input_filename = 'Piano-Hero-2_Overall.csv'
input_filepath = os.path.join(os.getcwd(), input_filename)
output_filename = 'real-write-test.csv'
output_filepath = os.path.join(os.getcwd(), output_filename)

summarizer.data_summary(csv_reader.read_csv(input_filepath), output_filepath)