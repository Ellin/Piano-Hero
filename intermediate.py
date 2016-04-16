import csv

def intermediate_data(data_dict, output_filepath): # output individual trial analyses to new csv file
	intermediate_dict = ({})
	column_labels = ["Patient", "Session", "Trial", "Given Balls", "Presses", "Correct", "Hits", "Substitutions", "Additions", "Order error", "Condition"]
	with open(output_filepath, 'w', newline = '') as new_csvfile:
		writer = csv.DictWriter(new_csvfile, fieldnames = column_labels)
		writer.writeheader()

		for patient_key, patient in sorted(data_dict.items()):
			for session_key, session in patient.items():
				for trial_key, trial in session.items():
					given_list = trial['given balls']
					press_list = trial['presses']
					correct = trial['correct']
					hits = trial['hits']
					substitutions = trial['substitutions']
					additions = trial['additions']
					order_error = trial['order error']
					condition = trial['condition']

					intermediate_dict = {"Patient": patient_key, "Session": session_key, "Given Balls": given_list, "Presses": press_list, "Trial": trial_key, "Correct": correct, "Hits": hits, "Substitutions": substitutions, "Additions": additions, "Order error": order_error, "Condition": condition}
					writer.writerow(intermediate_dict)