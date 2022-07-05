from random import shuffle
from math import floor

#Num of Elements to be sorted
test_limit = int(input("Enter the test limit: \n"))
print("\n\n")
number_of_tests = int(input("Enter the number of tests: \n"))
ar_of_num_of_steps = []

for i in range(number_of_tests):
    arr_of_numbers = []
    objective_ar = []
    for i in range(1, test_limit+1):
        arr_of_numbers.append(int(i))
        objective_ar.append(int(i))

    shuffle(arr_of_numbers)

    print(arr_of_numbers)

    def comparation_and_swap(num1, num2):
        if num1<= num2:
            return num1, num2
        else:
            return num2, num1

    num_of_steps = 0

    while arr_of_numbers != objective_ar:
        for num_of_el in range(test_limit-1):
            num_of_steps+=1
            temp_num1, temp_num2 = comparation_and_swap(arr_of_numbers[num_of_el],arr_of_numbers[num_of_el+1])
            arr_of_numbers[num_of_el] = temp_num1
            arr_of_numbers[num_of_el+1] = temp_num2
            print(arr_of_numbers)
            if arr_of_numbers == objective_ar:
                break

    print("\n\n\n Total Number of Steps: {}\n\n\n".format(num_of_steps))

    ar_of_num_of_steps.append(int(num_of_steps))

#Average Calculation

temp_calculation = 0

for element in ar_of_num_of_steps:
    temp_calculation += element

average = temp_calculation/number_of_tests

print("---------------------------")
print("\n\nThe average of steps for a {} numbers list is {}\n\n".format(test_limit, floor(average)))
