# Dummy Code containing multiple functions
#import cProfile

#@profile
def create_array():
  arr=[]
  for i in range(0,400000):
    arr.append(i)
  initialize_array(arr)


#@profile
def print_statement():
  print('Array created successfully')

#@profile
def initialize_array(my_array = [], *arr):
  for x in range(0,4000000):
    my_array.append(0)
  initialize_to_1_array (my_array)

#@profile
def initialize_to_1_array(my_array_1 = [], *my_array):
  for x in range(0,4000000):
    my_array_1.append(1)
  print('Array initialized to 1 successfully')

#@profile
def main():
  create_array()
  print_statement()


if __name__ == '__main__':
    main()
    #cProfile.run('main()')