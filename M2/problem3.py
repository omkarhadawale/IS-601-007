'''
Name: Omkar Karbhari Hadawale
UCID: oh45
Date:20/09/2022 

'''

a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # TODO add new code here to print the desired result
    """
    IF - If the item in the list is of type string then first converting it to int or float types.Then
    if its negative converting it to its respective positive value in int or float and finally 
    output as string. 

    ELSE - The items of type int and float will directly shown as ouput if positive else will be converted 
    to positive and then will be shown as output
    """
    for i in arr: 
        if type(i) == str:
            if '.' in i: # If a string contains '.' then it is a float else it will be integer
                print(i,end=', ') if float(i) > 0.0  else print((str(float(i)*-1)),end=', ') 
            else:
                print(i,end=', ') if int(i) > 0  else print((str(int(i)*-1)),end=', ')
        else :    
            print(i,end=', ') if type(i)(i) > type(i)(0)  else print((i*-1),end=', ') 


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
