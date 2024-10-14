print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

for i in range(1,11):
    """
    This method uses a for loop to create a chain list of 
    number that adds the number before it and then repeats 
    this method 10 times using the range of 1 to 11 in 
    parenthesis in the for loop. 

    Arg: "1, 11" keeps the range of the for loop from to 11.

    Return: previous number and x_sum
    """
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    previous_num = i