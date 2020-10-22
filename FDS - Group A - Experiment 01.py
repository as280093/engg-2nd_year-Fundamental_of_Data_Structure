m = int(input("Enter the Class Strength: "))
list1 = []      #for Storing Cricket Players RollNo.list2 = []      #for Storing Badminton Players RollNo.list3 = []      #for Storing Football Players RollNo.
# INFINITE WHILE LOOP TO KEEP ASKING USER FOR APPROPRIATE NUMBER LESS THEN CLASS STRENGTHwhile True:
    c = int(input("Enter the count for cricket players: "))
    if c > m:
        print("Number is greater then Class Strength, Enter Again")
    else:
        break# GETTING ALL ROLL NUMBERS FOR CRICKET PLAYERSfor i in range(c):
    x = int(input("Enter the roll no of a student who plays cricket: "))
    list1.append(x)


# INFINITE WHILE LOOP TO KEEP ASKING USER FOR APPROPRIATE NUMBER LESS THEN CLASS STRENGTHwhile True:
    b = int(input("Enter the count of badminton players: "))
    if b > m:
        print("Number is greater then Class Strength, Enter Again")
    else:
        break# GETTING ALL ROLL NUMBERS FOR CRICKET PLAYERSfor i in range(b):
    y = int(input("Enter the roll no of a student who plays Badminton: "))
    list2.append(y)

# INFINITE WHILE LOOP TO KEEP ASKING USER FOR APPROPRIATE NUMBER LESS THEN CLASS STRENGTHwhile True:
    f = int(input("Enter the count of football players: "))
    if f > m:
        print("Number is greater then Class Strength, Enter Again")
    else:
        break
for i in range(f):
    z = int(input("Enter the roll no of a student who plays Football: "))
    list3.append(z)

def menu():
   print("\n ######### MAIN MENU #########")
   print("1.Students who play both Cricket & Badminton")
   print("2.Students who play either cricket or badminton but not both")
   print("3.Number of student who player neither cricket nor Badminton")
   print("4.Student who player cricket or football nor Badminton")
   print("5. Exit")
   selection = int(input("\nEnter Choice: "))
   if selection == 1:
       cricketbadminton(list1,list2)
       menu()
   elif selection == 2:
       eitercricketbadminton(list1,list2)
       menu()
   elif selection == 3:
       neithercnorb(list1,list2)
       menu()
   elif selection == 4:
       cricketfootball(list1,list2,list3)
       menu()
   elif selection == 5:
       exit()
   else:
       print("Enter a Valid Selection")
   menu()

#       a)  List of students who play both cricket and badmintondef cricketbadminton(l1,l2):
    temp = []
    for a in l1:
        for bb in l2:
            if a==bb:
                temp.append(a)
    if len(temp) != 0:
        print("Roll no of Students who play both Cricket & Badminton are: " + str(temp))
    else:
        print("no Student plays both Cricket & badminton")

#       b)  List of students who play either cricket or badminton but not bothdef eitercricketbadminton(l1,l2):
    temp = []
    for j in l1:
        if j not in l2:
            temp.append(j)
    for j in l2:
        if j not in l1:
            temp.append(j)

    if len(temp) != 0  :
        print("Roll no of Students who play Either Cricket or Badminton but not both are: "+ str(temp))
    else:
        print("No Student plays Either Cricket or Badminton")

#       c)  Number of students who player neither cricket nor badmintondef neithercnorb(l1,l2):
    unioncb = l1 + [ii for ii in l2 if ii not in l1]
    res = [jj for jj in range(1,m + 1) if jj not in unioncb]
    print("Number of student who player neither cricket nor Badminton is: "+ str(len(res))+", Which are: " +str(res))

#       d)  Number of students who play cricket and football not badminton.def cricketfootball(l1,l2,l3):
    tempstore = []
    unioncf = l1 + [ii for ii in l3 if ii not in l1]
    for element in unioncf:
        if element not in l2:
            tempstore.append(element)
    print("Number of students who play cricket and football not badminton is: "+ str(len(tempstore))+", Which are: " +str(tempstore))

#main instancemenu()
