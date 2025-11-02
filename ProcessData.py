#ProcessData.py
#Name:
#Date:
#Assignment:

def main():

    inFile = open("names.dat", 'r')
    outFile = open("StudentList.csv", 'w')


    header = inFile.readline()


    for line in inFile:

        parts = line.strip().split('\t')


        if len(parts) < 7:
            continue

        # Extract data fields
        first_name = parts[0]
        last_name = parts[1]
        student_id = parts[3]
        year = parts[5]
        major = parts[6]


        user_id = first_name[0].lower() + last_name.lower()
        if len(last_name) < 5:
            user_id += 'X'
        user_id += student_id[-3:]

        major_code = major[:3].upper()


        year_map = {
            "Freshman": "FR",
            "Sophomore": "SO",
            "Junior": "JR",
            "Senior": "SR"
        }

        year_code = year_map.get(year, year[:2].upper())
        major_year = major_code + "-" + year_code


        outFile.write(f"{last_name},{first_name},{user_id},{major_year}\n")


    inFile.close()
    outFile.close()

    print("✅ StudentList.csv created successfully!")

if __name__ == '__main__':
    main()

