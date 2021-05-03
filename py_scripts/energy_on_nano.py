# python measure_time_energy.py "python example.py" 2
# Output:
# "output of the example file"
# time = ...
# ... (Joule)

import os

#print (os.listdir())
x = os.listdir()
print (x)
for i in x: 
    print ("python script: "+ i)
    qoutes = '"'
    if ((i != "energy_on_nano.py") and (i != "README.md")):
        command = "python measure_time_energy.py " + qoutes + "python " + i + qoutes + " 2"
        #print ("python measure_time_energy.py " + qoutes + "python example.py" + qoutes + " 2")
        print (command)
        #os.system(command)
    #else:
        #print ("found " + i)
    print ("-----------------------------------------")
