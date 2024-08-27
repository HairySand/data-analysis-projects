flavors = {
  'chocolate' : 0.35,
  'vanilla' : 0.35,
  'strawberry' : 0.42,
  'cookies and cream' : 0.45,
  'mint chocolate chip' : 0.42,
  'fudge chunk' : 0.45,
  'saffron' : 2.25,
  'garlic' : 0.05
}

## Set a variable called choice to the flavor you want to search for.

cost = 0
while cost == 0:
  choice = input("What flavor do you want?  ")
## Use an if statement to check if choice is in the flavors dictionary.
  if choice in flavors:


## If it is, set another variable called cost to the value associated with choice.
      cost = flavors[choice]
      print(f"That will be ${cost}")
## If it isn’t, set cost to 0.
  else:
    print("We don't have that flavor at this time? Please choose another flavor.")
    cost = 0
## Print the cost.
## See above. I made the stuff a little more complicated.

### Search a Dictionary Part 2:

## Initialize two variables: highest_cost to 0 and fanciest to an empty string.
highest_cost = 0
fanciest = ""

## Loop through the flavors dictionary using a for loop.

for flavor in flavors.keys():

## For each flavor, check if its price is higher than highest_cost.
  if flavors[flavor] > highest_cost:

## If it is, update fanciest to this flavor and highest_cost to its price.
    fanciest = flavor
    highest_cost = flavors[flavor]
## After the loop, print the most expensive flavor.
print(f"The fanciest flavor is {fanciest} at ${flavors[fanciest]}.")