#################
## reading
#################
# finger exercise, p 184: Add a method satisfying the specification below to the
# Int_set class.
class Int_set(object):
    """An Int_set is a set of integers"""

    def __init__(self):
        """Create an empty set of integers"""
        self._vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returs True if e is in self, and False otherwise"""
        return e in self._vals

    def remove(self, e):
        """Assues e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + " not found")

    def get_members(self):
        """Returns a list containing the elements of self._
        Nothing can be assumed about the order of the elements"""
        return self._vals[:]

    def __str__(self):
        """Returns a string representation of self"""
        if self._vals == []:
            return "{}"
        self._vals.sort()
        result = ""
        for e in self._vals:
            result = result + str(e) + ","
        return f"{{{result[:-1]}}}"  # why 3? {{ escapes { in f-string
        # so one set for f-string, two to print {} because of f-string

    def union(self, other):
        """other is an Int_set
        mutates self so that it contains exactly the elements in self
        plus the elements in other."""
        self._vals.extend(other._vals)

    # finger exercise, p 186: Replace the union method you added to Int_set by a
    # method that allows cliens of Int_set to use the + operator to denote set union.
    def union_2(self, other):
        """other is an Int_set
        no longer mutates self, but concatenates and returns elements in self
        plus the elements in other."""
        new_set = Int_set()
        new_set._vals = self._vals + other._vals
        return new_set


#################
## lecture
## EXAMPLE: simple Coordinate class
#################
class Coordinate(object):
    """A coordinate made up of an x and y value"""

    def __init__(self, x, y):
        """Sets the x and y values"""
        self.x = x
        self.y = y


# c = Coordinate(3,4)
# a = 0
# origin = Coordinate(a,a)
# print(c.x)
# print(origin.x)


class Coordinate(object):
    """A coordinate made up of an x and y numerical value"""

    def __init__(self, x, y):
        """Sets the x and y values"""
        self.x = x
        self.y = y

    def getX(self):
        """Returns how far away self is on the x axis"""
        return self.x

    def getY(self):
        """Returns how far away self is on the y axis"""
        return self.y

    def distance(self, other):
        """Returns the euclidean distance between two Coordinate objects"""
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5


c = Coordinate(3, 4)
a = 0
origin = Coordinate(a, a)

# these 3 calls returns the same thing
# print(c.distance(origin))
# print(Coordinate.distance(c, origin))
# print(origin.distance(c))


###########################################################
################ AT HOME #####################
###########################################################
# Question 1:
# Write a class definition for a vehicle. A vehicle is defined by attributes:
# Number of wheels
# Number of occupants
# Color
# Decide the type of each data attribute and document this
class Vehicle(object):
    def __init__(self, wheels, occupants, color):
        self.num_wheels: int = wheels
        self.num_occupants: int = occupants
        self.color: str = color


# Question 2:
# Create 2 vehicle instances using the class we wrote previously.
# One red vehicle with 2 wheels, and 1 occupant
# One green vehicle with 18 wheels, and 3 occupants
# Print the first one's number of occupants
# Print the second one's color
bike = Vehicle(2, 1, "red")
truck = Vehicle(18, 3, "green")
print(bike.num_occupants)
print(truck.color)


# Question 3:
# Add on to the code from above for class Vehicle.
# Create another method for the vehicle class named add_n_occupants,
# which takes in an int n. When called, self's number of occupants
# increases by n. It returns the total occupants after the increase.


class Vehicle(object):
    def __init__(self, w, o, c="black"):  # default color for Q5
        self.wheels = w
        self.occ = o
        self.color = c
        self.max_occ = 5

    # add method add_n_occupants here
    def add_n_occupants(self, n):
        if self.occ + n > self.max_occ:
            raise ValueError("exceeds maximum num of occupants")
        else:
            self.occ += n
        return self.occ


v1 = Vehicle(4, 3, "blue")  # from 2 to 3 for Q4
print(v1.occ)  # prints 2
print(v1.add_n_occupants(3))  # prints 5
print(v1.occ)
print(v1.color)

# Question 4:
# Add another data attribute to the Vehicle class, called max_occupancy,
# which is always 5. This attribute is not passed in as a parameter, but
# is defined in the init.
# Modify the add_n_occupants methods such that if adding the occupants
# exceeds the max_occupancy allowed for that vehicle,
#   * you do not perform the increase, and
#   * you raise a ValueError with an apprpriate message

# Question 5:
# Modify the Vehicle class __init__ such that if a vehicle is created
# without specifying a color then the color is set to "black".
# Hint: remember default parameters?

###########################################################
# finger exercises: Write the class according to the specifications below


class Circle:
    def __init__(self, radius):
        """Initializes self with radius"""
        # your code here
        # VAO: my code
        self.radius = radius

    def get_radius(self):
        """Returns the radius of self"""
        # your code here
        # VAO: my code
        return self.radius

    def set_radius(self, radius):
        """radius is a number
        Changes the radius of self to radius"""
        # your code here
        # VAO: my code
        self.radius = radius

    def get_area(self):
        """Returns the area of self using pi = 3.14"""
        # your code here
        # VAO: my code
        return 3.14 * self.radius**2

    def equal(self, c):
        """c is a Circle object
        Returns True if self and c have the same radius value"""
        # your code here
        # VAO: my code
        return self.radius == c.radius

    def bigger(self, c):
        """c is a Circle object
        Returns self or c, the Circle object with the bigger radius"""
        # your code here
        # VAO: my code
        if self.radius > c.radius:
            return self
        elif self.radius < c.radius:
            return c
        else:
            print("circles are of equal size")


###########################################################
################ ANSWERS TO AT HOME ############
###########################################################

# Question 1
# class Vehicle(object):
#     def __init__(self, w, o, c):
#         self.wheels = w
#         self.occ = o
#         self.color= c

# Question 2
# car1 = Vehicle(2, 1, 'red')
# car2 = Vehicle(18, 3, 'green')
# print(car1.occ)
# print(car2.color)

# Question 3
# class Vehicle(object):
#     def __init__(self, w, o, c):
#         self.wheels = w
#         self.occ = o
#         self.color= c
#     # add method add_n_occupants here
#     def add_n_occupants(self, n):
#         self.occ += n
#         return self.occ

# v1 = Vehicle(4,2,'blue')
# print(v1.occ)
# print(v1.add_n_occupants(2))
# print(v1.occ)

# Question 4
# class Vehicle(object):
#     def __init__(self, w, o, c):
#         self.wheels = w
#         self.occ = o
#         self.color= c
#         self.max_occ = 5
#     def add_n_occupants(self, n):
#         new_occ = self.occ + n
#         if new_occ > self.max_occ:
#             raise ValueError("exceeded max occupancy")
#         else:
#             self.occ = new_occ
#             return self.occ

# v1 = Vehicle(4,2,'blue')
# print(v1.occ)
# print(v1.add_n_occupants(2))   # should print 4
# #print(v1.add_n_occupants(2))   # should raise ValueError

# Question 5
# class Vehicle(object):
#     def __init__(self, w, o, c='black'):
#         self.wheels = w
#         self.occ = o
#         self.color= c
#         self.max_occ = 5
#     def add_n_occupants(self, n):
#         new_occ = self.occ + n
#         if new_occ > self.max_occ:
#             raise ValueError("exceeded max occupancy")
#         else:
#             self.occ = new_occ
#             return self.occ

# v1 = Vehicle(4,3,'red')
# print(v1.color)     # prints 'red'
# v2 = Vehicle(2,1)
# print(v2.color)     # prints 'black'
