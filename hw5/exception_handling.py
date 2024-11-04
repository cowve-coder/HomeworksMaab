#P1
#x, y= 100, 0
#try:
#    z = x / y
#except ZeroDivisionError:
#    print("cannot divide by zero!")

#P2
#try: 
#    a = int(input("Enter an integer number: "))
#except ValueError:
#    print("The number is not integer!")

#P3
#my_file = open("sumth.txt", 'r')
#try:
#    contents = my_file.read()
#    print(contents, '\n')
#    my_file.close()
#except FileNotFoundError:
#    print("There does not exist such file!")

#P4
#c = 0
#try:
#    a = float(input("enter a number of some sort: "))
#    b = input(("enter a number of some sort: "))
#    c = a * b
#except TypeError:
#    print("Error, number is not numerical")

#P5
#try:
#    file = open("restricted_file.txt", "w")
#    file.write("trying to write in a file.\n")
#except PermissionError:
#    print("cannot write this file!")
#    try:
#        file.close()
#    except NameError:
#        pass

#P6
#my_list = [10, 20, 30, 40, 50]
#try:
#    index = 10 
#    print("Element at index", index, "is:", my_list[index])
#except IndexError:
#    print("Index out of range!")

#P7
#try:
#    number = input("Please enter a number: ")
#    print("You entered:", number, "\n")
#except KeyboardInterrupt:
#    print("Input canceled by user.")

#P8
#try:
#    a = float(input("Enter a number: "))
#    b = float(input("Enter a number: "))
#    result = a / b
#    print("Result:", result)
#except ArithmeticError:
#    print("An arithmetic error: Cannot divide by zero.")

#P10
#my_list = [1, 2, 3, 4, 5]
#try:
#    my_list.append(6) 
#    print("List after append:", my_list)
#    my_list.some_sort_of_method()
#except AttributeError:
#    print("AttributeError: The specified method does not exist on the list.")