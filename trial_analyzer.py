
def check_correct(given_list, press_list):
	if press_list == given_list:
		correct = True
	else:
		correct = False	
	return correct

def check_additions(given_list, press_list):
	if len(press_list) > len(given_list):
		additions = len(press_list) - len(given_list)
	else:
		additions = 0
	return additions

def check_order_error(given_list, press_list):
	# intersections of press_list & given_list, but unlike set(), keeps duplicate elements & also preserves order
	given_list_mod = [x for x in given_list if x in press_list]
	press_list_mod = [x for x in press_list if x in given_list_mod]
	order_error = False		
	order_hits = 0
	j = 0
	for i in range(len(press_list_mod)):
		if press_list_mod[i] == given_list_mod[j]:
			order_hits = order_hits + 1
			if len(given_list_mod) - 1 > j:
				j = j + 1

	if order_hits < len(given_list_mod):
		order_error = True

	return order_error

def analyze_trial(given_list, press_list):
	correct = False				
	order_error = False		
	hits = 0				
	substitutions = 0	
	additions = 0		
	trial_data = ({})
	intersection_list = list(set(press_list) & set(given_list))

	if press_list != []: 
		correct = check_correct(given_list, press_list)
		if correct:
			hits = len(given_list)
		else:
			hits = len(intersection_list)	# hits = length of list of intersection of press_list & given_list
			additions = check_additions(given_list, press_list)
			substitutions = len(press_list) - hits - additions
			order_error = check_order_error(given_list, press_list)

	trial_data = ({"correct": correct, "hits": hits, "substitutions": substitutions, "additions": additions, "order error": order_error})
	return trial_data