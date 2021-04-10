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
	all_rows = []
	number_of_options_list = []
	
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
				number_of_options = -1

				for row in reader:
					if row[2] == question:
						#get rid of the comments at the end (to currently estimate the number of options)
						for n in range(len(row)-1,-1,-1):
							if not row[n].isdigit():
								del row[n]
							else:
								break
						
						# deduce the number of options from the number of columns
						if number_of_options == -1:
							#if not initialized
							if (len(row) - 10)%2 != 0:
								#there must be same number of options as answers
								raise Exception("Inconsistent columns in file {}, session {}, class {}.".format(csv_file,row[0],row[5]))
							number_of_options = int((len(row) - 10)/2)
							number_of_options_list.append(number_of_options)
						else:
							if number_of_options != int((len(row) - 10)/2):
								raise Exception("Inconsistent columns in file {}, session {}, class {}.".format(csv_file,row[0],row[5]))
						new_row_info = []
						new_row_options = []
						new_row_votes = []
						
						if school_name == curr_school:
							new_row_info.append("")
							new_row_info.append("")
						else:
							new_row_info.append(school_name)
							new_row_info.append(question)
							curr_school = school_name

						new_row_info.append(row[6])
						new_row_info.append(row[7])

						for n in range(10, 10 + number_of_options):
							new_row_options.append(row[n])
						
						for n in range(10+number_of_options, 10 + 2*number_of_options):
							new_row_votes.append(row[n])
						
						"""
						new_row.append(row[10])
						new_row.append(row[11])
						new_row.append(row[12])
						new_row.append(row[13])
						new_row.append(row[14])
						new_row.append(row[15])
						new_row.append(row[16])
						new_row.append(row[17])
						"""

						all_rows.append((new_row_info,new_row_options,new_row_votes))

	with open('symphonyQ_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
		writer = csv.writer(csvfile)

		header = ['School', 'Question', 'Key Stage','No. Groups']

		for n in range(1,max(number_of_options_list)+1):
			header.append('Question Option {}'.format(n))

		for n in range(1,max(number_of_options_list)+1):
			header.append('Votes {}'.format(n))
		
		writer.writerow(header)

		for new_row_info,new_row_options,new_row_votes in all_rows:
			blank_spaces = max(number_of_options_list) - len(new_row_votes)
			row = new_row_info + new_row_options + [""]*blank_spaces + new_row_votes + [""]*blank_spaces
			writer.writerow(row)


if __name__ == "__main__":
	main()
