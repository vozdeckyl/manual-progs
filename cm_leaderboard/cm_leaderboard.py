#!/usr/bin/python3

# Jack Bigej
# Smart School Councils

# This program generates csv files (tables) for Class Meeting Statistics. It requires the School Meetings CSV file from WordPress.

# Mandatory Components:
#	1. Look up and download the csv file for all class meetings information. Save this CSV File in the local folder and rename it school_questions.csv. 

# Execution:
#	1. Ensure that the program is executable by typing 'chmod +x cm_leaderboard.py' (you only have to do this once ever for each program of mine that you download)
#	2. './cm_leaderboard.py'

# Results:
#	This program will create five csv files holding the top schools in each of the five categories and will be named respectively. 

import sys
import csv
from datetime import *
import datetime


def school_sort(school):
	return school['count']

def evaluate_top(schools):
		if len(schools) > 5:
			i = 5
			while i < len(schools) and schools[i]['count'] == schools[4]['count']:
				i += 1
			return schools[0:i]

		else:
			return schools

def compile_schools(school_dict):
	schools = []

	for school in school_dict:
		temp_dict = {}
		temp_dict['name'] = school
		temp_dict['count'] = school_dict[school]
		schools.append(temp_dict)

	return schools

def great_start():

	with open('school_questions.csv') as csvfile:
		reader = csv.reader(csvfile)
		school_name = ""
		school_dict = {}
		schools = []

		today = datetime.date.today()
		deadline = today - timedelta(days = 30)

		for row in reader:
			if len(row) != 3:
				continue

			school_name = row[0]
			session_date = row[1].split('/')
			if len(session_date) < 3:
				continue

			date = datetime.date(int(session_date[2]), int(session_date[1]), int(session_date[0]))

			if school_name == "" or school_name == "Coronavirus Daily Debates":
				continue

			
			if school_name in school_dict:
				school_dict[school_name]['count'] += 1
			else:
				temp_dict = {}
				temp_dict['count'] = 1
				temp_dict['date'] = date
				school_dict[school_name] = temp_dict

		schools = []

		for school in school_dict:
			if school_dict[school]['count'] == 1:
				if school_dict[school]['date'] > deadline:
					temp_dict = {}
					temp_dict['name'] = school
					temp_dict['count'] = str(school_dict[school]['date'])
					schools.append(temp_dict)

		schools.sort(reverse=True, key=school_sort)
		top_schools = evaluate_top(schools)

		print('Great Starts:', top_schools)

	with open('great_start.csv', 'w+') as csvfile:
		writer = csv.writer(csvfile)

		writer.writerow(['School', 'Meetings'])

		for school in top_schools:
			writer.writerow([school['name'], school['count']])

def top_trending():

	with open('school_questions.csv') as csvfile:
		reader = csv.reader(csvfile)
		school_name = ""
		school_dict = {}
		schools = []

		today = datetime.date.today()
		deadline = today - timedelta(days = 30)

		for row in reader:
			if len(row) != 3:
				continue

			school_name = row[0]
			session_date = row[1].split('/')
			if len(session_date) < 3:
				continue

			date = datetime.date(int(session_date[2]), int(session_date[1]), int(session_date[0]))

			if date < deadline:
				continue
			
			if school_name == "" or school_name == "Coronavirus Daily Debates":
				continue

			

			if school_name in school_dict:
				school_dict[school_name] += 1
			else:
				school_dict[school_name] = 1

		schools = compile_schools(school_dict)
		schools.sort(reverse=True, key=school_sort)
		top_schools = evaluate_top(schools)

		print('Top Trending:', top_schools)

	with open('top_trending.csv', 'w+') as csvfile:
		writer = csv.writer(csvfile)

		writer.writerow(['School', 'Meetings'])

		for school in top_schools:
			writer.writerow([school['name'], school['count']])

def top_term():

	with open('school_questions.csv') as csvfile:
		reader = csv.reader(csvfile)
		school_name = ""
		school_dict = {}
		schools = []
		today = datetime.date.today()
		current_date = str(datetime.date.today()).split('-')

		summer_start = datetime.date(int(current_date[0]), 4, 12)
		summer_end = datetime.date(int(current_date[0]), 7, 31)

		spring_start = datetime.date(int(current_date[0]), 1, 1)
		spring_end = datetime.date(int(current_date[0]), 4, 11)

		autumn_start = datetime.date(int(current_date[0]), 9, 1)
		autumn_end = datetime.date(int(current_date[0]), 12, 31)

		current_start = datetime.date.today()
		current_end = datetime.date.today()

		if today <= spring_end and today >= spring_start:
			current_start = spring_start
			current_end = spring_end
		elif today <= summer_end and today >= summer_start:
			current_start = summer_start
			current_end = summer_end
		elif today <= autumn_end and today >= autumn_start:
			current_start = autumn_start
			current_end = autumn_end

		for row in reader:
			if len(row) != 3:
				continue

			school_name = row[0]
			session_date = row[1]
			date = session_date.split('/')
			
			if len(date) < 3:
				continue

			if school_name == "" or school_name == "Coronavirus Daily Debates":
				continue

			session_date = datetime.date(int(date[2]), int(date[1]), int(date[0]))

			if session_date > current_end or session_date < current_start:
				continue

			if school_name in school_dict:
				school_dict[school_name] += 1
			else:
				school_dict[school_name] = 1

		schools = compile_schools(school_dict)
		schools.sort(reverse=True, key=school_sort)
		top_schools = evaluate_top(schools)
	
		print('Top Schools This Term:', top_schools)

	with open('top_term.csv', 'w+') as csvfile:
		writer = csv.writer(csvfile)

		writer.writerow(['School', 'Meetings'])

		for school in top_schools:
			writer.writerow([school['name'], school['count']])

def top_year():

	with open('school_questions.csv') as csvfile:
		reader = csv.reader(csvfile)
		school_name = ""
		school_dict = {}
		schools = []
		current_date = str(datetime.date.today()).split('-')


		for row in reader:
			if len(row) != 3:
				continue

			school_name = row[0]
			session_date = row[1]
			date = row[1].split('/')
			
			if len(date) < 3:
				continue

			if school_name == "" or school_name == "Coronavirus Daily Debates":
				continue

			if date[2] != current_date[0]:
				continue

			if school_name in school_dict:
				school_dict[school_name] += 1
			else:
				school_dict[school_name] = 1
		
		schools = compile_schools(school_dict)
		schools.sort(reverse=True, key=school_sort)
		top_schools = evaluate_top(schools)
	
		print('Top Schools This Year:', top_schools)

	with open('top_year.csv', 'w+') as csvfile:
		writer = csv.writer(csvfile)

		writer.writerow(['School', 'Meetings'])

		for school in top_schools:
			writer.writerow([school['name'], school['count']])

def top_alltime():


	with open('school_questions.csv') as csvfile:
		reader = csv.reader(csvfile)
		school_name = ""
		school_dict = {}
		schools = []


		for row in reader:
			if len(row) != 3:
				continue

			school_name = row[0]

			if school_name == "":
				continue

			if school_name in school_dict:
				school_dict[school_name] += 1
			else:
				school_dict[school_name] = 1

		schools = compile_schools(school_dict)
		schools.sort(reverse=True, key=school_sort)
		top_schools = evaluate_top(schools)
		
		print('Top Schools All Time:', top_schools)

	with open('top_alltime.csv', 'w+') as csvfile:
		writer = csv.writer(csvfile)

		writer.writerow(['School', 'Meetings'])

		for school in top_schools:
			writer.writerow([school['name'], school['count']])

def main():
	top_alltime()
	print()
	top_year()
	print()
	top_term()
	print()
	top_trending()
	print()
	great_start()

if __name__ == '__main__':
	main()
