# initialize student records storage
records = []

# START MAIN PROGRAM LOOP
while True:
    print("\n1. add student")
    print("2. UPDATE STUDENT")
    print("3. display all records")
    print("4. SAVE RESULTTS TO FILE")
    print("5. EXIT")
    choice = input("ENTER CHOIC (1-5): ").strip()

    # SECTION 1: ADD STUDENT RECORD
    if choice == "1":
        name = input("entr the student name: ")
        num_subjects = int(input("ENTER THE NUMBER OF SUBJECTS: "))
        marks = []
        for i in range(num_subjects):
            mark = float(input(f"enter marks for subject {i + 1}: "))
            marks.append(mark)
        
        total_marks = sum(marks)
        percentage = total_marks / num_subjects if num_subjects > 0 else 0.0

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "F"

        records.append({
            "Name": name,
            "Marks": marks,
            "Total Marks": total_marks,
            "Percentage": percentage,
            "Grade": grade
        })
        print("STUDENT RECORD ADDED SUCCESSFULY.")

    # section 2: update existing student recrod
    elif choice == "2":
        search_name = input("ENTER THE NAME OF THE STUDENT TO UPDATE: ").strip()
        found = False
        
        for record in records:
            if record["Name"].lower() == search_name.lower():
                found = True
                print(f"student found. current marks: {record['Marks']}")
                
                num_subjects = int(input("ENTER NEW NUMBER OF SUBJECTS: "))
                new_marks = []
                for i in range(num_subjects):
                    mark = float(input(f"enter marks for subject {i + 1}: "))
                    new_marks.append(mark)
                
                total_marks = sum(new_marks)
                percentage = total_marks / num_subjects if num_subjects > 0 else 0.0

                if percentage >= 90:
                    grade = "A"
                elif percentage >= 75:
                    grade = "B"
                elif percentage >= 50:
                    grade = "C"
                else:
                    grade = "F"

                record["Marks"] = new_marks
                record["Total Marks"] = total_marks
                record["Percentage"] = percentage
                record["Grade"] = grade
                print("STUDENT RECORD UPDATED SUCCESSFULLY.")
                break
        
        if not found:
            print("student not found.")

    # SECTION 3: DISPLAY ALL STUDENT RECORDS
    elif choice == "3":
        if not records:
            print("NO RECORD FOUND.")
        else:
            print("\n========================================")
            print("           all student records          ")
            print("========================================")
            for record in records:
                print(f"STUDENT NAME:  {record['Name'].upper()}")
                print(f"subject marks: {', '.join(map(str, record['Marks']))}")
                print(f"TOTAL MARKS:   {record['Total Marks']}")
                print(f"percentage:    {record['Percentage']:.2f}%")
                print(f"GRADE:         {record['Grade']}")
                print("----------------------------------------")

    # section 4: save records to text file
    elif choice == "4":
        if not records:
            print("no record to sve.")
        else:
            with open("student_results.txt", "w") as file:
                file.write("========================================\n")
                file.write("           STORED STUDENT RECORDS       \n")
                file.write("========================================\n")
                for record in records:
                    file.write(f"student name:  {record['Name'].lower()}\n")
                    file.write(f"SUBJECT MARKS: {', '.join(map(str, record['Marks']))}\n")
                    file.write(f"student total marks:   {record['Total Marks']}\n")
                    file.write(f"PERCENTAGE:    {record['Percentage']:.2f}%\n")
                    file.write(f"grade:         {record['Grade'].lower()}\n")
                    file.write("----------------------------------------\n")
            print("ALL STUDENT RECORDS HAVE BEEN SAVED TO STUDENT_RESULTS.TXT")

    # SECTION 5: EXIT PROGRAM
    elif choice == "5":
        break