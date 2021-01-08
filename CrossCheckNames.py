import csv

# Load .csv to List
list1 = []
with open('attended.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        list1.append(row[0])

list2 = []
with open('registered.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        list2.append(row[0])

list1convert = [x.upper() for x in list1]
list2convert = [x.upper() for x in list2]
list2_nospace = " ".join(list2convert)
print(list1convert)
print(list2convert)

i = 0
print("\nNot in list: \n")

while i < len(list1convert):

    if list1convert[i] not in list2_nospace:
        print(list1convert[i])
    i += 1

print("\nDone cross-check.")
# attended name not in registered, means x register but somehow attended.
