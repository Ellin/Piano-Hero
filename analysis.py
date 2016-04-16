
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
	
	#press_list_mod = []
	# the following forloop removes all *adjacent* duplicates in inter_press_list
	# might be unnecessary
#	for i in range (inter_press_list.length):
#		if i >= inter_press_list.length - 1 or inter_press_list[i] != inter_press_list[i+1]:
#			press_list_mod.append(inter_press_list[i])
	order_hits = 0
	j = 0
	for i in range(len(press_list_mod)):
		if press_list_mod[i] == given_list_mod[j]:
			order_hits = order_hits + 1
			if len(given_list_mod) - 1 > j:
				j = j + 1

	if order_hits < len(given_list_mod):
		order_error = True

def analyze_trial(given_list, press_list):
	correct = False				# 1 = user_list is correct; 0 = incorrect
	order_error = False		# 1 = atleast one element in user_list is in the wrong order
	hits = 0				# element in user_list is in given_list and is not excessive
	substitutions = 0	# element in user_list is not in given_list or is excessive
	additions = 0		# excessive elements in user_list; user_list > given_list

	intersection_list = list(set(press_list) & set(given_list))
	print ("intersection: " + str(intersection_list))

	if press_list != []: 
		correct = check_correct(given_list, press_list)
		if correct:
			hits = len(given_list)
		else:
			hits = len(intersection_list)	# hits = length of list of intersection of press_list & given_list
			additions = check_additions(given_list, press_list)
			substitutions = len(press_list) - hits - additions
			check_order_error(given_list, press_list)
	print ("correct: " + str(correct))
	print ("hits: " + str(hits))
	print ("additions: " + str(additions))
	print ("substitutions: " + str(substitutions))
	print ("OE: " + str(order_error))

given_list = [4, 1, 2, 3]
press_list = []
print (analyze_trial(given_list, press_list))