# python measure_time_energy.py "python example.py" 2
# Output:
# "output of the example file"
# time = ...
# ... (Joule)

import os

#print (os.listdir())
path = "/home/gavrielides/python_dataset/py_scripts"
x = os.listdir(path)
j = 448
#print (x)
for i in x: 
    j= j+1
    print ("python script: "+ i)   #x[j]
    qoutes = '"'
    if ((i != "energy_on_nano.py") and (i != "README.md")):
        command = "python measure_time_energy.py " + qoutes + "python3 " + i + qoutes + " 2"
        #print ("python measure_time_energy.py " + qoutes + "python example.py" + qoutes + " 2")
        #print (command)
	try:
        	os.system(command)
	except ModuleNotFoundError:
		print ("INSTALL THE LIBRARY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		break
    #else:
        #print ("found " + i)
    #if ImportError:
     #   print ("ERRORRRRRRRRRRR download the needed library")
      #  break
    #decision = input("Everything OK? (1 for yes/0 for no) \n")
    #if (decision == 0): break
    print ("-----------------------------------------")
