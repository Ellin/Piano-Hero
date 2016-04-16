import csv
import trial_analyzer

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

def read_csv(filepath):	# gets data from input csv file and analyzes each trial, and outputs a dictionary containing analyzed trial data for each patient; trial data still needs to be summarized
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

			trial_dict[trial] = trial_analyzer.analyze_trial(given_list, press_list)
			trial_dict[trial]['condition'] = condition	# add # of balls given (1,2,3,4) in each trial
			session_dict[session] = trial_dict
			data_dict[patient] = session_dict

	return data_dict

