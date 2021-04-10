#!/usr/bin/env python3

# Jack Bigej
# Smart School Councils

# This program is used to compile a list of schools that participated in the Symphony Question.

# Mandatory Components: 
# 	1. Must have the all questions csv downloaded and in the same folder as this program

# Execution:
#	1. Ensure that the program is executable by typing 'chmod +x gen_symph_school_list.py' (you only have to do this once ever for every program of mine that you download)

#   2. './gen_symph_school_list.py "Symphony Question of the week"' where "Symph..." is the actual question of the week.

# Results:
#	This program will create a partially completed text file input for use in chart_symph_qs.py called school_list.txt

import sys
import csv

def create_dict(question):
	q_dict = {}
	question = question.split()

	for w in question:
		word = w.rstrip()
		word = word.lower()
		if word in q_dict:
			q_dict[word] += 1
		else:
			q_dict[word] = 1

	return q_dict

def main():

	question = ""
	week = "11/12/2020"

	if len(sys.argv) > 1:
		question = sys.argv[1]

	if len(sys.argv) > 2:
		week = sys.argv[2]

	with open('school_questions.csv', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile)
		
		school_name = ""
		q_dict = create_dict(question)
		total_words = 0
		recorded_schools = dict()

		for key in q_dict.keys():
			total_words += q_dict[key]

		print(total_words)

		print(q_dict)

		for row in reader:
			if len(row) != 3:
				continue

			school_name = row[0]
			r_dict = create_dict(row[2])

			#print(r_dict)

			matching_words = 0

			for key in q_dict.keys():
				if key in r_dict:
					matching_words += min(r_dict[key], q_dict[key])

			if float(matching_words/total_words) > .80:
				if school_name in recorded_schools:
					continue

				print(row)
				recorded_schools[school_name] = row[2]
				

		print(recorded_schools)
		with open('school_list.txt', 'w+', encoding='utf-8') as textfile:
			for school in recorded_schools:
				textfile.write(str(school) + ':' + str(recorded_schools[school]) + ':school_' + '\n')

if __name__ == '__main__':
	main()
