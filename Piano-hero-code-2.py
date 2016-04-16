import os
import csv

filename = 'test.csv'
filepath = os.path.join(os.getcwd(), filename)

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
		my_dict = ({})
		session_dict = ({})
		trial_dict = ({})

		for row in reader:
			patient = 'patient ' + row[0]
			session = 'session ' + row[1]
			trial = 'trial ' + row[3]
			given_list = get_given_balls (row[4], row[5], row[6], row[7])
			press_list = get_patient_presses (row[8], row[9], row[10], row[11])

			if patient in my_dict:
				session_dict = my_dict[patient]
			else:
				session_dict = ({})

			if session in session_dict:
				trial_dict = session_dict[trial]
			else:
				trial_dict = ({})

			trial_dict[trial] = analyze_trial (given_list, press_list)
			#within trial:  correct (0,1), # hit, # substitions, # additions, order error (1,0), # balls given (1,2,3,4)
			#analysis function returns trial dict of... {correct: x, num_hit: x, num_substitutions: x, num_additions: x, order_error: x}


				somedict = ({key1: value1, key2: value2, key3: value3})
				#somedict[key1] -> value1
				#session_dict["trial 1"]['correct']
				if session in my_dict[patient]:

			trial_dict[trial] = row[3]
			session_dict[session] = trial_dict
			my_dict[patient] = session_dict

		
		print (my_dict)
		print (my_dict.keys())
		print (my_dict['patient 27'].keys())
		print (my_dict['patient 27']['session 1'].keys())


correct = False				# 1 = user_list is correct; 0 = incorrect
order_error = False		# 1 = atleast one element in user_list is in the wrong order
hits = 0				# element in user_list is in given_list and is not excessive
substitution = 0	# element in user_list is not in given_list or is excessive
additions = 0		# excessive elements in user_list; user_list > given_list

def check_correct():
	if input_list == given_list:
		correct = True
def check_additions():
	if input_list.length > given_list.length:
		additions = input_list.length - given_list.length

def check_order_errors(intersection_list):
	# intersections of input_list & given_list, but unlike set(), keeps duplicate elements & also preserves order
	given_list_mod = [x for x in given_list if x in input_list]
	input_list_mod = [x for x in input_list if x in given_list_mod]		
	
	#input_list_mod = []
	# the following forloop removes all *adjacent* duplicates in inter_input_list
	# might be unnecessary
#	for i in range (inter_input_list.length):
#		if i >= inter_input_list.length - 1 or inter_input_list[i] != inter_input_list[i+1]:
#			input_list_mod.append(inter_input_list[i])
	order_hits = 0
	j = 0
	for i in range(input_list_mod.length):
		if input_list_mod[i] == given_list_mod[j]:
			order_hits = order_hits + 1
			if given_list_mod.length - 1 > j:
				j = j + 1

	if order_hits < given_list_mod.length:
		order_error = True

def analyze_trial(t):
	input_list = all_input[t] # the list of patient inputs for a single trial
	given_list = all_given[t] # the list of givens for a single trial
	intersection_list = list(set(input_list) & set(given_list))
	# t = trial # for a patient (1 to 40)
	if input_list != []: 
		check_correct()
		if correct:
			hits = given_list.length
		else:
			hits = intersection_list.length	# hits = length of list of intersection of input_list & given_list
			check_additions()
			substitutions = input_list.length - hits - additions
			check_order_error()

def write_output_data():
	#... make new file

for patient in patient_list:
	for t in trials:
		analyze_trial(t)
		write_output_data(patient, t, correct, hits, addition, substitutions, order_error)



read_csv(filepath)