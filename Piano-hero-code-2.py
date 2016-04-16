import os
import csv
import analysis

input_filename = 'Piano-Hero-2_Overall.csv'
input_filepath = os.path.join(os.getcwd(), input_filename)
output_filename = 'real-write-test.csv'
output_filepath = os.path.join(os.getcwd(), output_filename)

def get_given_balls (ball1, ball2, ball3, ball4):
	given_list = []
	if ball1 != "":
		given_list.append(int(ball1))
	if ball2 != "":
		given_list.append(int(ball2))
	if ball3 != "":
		given_list.append(int(ball3))
	if ball4 != "":
		given_list.append(int(ball4))
	return given_list

def get_patient_presses (press1, press2, press3, press4):
	press_list = []
	if press1 != "":
		press_list.append(int(press1))
	if press2 != "":
		press_list.append(int(press2))
	if press3 != "":
		press_list.append(int(press3))
	if press4 != "":
		press_list.append(int(press4))
	return press_list


def read_csv(filepath):
	with open(filepath, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)	#skips header row
		data_dict = ({})

		for row in reader:
			patient = int(row[0])
			session = int(row[1])
			trial = int(row[3])
			given_list = get_given_balls (row[4], row[5], row[6], row[7])
			press_list = get_patient_presses (row[8], row[9], row[10], row[11])
			condition = int(row[18])

			if patient in data_dict:
				session_dict = data_dict[patient]
			else:
				session_dict = ({})

			if session in session_dict:
				trial_dict = session_dict[session]
			else:
				trial_dict = ({})

			trial_dict[trial] = analysis.analyze_trial(given_list, press_list)
			trial_dict[trial]['condition'] = condition

			session_dict[session] = trial_dict
			data_dict[patient] = session_dict
			#within trial:  correct (0,1), # hit, # substitions, # additions, order error (1,0), # balls given (1,2,3,4)
			#analysis function returns trial dict of... {correct: x, num_hit: x, num_substitutions: x, num_additions: x, order_error: x}

			#print (trial_dict[trial])
	#print (data_dict)
	return data_dict


def data_summary(data_dict): #calculate summary analyses and output to a new csv file
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

data_summary(read_csv(input_filepath))
