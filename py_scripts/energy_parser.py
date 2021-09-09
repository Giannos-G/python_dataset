#	
#	File name: energy_parser.py
#
#	This file contains all the functions for parsing information for specific part of data from valgrind output files
#
#	
#	Verion: 1.0
#	Last modified: 	28/02/2019
#
#	Author: Charalampos Marantos
#
#	THIS FILE NEEDS OPTIMIZATIONS AND BUG REMOVING
#

import collections
import itertools
import sys
import os.path
import csv
#from measure_time_energy import filename
#import measure_time_energy

# The temp directory to save temporary files
temp_dir = './temp/'

def find_annotated_line(line_text,file):
	line_number = 0
	with open(file) as myFile:
		for num, line in enumerate(myFile, 1):
			if line_text in line:
				line_number = num
	return line_number


def energy_results():
	line_start = "Start"
	line_end = "End"
	directory = "./"

    #initialize return values
	output = ["" for x in range(6)]
	line_info = []

	#check if file exists
	if not os.path.exists("module-power-input.txt"):
		output[0] = 0
		output[1] = 'No info available'
		return output, line_info

	line_start = find_annotated_line(line_start,"module-power-input.txt")
	line_end = find_annotated_line(line_end,"module-power-input.txt")
	# report module power
	f = open("module-power-input.txt")
	module_power = 0;
	suma = 0;
	flag_in = 0

	for num, line in enumerate(f,1):
		
		if num == line_end:
			flag_in = 0
			break

		if flag_in == 1:
			fields = line.split()		#split the line with whitespace as delimmiter
			module_power = module_power + int(fields[0])
			suma = suma + 1

		if num == line_start:		#find the begining of the specified area aof the code
			flag_in = 1

	module_power = float(module_power)/suma
	line_start = max(1,line_start - 1)
	line_end = line_end - 1

	# report gpu power
	f = open("GPU-power.txt")
	gpu_power = 0;
	suma = 0;
	flag_in = 0

	for num, line in enumerate(f,1):
		
		if num == line_end:
			flag_in = 0
			break

		if flag_in == 1:
			fields = line.split()		#split the line with whitespace as delimmiter
			gpu_power = gpu_power + int(fields[0])
			suma = suma + 1

		if num == line_start:		#find the begining of the specified area aof the code
			flag_in = 1

	#average module power
	gpu_power = float(gpu_power)/suma

	# report cpu power
	f = open("CPU-power.txt")
	cpu_power = 0;
	suma = 0;
	flag_in = 0

	for num, line in enumerate(f,1):
		
		if num == line_end:
			flag_in = 0
			break

		if flag_in == 1:
			fields = line.split()		#split the line with whitespace as delimmiter
			cpu_power = cpu_power + int(fields[0])
			suma = suma + 1

		if num == line_start:		#find the begining of the specified area aof the code
			flag_in = 1

	#average module power
	cpu_power = float(cpu_power)/suma

	# report time
	f = open("prof_time.txt")
	prof_time = 0;
	flag_in = 0

	for num, line in enumerate(f,1):
		
		if num == line_end:
			flag_in = 0
			break

		if flag_in == 1:
			fields = line.split()		#split the line with whitespace as delimmiter
			prof_time = prof_time + int(fields[0])

		if num == line_start:		#find the begining of the specified area aof the code
			flag_in = 1

	module_energy = (module_power/1000)*(float(prof_time)/1000)
	cpu_energy = (cpu_power/1000)*(float(prof_time)/1000)
	gpu_energy = (gpu_power/1000)*(float(prof_time)/1000)
	total = module_energy + cpu_energy + gpu_energy

	#print 'module_energy: ', module_energy;
	#print 'cpu_energy: ', cpu_energy;
	#print 'gpu_energy: ', gpu_energy;
	#print module_energy, cpu_energy, gpu_energy, total
        print "energy (Joule) = "
	print  module_energy
	return module_energy
	
#	with open('Energy_Profiling_on_nano.csv', 'ab',  )as f:
#		thewriter=csv.writer(f)
#		thewriter.writerow([filename, module_energy])
        
