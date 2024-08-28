proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]



# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
# for string in range(len(strings)):
#     if "," in strings[string]:
#         print(f"{strings[string]} has commas.")
#     elif ";" in strings[string]:
#         print(f"{strings[string]} has semicolons.")
#     else:
#         print(f"{strings[string]} has spaces.")      


# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
for string in strings:
    if "," in string:
        comma_fixer = string.split(",")
        comma_fixer.reverse()
        new_comma_string = ','.join(comma_fixer)
        print(new_comma_string)
    # elif ";" in strings[string]:
    #     print(f"{strings[string]} has semicolons.")
    # else:
    #     print(f"{strings[string]} has spaces.")    


# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.

    elif ";" in string:
        sc_fixer = string.split(";")
        sc_fixer.sort()
        new_sc_string = ','.join(sc_fixer)
        print(new_sc_string)


# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.

    elif " " in string:
        if "," in string:
            comma_fixer = string.split(",")
            comma_fixer.reverse()
            new_comma_string = ','.join(comma_fixer)
            print(new_comma_string)
        else:
            space_fixer = string.split(" ")
            space_fixer.sort(reverse = True)
            new_space_string = ' '.join(space_fixer)
            print(new_space_string)

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
