# Exercise #1: Construct for loops that accomplish the following tasks:
    # a. Print the numbers 0 - 20, one number per line.

# for number in range(21):
#         print(number)

    # b. Print only the ODD values from 3 - 29, one number per line.

# for oddnum in range(3,30,2):
#             print(oddnum)

#     # c. Print the EVEN numbers 12 to -14 in descending order, one number per line.

# for devn in range(12, -15, -2):
#         print(devn)

    # d. Challenge - Print the numbers 50 - 20 in descending order, but only if the numbers are multiples of 3. (Your code should work even if you replace 50 or 20 with other numbers).

topnum = 50
bottomnum = 18
for num in range(topnum, bottomnum-1, -1):
        if num%3 == 0:
            print(num)


