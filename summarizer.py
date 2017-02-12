import csv

def data_summary(data_dict, output_filepath): # calculate summary analyses and output to a new csv file
	summary_dict = ({})

	# C# = condition # (e.g. C3 = condition 3 = 3 balls are dropped in that condition)
	column_labels = ["Patient", "Session", "% Correct", "% Correct C1", "% Correct C2", "% Correct C3", "% Correct C4", "% Hits", "% Hits C1", "% Hits C2", "% Hits C3", "% Hits C4", "Substitutions", "Subs C1", "Subs C2", "Subs C3", "Subs C4", "Additions", "Adds C1", "Adds C2", "Adds C3", "Adds C4", "Order Errors", "OE C2", "OE C3", "OE C4"]
	# Note: OE 1 would always be 0

	with open(output_filepath, 'w', newline = '') as new_csvfile:
		writer = csv.DictWriter(new_csvfile, fieldnames = column_labels)
		writer.writeheader()

		for patient_key, patient in sorted(data_dict.items()):
			for session_key, session in patient.items():
				total_ball_drops = 0
				total_correct = 0		
				total_hits = 0
				total_substitutions = 0
				total_additions = 0
				total_order_errors = 0

				total_c1_trials = 0
				total_c2_trials = 0
				total_c3_trials = 0
				total_c4_trials = 0
				correct_c1 = 0
				correct_c2 = 0
				correct_c3 = 0
				correct_c4 = 0
				hits_c1 = 0
				hits_c2 = 0
				hits_c3 = 0
				hits_c4 = 0
				substitutions_c1 = 0
				substitutions_c2 = 0
				substitutions_c3 = 0
				substitutions_c4 = 0
				additions_c1 = 0
				additions_c2 = 0
				additions_c3 = 0
				additions_c4 = 0
				oe_c2 = 0
				oe_c3 = 0
				oe_c4 = 0

				for trial_key, trial in session.items():
					correct = trial['correct']
					hits = trial['hits']
					substitutions = trial['substitutions']
					additions = trial['additions']
					order_error = trial['order error']
					condition = trial['condition']

					total_ball_drops = total_ball_drops + condition
					total_correct = total_correct + correct
					total_hits = total_hits + hits
					total_substitutions = total_substitutions + substitutions
					total_additions = total_additions + additions
					total_order_errors = total_order_errors + order_error

					if condition == 1:
						total_c1_trials = total_c1_trials + 1
						correct_c1 = correct_c1 + correct
						hits_c1 = hits_c1 + hits
						substitutions_c1 = substitutions_c1 + substitutions
						additions_c1 = additions_c1 + additions
					elif condition == 2:
						total_c2_trials = total_c2_trials + 1
						correct_c2 = correct_c2 + correct
						hits_c2 = hits_c2 + hits
						substitutions_c2 = substitutions_c2 + substitutions
						additions_c2 = additions_c2 + additions
						oe_c2 = oe_c2 + order_error
					elif condition == 3:
						total_c3_trials = total_c3_trials + 1
						correct_c3 = correct_c3 + correct
						hits_c3 = hits_c3 + hits
						substitutions_c3 = substitutions_c3 + substitutions
						additions_c3 = additions_c3 + additions
						oe_c3 = oe_c3 + order_error
					elif condition == 4:
						total_c4_trials = total_c4_trials + 1
						correct_c4 = correct_c4 + correct
						hits_c4 = hits_c4 + hits
						substitutions_c4 = substitutions_c4 + substitutions
						additions_c4 = additions_c4 + additions
						oe_c4 = oe_c4 + order_error

				percent_correct = (total_correct/40)*100
				percent_correct_c1 = (correct_c1/total_c1_trials)*100
				percent_correct_c2 = (correct_c2/total_c2_trials)*100
				percent_correct_c3 = (correct_c3/total_c3_trials)*100
				percent_correct_c4 = (correct_c4/total_c4_trials)*100

				percent_hits = (total_hits/total_ball_drops)*100
				total_c1_ball_drops = total_c1_trials
				total_c2_ball_drops = total_c2_trials*2
				total_c3_ball_drops = total_c3_trials*3
				total_c4_ball_drops = total_c4_trials*4
				percent_hits_c1 = (hits_c1/total_c1_ball_drops)*100
				percent_hits_c2 = (hits_c2/total_c2_ball_drops)*100
				percent_hits_c3 = (hits_c3/total_c3_ball_drops)*100
				percent_hits_c4 = (hits_c4/total_c4_ball_drops)*100

				summary_dict = {"Patient": patient_key, "Session": session_key, "% Correct": percent_correct, "% Correct C1": percent_correct_c1, "% Correct C2": percent_correct_c2, "% Correct C3": percent_correct_c3, "% Correct C4": percent_correct_c4, "% Hits": percent_hits, "% Hits C1": percent_hits_c1, "% Hits C2": percent_hits_c2, "% Hits C3": percent_hits_c3, "% Hits C4": percent_hits_c4, "Substitutions": total_substitutions, "Subs C1": substitutions_c1, "Subs C2": substitutions_c2, "Subs C3": substitutions_c3, "Subs C4": substitutions_c4, "Additions": total_additions, "Adds C1": additions_c1, "Adds C2": additions_c2, "Adds C3": additions_c3, "Adds C4": additions_c4, "Order Errors": total_order_errors, "OE C2": oe_c2, "OE C3": oe_c3, "OE C4": oe_c4}
				writer.writerow(summary_dict)