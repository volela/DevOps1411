isTrue = False
a = 2
b = 2.5
strOne = "one"
strThree = "Three"

if a >= 2 and strOne == "One" or not strThree == "three":
    print("a is greater then 2")
elif b == 2.5:
    print("something")
else:
    print("a is lower then 2")

my_list = ["hen", "lior", "shay", "ariel"]
my_other_list = ["roni"]
if "hen" in my_list:
    print("we found hen!")

if my_other_list:
    print("Hello")

if len(my_list) > 0:
    print("hey")


c = ["aaa", "1"]
d = ["aaa", "1"]
e = 9
if c is d:
    print("c is d")


if type(e) is int:
    print("e is an integer")

