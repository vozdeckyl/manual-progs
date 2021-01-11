#!/usr/bin/env python3

# Jack Bigej
# Smart School Councils

# This program generates the data table for the symphony question. It uses an input text file formatted similar to the first program (staff briefing) as follows:

#		School Name:Exact Question:csv_file_name

# Examples:
#	Grove Primary School:What is the best time to wake up on Christmas Day?:school_12140
#	George White Junior School: What time is it OK to wake up on Christmas Day?:school_11000

# Mandatory Components:
#	1. Run gen_symph_school_list.py
#	2. Look up and download the csv files for each of the schools in the generated school list, move these files into the folder this program is in, and fill in the csv_file_name portion of the school list.

# Execution:
#	1. Ensure that the program is executable by typing 'chmod +x chart_symph_qs.py' (you only have to do this once ever for every program of mine that you download)
#	2. './chart_symph_qs.py < school_list.txt'

# Results:
#	This program will create a file called symphonyQ_data.csv

import sys
import csv


def main():
	with open('symphonyQ_data.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['School', 'Question', 'Key Stage','No. Groups','Question Option 1', 'Question Option 2', 'Question Option 3', 'Question Option 4', 'Votes 1', 'Votes 2', 'Votes 3', 'Votes 4'])


	all_rows = []

	for info in sys.stdin:
		info = info.rstrip()
		info = info.split(':')

		school_name = info[0]
		question = info[1]
		csv_file = info[2] + '.csv'
		print(school_name)
		print(question)

		if csv_file != '*.csv':
			with open(csv_file) as csvfile:
				reader = csv.reader(csvfile)
				curr_school = ""


				for row in reader:
					if row[2] == question:
						new_row = []
						
						if school_name == curr_school:
							new_row.append("")
							new_row.append("")
						else:
							new_row.append(school_name)
							new_row.append(question)
							curr_school = school_name

						new_row.append(row[6])
						new_row.append(row[7])
						new_row.append(row[10])
						new_row.append(row[11])
						new_row.append(row[12])
						new_row.append(row[13])
						new_row.append(row[14])
						new_row.append(row[15])
						new_row.append(row[16])
						new_row.append(row[17])

						all_rows.append(new_row)

	with open('symphonyQ_data.csv', 'a', newline='') as csvfile:
		writer = csv.writer(csvfile)
		for row in all_rows:
			writer.writerow(row)


if __name__ == "__main__":
	main()
