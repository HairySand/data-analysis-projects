food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
cargo_hold = [food, equipment, pets, sleep_aids]
cabinet_total = len(cargo_hold)
cabinet_number_holder= 0
for cabinet in cargo_hold:
    cabinet.lower
    cabinet = cabinet.split(",")
    cabinet.sort()
    cargo_hold[cabinet_number_holder] = cabinet
    cabinet_number_holder += 1
   
    # print(cabinet)
# print(cargo_hold)
# print(cargo_hold[1][0])


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.



# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
# cabinet_selection = int(input("Please select a cabinet (0-{0}):    ".format(cabinet_total-1)))
# if cabinet_selection > cabinet_total -1 or cabinet_selection < 0:
#    print("You entered an invalid cabinet number, please try again!")
# else:
#     print("The cabinet you selected contains: {0}".format(cargo_hold[cabinet_selection]))


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.



# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
cabinet_selection = int(input("Please select a cabinet (0-{0}):    ".format(cabinet_total-1)))
if cabinet_selection > cabinet_total -1 or cabinet_selection < 0:
   print("You entered an invalid cabinet number, please try again!")
else:
    print("The cabinet you selected contains: {0}".format(cargo_hold[cabinet_selection]))

item_selection = str(input("Please select an item from the cabinet:"))
item_selection.lower
if item_selection in cargo_hold[cabinet_selection]:
    print("The item you selected is: {0}".format(item_selection))
else:
    print("Item does not exist.")
