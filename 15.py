what_to_print = "hello word!"
list_of_names = ["hen", "michael", "noam", "lior", "amichai"]

for i in range(len(list_of_names)):
    print(list_of_names)

for name in list_of_names:
    print(name)

for name in list_of_names:
    if name == "hen":
        continue
    print(name)

#a = 0
#while a < 10:
#    print(a)
#    a = a + 1

for i in range(1, 101):
    if i % 7 == 0 or "7" in str(i):
        continue
    print(i)

a = "a"
while a != "q":
    a = input("enter q or not: ")
else:
    print("finished successfully")






