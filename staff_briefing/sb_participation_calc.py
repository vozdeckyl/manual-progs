#!/usr/bin/env python3

# Jack Bigej
# Smart School Councils

#For each school, this program reads their csv file, counts their number of questions and respondants for each question, calculates the percentage of the school's participation for each question on average, and formats/writes all of this information as a csv file.

#There is a lot of data that's not on the csv files which is neccessary for this program. The neccessary information is the name of the school, whether it attended staff briefing, and how many classes the school has. Furthermore I needed a way to relate the school name to the correct csv file. I didn't wanna try web scraping atm so I created a standard input text file to relay this information. The format of the file is as follows:

#	SCHOOL NAME:YES/NO (staff briefing):csv_file_name:# of classes

# Examples:
#	TRINITY PRIMARY SCHOOL HEREFORD:No:school_14950:20
#	ALL SAINTS CE PRIMARY SCHOOL:Yes:school_14916:13

# Mandatory Components:
#	1. Download and store all csv files you are planning to use in the folder immediately surrounding this program.
#   2. You need a text file formatted as shown above with the school information you want to chart.

# To execute the program type what's in 'quotes'in the terminal excluding the quotes themselves:
#	1. In the terminal make sure that program.py has executable permissions. (if you don't know, type:: 'chmod +x sb_participation_calc.py')
#	2. './sb_participation_calc.py < info.txt' where info.txt is the standard input text file

import csv
import sys

def main():
	
	with open('data.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['School', 'Staff Briefing (Y/N)', 'Number of Classes','Number of Questions', 'Total Participation % for all questions', 'Participation % for each question'])
	for info in sys.stdin:
		info = info.rstrip()
		info = info.split(':')
		data = []
		dates = []
		school = info[0]
		training = info[1]
		csv_file = info[2] + '.csv'
		num_classes = 0
		if len(info) > 3:
			if info[3] != '*':
				num_classes = int(info[3])

		if csv_file != '*.csv':
			with open(csv_file) as csvfile:
				reader = csv.reader(csvfile)
				q_id = -1
				q_date = ""
				count = 0
				for row in reader:
					line = ' '.join(row)
					split_row = line.split()
					if len(split_row) == 0:
						continue

					if split_row[0].isnumeric():
						if q_id == -1:
							q_id = int(split_row[0])
							q_date = str(split_row[1])
							dates.append(q_date)
							count = 1
						elif int(split_row[0]) == q_id:
							count += 1
						else:
							print('Q ' + str(q_id) + ':', count)
							data.append(count)
							num_classes = max(num_classes, count)
							count = 1
							q_id = int(split_row[0])
							q_date = str(split_row[1])
							dates.append(q_date)

				num_classes = max(num_classes, count)
				print('Q ' + str(q_id) + ':', count)
				data.append(count)
				print('Num Classes:', num_classes)

		print(data)
		data_percent = []
		total_participation = 0
		if num_classes > 0:
			data_percent = [float(x/num_classes) for x in data]
			total_participation = sum(data)/(num_classes * len(data))
			print(data_percent)
			print(total_participation)

		with open('data.csv', 'a', newline='') as csvfile:
			writer = csv.writer(csvfile)
			row_to_write = []
			row_to_write.append(school)
			row_to_write.append(training)
			row_to_write.append(num_classes)
			row_to_write.append(len(data))
			row_to_write.append(round(total_participation, 3))
			for i, p in enumerate(data_percent):
				if len(data) == 1:
					if data[0] == 0:
						row_to_write.append("")
				else:
					print(dates)
					print(data)
					row_to_write.append(str(dates[i]) + ':  ' + str(round(p, 3)))
			writer.writerow(row_to_write)



if __name__ == "__main__":
	main()
