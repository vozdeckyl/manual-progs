#!/usr/bin/env python3

import sys
import csv

def sort_num_groups(num_groups):
	return num_groups['num_groups']

def sort_num_parts(num_parts):
	return num_parts['num_parts']

def num_groups_chart(num_groups):

	num_groups_list = []

	for key in num_groups.keys():
		temp = {}
		temp['school'] = key
		temp['num_groups'] = num_groups[key]

		num_groups_list.append(temp)

	num_groups_list.sort(reverse=True, key=sort_num_groups)



	with open('HDC_num_groups_lb.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['School', 'Total No. Groups'])

		for school in num_groups_list:
			writer.writerow([school['school'], school['num_groups']])

def num_parts_chart(num_parts):
	
	num_parts_list = []

	for key in num_parts.keys():
		temp = {}
		temp['school'] = key
		temp['num_parts'] = num_parts[key]

		num_parts_list.append(temp)

	num_parts_list.sort(reverse=True, key=sort_num_parts)



	with open('HDC_num_participants_lb.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['School', 'Total No. Participants'])

		for school in num_parts_list:
			writer.writerow([school['school'], school['num_parts']])

def ind_school_chart(ores):
	for school in ores.keys():
		csv_name = '-'.join(school.split(' ')) + '.csv'

		with open(csv_name, 'w', newline='') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(['Answer', 'No. Votes', '%'])
			
			no = 0
			yes = 0

			if 'No' in ores[school]:
				no += ores[school]['No']
			if 'Yes' in ores[school]:
				yes += ores[school]['Yes']

			total = no + yes

			writer.writerow(['Yes', yes, float(yes/total)])
			writer.writerow(['No', no, float(no/total)])

def proc_overall(ores):
	with open('HDC_overall_results.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Answer', 'No. Votes', '%'])

		no = 0
		yes = 0

		for school in ores:
			if 'No' in ores[school]:
				no += ores[school]['No']
			if 'Yes' in ores[school]:
				yes += ores[school]['Yes']

		total = no + yes
		writer.writerow(['Yes', yes, float(yes/total)])
		writer.writerow(['No', no, float(no/total)])

def part_schools_chart(part_schools):
	with open('HDC_part_schools.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['School'])

		for school in part_schools.keys():
			writer.writerow([school])


def general_charting(all_rows):
	with open('HDC_data.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['School', 'Question', 'Key Stage', 'No. Groups', 'Question Option 1', 'Question Option 2', 'Question Option 3', 'Question Option 4', 'Votes 1', 'Votes 2', 'Votes 3', 'Votes 4'])
		for row in all_rows:
			writer.writerow(row)

def main():

	#TODO: Prioritize 2, 3, 5 in order

	#1. List of participating schools
	#2. Leaderboard of schools with highest number of groups taking part
	#3. Leaderboard of schools with the highest number of participants (over 199 removed)
	#4. New schools who have no participated before.... (kinda hard)
	#5. The actual resutls, numbers for each side (participants over 199 removed)
	#6. Create seperate csv files for each school that participated
	#7. Pull from text responses

	'''
	List format:
		School:Question:csvfile
	'''

	all_rows = []
	part_schools = set()
	num_groups = {} #Used for 2
	num_parts = {}
	overall_results = {}
	ind_schools = {}

	with open('debate.csv') as csvfile:
		reader = csv.reader(csvfile)
		
		for row in reader:
			if row[3].strip() == 'Number of debaters':
				continue
			
			school_title = ' '.join(row[4].split(' ')[:-2]).upper()

			if school_title in num_groups:
				num_groups[school_title] += 1
			else:
				num_groups[school_title] = 1



			if int(row[3]) > 199:
				continue

			if school_title in overall_results:
				overall_results[school_title]
				if row[0] in overall_results[school_title]:
					overall_results[school_title][row[0]] += int(row[3])
				else:
					overall_results[school_title][row[0]] = int(row[3])

			else:
				overall_results[school_title] = {}
				overall_results[school_title][row[0]] = int(row[3])


			if school_title in num_parts:
				num_parts[school_title] += int(row[3])
			else:
				num_parts[school_title] = int(row[3])


	print('Generating Participating Schools...')
	part_schools_chart(num_groups)
	
	print('Generating No. Groups LB...')
	num_groups_chart(num_groups)

	print('Generating No. Participants LB...')
	num_parts_chart(num_parts)
	
	print('Generating Individual School Results...')
	ind_school_chart(overall_results)
	
	print('Generating Overall Results...')
	proc_overall(overall_results)

if __name__ == '__main__':
	main()
