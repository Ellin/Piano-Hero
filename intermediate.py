import csv

def intermediate_data(data_dict, output_filepath): # calculate summary analyses and output to a new csv file
	intermediate_dict = ({})
	column_labels = ["Patient", "Session", "Trial", "Correct", "Hits", "Substitutions", "Additions", "Order error"]
	with open(output_filepath, 'w', newline = '') as new_csvfile:
		writer = csv.DictWriter(new_csvfile, fieldnames = column_labels)
		writer.writeheader()

		for patient_key, patient in sorted(data_dict.items()):
			for session_key, session in patient.items():
				for trial_key, trial in session.items():
					correct = trial['correct']
					hits = trial['hits']
					substitutions = trial['substitutions']
					additions = trial['additions']
					order_error = trial['order error']
					condition = trial['condition']

					intermediate_dict = {"Patient": patient_key, "Session": session_key, "Trial": trial_key, "Correct": correct, "Hits": hits, "Substitutions": substitutions, "Additions": additions, "Order error": order_error}
					writer.writerow(intermediate_dict)