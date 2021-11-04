import pickle


def insertRec():
    record = []
    while True:
        f = open("student.dat", "wb")
        name = input("Enter name of student:")
        class1 = input("Enter student class:")
        Rollno = int(input("Enter the student's Roll no:"))
        data = [name, class1, Rollno]
        record.append(data)
        choice = input("Wish to enter more data (Y/N)?:")
        pickle.dump(record, f)
        if choice.upper() == 'N':
            print("Record Added")
            break
        f.close()


def readRec():
    f = open("student.dat", "rb")
    record = pickle.load(f)
    print("Contents of student file are:")
    for i in record:
        name = i[0]
        class1 = i[1]
        Rollno = i[2]
        print(name, class1, Rollno)
    f.close()


def searchRollNo():
    t = 0
    f = open("student.dat", "rb")
    record = pickle.load(f)
    for i in record:
        name = i[0]
        class1 = i[1]
        Rollno = i[2]
    r = int(input("Enter Student Roll number to be searched:"))
    for i in record:
        if i[2] == r:
            print("Search Complete")
            print("Details:")
            print(i[0], i[1], i[2])
            t = 1
            break
        if t != 1:
            print("Record Not Found")
    f.close()


def updateMarks():
    f = open("student.dat", "rb+")
    record = pickle.load(f)
    found = 0
    rollno = int(input("Enter the roll number to search:"))
    for R in record:
        rno = R[2]
        if rno == rollno:
            print("Current name is:", R[0])
            R[0] = input("New Name:")
            found = 1
            break
    if found == 1:
        f.seek(0)
        pickle.dump(record, f)
        print("Name Updated!!!")
    f.close()


def deleteRec():
    f = open("student.dat", "rb")
    record = pickle.load(f)
    for i in record:
        name = i[0]
        class1 = i[1]
        Rollno = i[2]
    f.close()
    r = int(input("Enter Student Roll number to be deleted:"))
    f = open("student.dat", 'wb+')
    z = []
    for x in record:
        if x[2] == r:
            print("Record Deleted")
            continue
        z.append(x)
    pickle.dump(z, f)
    f.close()


print('Type 1 to insert rec. ')
print('Type 2 to display rec. ')
print('Type 3 to search rec. ')
print('Type 4 to update rec. ')
print('Type 5 to delete rec. ')
print('Enter your choice 0 to exit ')


while True:
    choice = int(input("Enter your choice: "))
    if choice == 0:
        break
    elif choice == 1:
        insertRec()
    elif choice == 2:
        readRec()
    elif choice == 3:
        searchRollNo()
    elif choice == 4:
        updateMarks()
    elif choice == 5:
        deleteRec()
