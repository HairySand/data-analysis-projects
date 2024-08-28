my_string = input("What is your string?  ").strip().lower()
input_number = int(input("How many characters do you want to move?  "))
new_string = str("")
# a) Use string methods to remove the first three characters from the string and add them to the end.

if input_number > len(my_string):
    print("We can't change more letters than in the word. Please put in a number less than the number of letters in the word you input. Please try again.")
else:
    first_letters = my_string[0:input_number]
    my_string = my_string.replace(first_letters, "")
    new_string = my_string + first_letters

print("The original String: {0} New String: {1}".format(my_string, new_string))



# Use a template literal to print the original and modified string in a descriptive phrase.




# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.


# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.





# my_string = str(input("What word do you want us to change?   "))
# num_input = int(input("How many letters should we change?   "))
# my_string = my_string.strip()



# if num_input > len(my_string):
#     print("We can't change more letter than in the word. Please put in a number less than the number of letters in the word you input. Please try again.")
# else:
#     my_string = my_string.strip()
#     first_letters = my_string[0 : num_input]
#     new_string = my_string.replace(first_letters,"", 1)
#     new_string = new_string + first_letters

#     print("Your old word was {0}, your new word is {1}".format(my_string, new_string))