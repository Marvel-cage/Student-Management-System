print("Saint Isabel Student Management System")
students = []
while True:
    print()
    print("1. Add a new Student")
    print("2. Display Students details")
    print("3. Update Student Details")
    print("4. Delete Student Details")
    print("5. Search Student By ID")
    print("6. Exit")
    menu = input("select your choice: ")
    print()
    if menu == "1":
        while True:
            ID = input("Enter ID: ")
            print()
            if not ID:
                print("Space cannot be empty")
                print()
            else:
                for student in students:
                    if ID == student['ID']:
                        print("ID already exist in our database")
                        print()
                        break
                else:
                    if ID.isdigit():
                        if ID.startswith("000"):
                            if len(ID) == 6:
                                break
                            else:
                                print(f'ID must be 6 digits')
                                print()
                        else:
                            print("ID should start with 000")
                            print()
                    else:
                        if ID.isalnum() or ID.isspace() or ID.isalpha():
                            print("ID must be digit")
                            print()
        while True:
            while True:
                first_name = input("Enter your first name: ").capitalize()
                print()
                if not first_name:
                    print("Space cannot be empty")
                    print()
                else:
                    if first_name.isalpha():
                        if len(first_name) <= 20:
                            break
                        else:
                            print("first name is too long")
                            print()
                    else:
                        print("First name must be only alphabet")
                        print()
            while True:
                sur_name = input("Enter your last name: ").capitalize()
                print()
                if not sur_name:
                    print("Space cannot be empty")
                    print()
                else:
                    if sur_name.isalpha():
                        if len(sur_name) <= 20:
                            break
                        else:
                            print("Last name is too long")
                            print()
                    else:
                        print("Last name must be only alphabet")
                        print()
            while True:
                mid_name = input("Enter your middle name: ").capitalize()
                print()
                if not mid_name:
                    print("Space cannot be empty")
                    print()
                else:
                    if mid_name.isalpha():
                        if len(mid_name) <= 20:
                            break
                        else:
                            print("Middle name is too long")
                            print()
                    else:
                        print("Middle name must be only alphabet")
                        print()
            break
        while True:
            age = (input("Enter age: "))
            print()
            if not age:
                print("Space cannot be empty")
                print()
            else:
                if age.isdigit():
                    if int(age) < 10:
                        print("Age cannot be lesser than 10 years")
                        print()
                    elif int(age) > 18:
                        print("Age cannot be more the 18 years")
                        print()
                    else:
                        break
                else:
                    print("age is in digit")
                    print()
        while True:
            classe = input("Enter class: ")
            print()
            if not classe:
                print("Space cannot be empty")
                print()
            else:
                if classe.isupper():
                    if classe in ("JSS1", "JSS2", "JSS3", "SSS1", "SSS2", "SSS3"):
                        if classe == "JSS1" and 9 < int(age) < 14:
                            break
                        elif classe == "JSS2" and 10 < int(age) < 15:
                            break
                        elif classe == "JSS3" and 11 < int(age) < 16:
                            break
                        elif classe == "SSS1" and 12 < int(age) < 17:
                            break
                        elif classe == "SSS2" and 13 < int(age) < 18:
                            break
                        elif classe == "SSS3" and 14 < int(age) < 19:
                            break
                        else:
                            print(f"{age} years is not right for {classe}")
                            print()
                    else:
                        print("Choose a class from JSS1 - JSS3 , SSS1 - SSS3")
                        print()
                else:
                    print(f"Write in upper case e.g JSS1, SSS3")
                    print()
        while True:
            sex = input(f"Enter sex(M/F): ").upper()
            print()
            if not sex:
                print("Space cannot be empty")
                print()
            else:
                if sex in ("M", "F"):
                    break
                else:
                    print("Enter (M) for males while (F) for female")
                    print()
        while True:
            state = input("Enter State of Origin: ").capitalize()
            print()
            if not state:
                print("Space cannot be empty")
            else:
                if state.isalpha():
                    if len(state) <= 20:
                        break
                    else:
                        print("State is too long")
                        print()
                else:
                    print("State can only be in alphabets")
                    print()
        while True:
            LGA = input("Enter Local Government Area: ").capitalize()
            print()
            if not LGA:
                print("Space cannot be empty")
                print()
            else:
                if LGA.isalpha():
                    if len(LGA) <= 20:
                        break
                    else:
                        print("LGA is too long")
                        print()
                else:
                    print("LGA can only be in alphabets\n i.e No space, punctuation marks, symbol")
                    print()
        while True:
            nationality = input("Enter Nationality: ").capitalize()
            print()
            if not nationality:
                print("Space cannot be empty")
                print()
            else:
                if nationality.isalpha():
                    if len(nationality) <= 20:
                        break
                    else:
                        print("Nationality is too long")
                        print()
                else:
                    print("Nationality can only be in alphabets")
                    print()
        student = {
            "ID": ID,
            "last name": sur_name,
            "first name": first_name,
            "middle name": mid_name,
            "age": age,
            "class": classe,
            "sex": sex,
            "state": state,
            "LGA": LGA,
            "nationality": nationality
        }
        students.append(student)
        print(f"Student information saved successfully")
    elif menu == "2":
        if not students:
            print("No student information found")
        else:
            for student in students:
                print(f"ID:", student['ID'], ", name:", student['last name'], student['middle name'],
                      student['first name'], ", age:", student['age'],
                      ", class:", student['class'], ", sex:", student['sex'],
                      ", state:", student['state'], ", LGA:", student['LGA'], ", nationality:", student['nationality'])
    elif menu == "3":
        std_id = input("Enter the student ID to update: ")
        for student in students:
            if std_id == student['ID']:
                while True:
                    print("Choose from one of this to update")
                    print("1. first name")
                    print("2. last name")
                    print("3. middle name")
                    print("4. age")
                    print("5. class")
                    print("6. sex")
                    print("7. state")
                    print("8. LGA")
                    print("9. Nationality")
                    print("10. Done Updating")
                    change = input("Choose from the above: ")
                    print()
                    if change == "1":
                        while True:
                            newfirstname = input("Enter new first name: ")
                            print()
                            if not newfirstname:
                                print("Space cannot be empty")
                                print()
                            else:
                                if newfirstname.isalpha():
                                    if len(newfirstname) <= 20:
                                        break
                                    else:
                                        print("First name is too long")
                                        print()
                                else:
                                    print("First name must be only alphabet")
                                    print()
                        student['first name'] = newfirstname
                        print("Student first name saved successfully")
                        print()
                    elif change == "2":
                        while True:
                            newlastname = input("Enter new last name: ")
                            print()
                            if not newlastname:
                                print("Space cannot be empty")
                                print()
                            else:
                                if newlastname.isalpha():
                                    if len(newlastname) <= 20:
                                        break
                                    else:
                                        print("Last name is too long")
                                        print()
                                else:
                                    print("Last name must be only alphabet")
                                    print()
                        student['last name'] = newlastname
                        print("Student last name saved successfully")
                        print()
                    elif change == "3":
                        while True:
                            newmidname = input("Enter new middle name: ")
                            print()
                            if not newmidname:
                                print("Space cannot be empty")
                                print()
                            else:
                                if newmidname.isalpha():
                                    if len(newmidname) <= 20:
                                        break
                                    else:
                                        print("Middle name is too long")
                                        print()
                                else:
                                    print("middle name must be only alphabet")
                                    print()
                        student['middle name'] = newmidname
                        print("Student middle name saved successfully")
                        print()
                    elif change == "4":
                        while True:
                            newage = input("Enter new age: ")
                            print()
                            if not newage:
                                print("Space cannot be empty")
                                print()
                            else:
                                if newage.isdigit():
                                    if int(newage) < 10:
                                        print("Age cannot be lesser than 10 years")
                                        print()
                                    elif int(newage) > 18:
                                        print("Age cannot be more the 18 years")
                                        print()
                                    else:
                                        break
                                else:
                                    print("age is in digit")
                                    print()
                        student['age'] = newage
                        print("Student age saved successfully")
                        print()
                    elif change == "5":
                        while True:
                            newclass = input("Enter new class: ")
                            print()
                            if not newclass:
                                print("Space cannot be empty")
                                print()
                            else:
                                if newclass.isupper():
                                    if newclass in ("JSS1", "JSS2", "JSS3", "SSS1", "SSS2", "SSS3"):
                                        if newclass == "JSS1" and 9 < int(student['age']) < 14:
                                            break
                                        elif newclass == "JSS2" and 10 < int(student['age']) < 15:
                                            break
                                        elif newclass == "JSS3" and 11 < int(student['age']) < 16:
                                            break
                                        elif newclass == "SSS1" and 12 < int(student['age']) < 17:
                                            break
                                        elif newclass == "SSS2" and 13 < int(student['age']) < 18:
                                            break
                                        elif newclass == "SSS3" and 14 < int(student['age']) < 19:
                                            break
                                        else:
                                            print(f"{student['age']} years is not right for {newclass}")
                                            print()
                                    else:
                                        print("Choose a class from JSS1 - JSS3 , SSS1 - SSS3")
                                        print()
                                else:
                                    print(f"Write in upper case e.g JSS1, SSS3")
                                    print()
                        student['class'] = newclass
                        print("Student class saved successfully")
                        print()
                    elif change == "6":
                        while True:
                            newsex = input("Enter new sex: ")
                            print()
                            if not newsex:
                                print("Space cannot be empty")
                                print()
                            else:
                                if newsex in ("M", "F"):
                                    break
                                else:
                                    print("Enter (M) for males while (F) for female")
                                    print()
                        student['sex'] = newsex
                        print("Student sex saved successfully")
                        print()
                    elif change == "7":
                        while True:
                            newstate = input("Enter new state: ")
                            print()
                            if not newstate:
                                print("Space cannot be empty")
                            else:
                                if newstate.isalpha():
                                    if len(newstate) <= 16:
                                        break
                                    else:
                                        print("State is too long")
                                        print()
                                else:
                                    print("State can only be in alphabets")
                                    print()
                        student['state'] = newstate
                        print("Student state saved successfully")
                        print()
                    elif change == "8":
                        while True:
                            newLGA = input("Enter new LGA: ")
                            print()
                            if not newLGA:
                                print("Space cannot be empty")
                            else:
                                if newLGA.isalpha():
                                    if len(newLGA) <= 20:
                                        break
                                    else:
                                        print("LGA is too long")
                                        print()
                                else:
                                    print("LGA can only be in alphabets")
                                    print()
                        student['LGA'] = newLGA
                        print("Student LGA saved successfully")
                        print()
                    elif change == "9":
                        while True:
                            newnationality = input("Enter new Nationality: ")
                            print()
                            if not newnationality:
                                print("Space cannot be empty")
                            else:
                                if newnationality.isalpha():
                                    if len(newnationality) <= 20:
                                        break
                                    else:
                                        print("Nationality is too long")
                                        print()
                                else:
                                    print("Nationality can only be in alphabets")
                                    print()
                        student['nationality'] = newnationality
                        print("Student Nationality saved successfully")
                        print()
                    elif change == "10":
                        print("Student information saved successfully")
                        print()
                        break
                    else:
                        print("choose from 1 to 10")
                break
        else:
            print(f"No Student ID like {std_id} found")
    elif menu == "4":
        delete_id = input("Enter the ID of the student to be deleted: ")
        for student in students:
            if delete_id == student['ID']:
                confirm = input("Are you sure you want to delete this(yes/no): ").lower()
                print()
                while True:
                    if confirm == "yes":
                        students.remove(student)
                        print("Student information safely deleted")
                        print()
                        break
                    elif confirm == "no":
                        print("Confirmed")
                        print()
                        break
                    else:
                        print("Enter either yes or no")
                        print()
            break
        else:
            print("No such ID like this exist in our database")
            print()
    elif menu == "5":
        id_search = input("Enter the ID: ")
        for student in students:
            if id_search == student['ID']:
                print("ID:", student['ID'], "name:", student['last name'], student['middle name'], student['first name'], "age:", student['age'], "class:", student['class'], "sex:", student['sex'], "state:", student['state'], "LGA:", student['LGA'], "nationality:", student['nationality'])
                break
        else:
            print(f"No Student ID like {id_search} found")
            print()
    elif menu == "6":
        print("Thank you")
        break
    else:
        print("Enter from 1 to 6")
