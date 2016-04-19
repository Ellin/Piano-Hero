import os
import csv_reader
import summarizer
import intermediate

input_filename = 'Piano-Hero-1_Overall.csv'
input_filepath = os.path.join(os.getcwd(), input_filename)
output_filename = 'piano-hero-1-data-summary.csv'
output_filepath = os.path.join(os.getcwd(), output_filename)
intermediate_output_filename = 'piano-hero-1-intermediate-output.csv'
intermediate_output_filepath = os.path.join(os.getcwd(), intermediate_output_filename)

intermediate_data_dict = csv_reader.read_csv(input_filepath)

summarizer.data_summary(intermediate_data_dict, output_filepath)
intermediate.intermediate_data(intermediate_data_dict, intermediate_output_filepath)