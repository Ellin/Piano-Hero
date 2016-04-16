import csv

def data_summary(data_dict, output_filepath): # calculate summary analyses and output to a new csv file
	summary_dict = ({})

	column_labels = ["Patient", "Session", "Percent Correct", "Percent Hits", "Substitutions", "Additions", "Order Errors", "OE 2 balls", "OE 3 balls", "OE 4 balls"]
	with open(output_filepath, 'w', newline = '') as new_csvfile:
		writer = csv.DictWriter(new_csvfile, fieldnames = column_labels)
		writer.writeheader()

		for patient_key, patient in sorted(data_dict.items()):
			for session_key, session in patient.items():
				total_correct = 0
				total_hits = 0
				total_substitutions = 0
				total_additions = 0
				total_order_errors = 0
				oe_2balls = 0
				oe_3balls = 0
				oe_4balls = 0
				total_ball_drops = 0

				for trial_key, trial in session.items():
					correct = trial['correct']
					hits = trial['hits']
					substitutions = trial['substitutions']
					additions = trial['additions']
					order_error = trial['order error']
					condition = trial['condition']

					total_correct = total_correct + correct
					total_hits = total_hits + hits
					total_ball_drops = total_ball_drops + condition

					if order_error == True:
						total_order_errors = total_order_errors + 1
						if condition == 2:
							oe_2balls = oe_2balls + 1
						elif condition == 3:
							oe_3balls = oe_3balls + 1
						elif condition == 4:
							oe_4balls = oe_4balls + 1

				percent_correct = (total_correct/40)*100
				percent_hits = (total_hits/total_ball_drops)*100
				summary_dict = {"Patient": patient_key, "Session": session_key, "Percent Correct": percent_correct, "Percent Hits": percent_hits, "Substitutions": total_substitutions, "Additions": total_additions, "Order Errors": total_order_errors, "OE 2 balls": oe_2balls, "OE 3 balls": oe_3balls, "OE 4 balls": oe_4balls}
				writer.writerow(summary_dict)