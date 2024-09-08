# Part 1 A -- Make a Line

#Makes a line of size "size" hashes.
def make_line(size):
    return "#" * size

# print(make_line(7)) # test for above

# Part 1 B -- Make a Square 
# create a function using your make_line function to code a square

# First iteration of Make a Square
# def make_square(size):
#     return (make_line(size) + "\n") * (size-1) + make_line(size)


# Second iteration of make a square
def make_square(size):
    return(make_rectangle(size, size))


# Part 1 C -- Make a Rectangle
def make_rectangle(width, height):
    return ((make_line(width) + "\n") * (height - 1)) + make_line(width)
            

# Part 2 A -- Make a Stairs

def make_downward_stairs(height):
    stairs = ""
    for i in range(height):
        stairs += (make_line(i+1) + "\n") 
    return stairs

# print(make_downward_stairs(5))


# Part 2 B -- Make Space-Line 

def make_space_line(numspaces, numchars):
    return (" " * numspaces) + ("#" * numchars) + (" " * numspaces)



# Part 2 C -- Make Isosceles Triangle

def make_isosceles_triangle(height):
    triangle = ""
    for i in range(height):
        triangle += (make_space_line((height - i - 1), (2*i +1)) + "\n")
    return triangle


# print(make_isosceles_triangle(4))
      

# Part 3 -- Make a Diamond
def make_diamond(height):
   diamond = ""+-7
   triangle = make_isosceles_triangle(height)
   diamond = triangle[:-1]
   for i in range(len(triangle)-1, 0, -1):
      diamond += triangle[i]
   return diamond

print (make_diamond(5))



