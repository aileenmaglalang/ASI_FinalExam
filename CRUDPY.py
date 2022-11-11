import mysql.connector

db = mysql.connector.connect(
  host='localhost', database='student_record', username='root', password=''
)

cursor = db.cursor()

def create():
  id = int(input("Enter student ID: "))
  fname = input("Enter student first name: ")
  lname = input("Enter student last name: ")
  sec = input("Enter student section: ")

  insert = "INSERT INTO student (STUDENT_ID, FIRST_NAME, LAST_NAME, SECTION) VALUES (%s,%s,%s,%s)"
  val = (id, fname, lname, sec)
  cursor.execute(insert, val)
  db.commit()

  print("{} records inserted.".format(cursor.rowcount))

def read():
  query = '''SELECT * FROM student'''
  cursor.execute(query)
  try:
    records = cursor.fetchall()
    i = 0
    if len(records) == 0:
      raise ValueError
    else:
      print("STUDENT RECORDS")
      print("---------------")
      for r in records:
        i = i+1
        print("Student #",i)
        print("ID:", r[0])
        print("Name:", r[1],r[2])
        print("Section:",r[3])
        print("---------------")
  except:
    print("No data present in the database!")

def update():
    eid = int(input("Enter student ID: "))
    select = '''SELECT * FROM student'''
    cursor.execute(select)
    records = cursor.fetchall()
    x = 0
    for r in records:
      if r[0] != eid:
        x = x + 1
        if x == 0:
          print("STUDENT ID DOES NOT EXIST!")
          raise ValueError 

    print("What do you need to update?")
    print("[A] FISRT NAME")
    print("[B] LAST NAME")
    print("[C] SECTION")
    print("[D] ALL OF THE ABOVE")
    option = input("Option: ")
    if option.upper() == "A":
      query = '''UPDATE student SET FIRST_NAME = %s WHERE STUDENT_ID = %s'''
      fname = input("Enter first name: ")
      cursor.execute(query, (fname,eid))
      db.commit()

    elif option.upper() == "B":
      query = '''UPDATE student SET LAST_NAME = %s WHERE STUDENT_ID = %s'''
      lname = input("Enter last name: ")
      cursor.execute(query, (lname,eid))
      db.commit()

    elif option.upper() == "C":
      query = '''UPDATE student SET SECTION = %s WHERE STUDENT_ID = %s'''
      sec = input("Enter section: ")
      cursor.execute(query, (sec,eid))
      db.commit()

    elif option.upper() == "D":
      query = '''UPDATE student SET FIRST_NAME, LAST_NAME, SECTION = %s WHERE STUDENT_ID = %s'''
      fname = input("Enter first name: ")
      lname = input("Enter last name: ")
      sec = input("Enter section: ")
      cursor.execute(query, (fname,lname,sec,eid))
      db.commit()

    else:
      print("OPTION DOESN'T EXIST!")

def delete():
  eid = int(input("Enter student ID: "))
  select = '''SELECT * FROM student'''
  cursor.execute(select)
  records = cursor.fetchall()
  x = 0
  for r in records:
    if r[0] != eid:
      x = x + 1
    else:
      x = 0
      break
  if x != 0:
    print("STUDENT ID DOES NOT EXIST!")
    raise ValueError
  
  query = '''DELETE FROM student WHERE STUDENT_ID = %s'''
  cursor.execute(query, [eid])
  db.commit()
  print("Student ID# {} is deleted from the record!".format(eid))

while True:
  print(""""
  Select an option:
  [1] Create a record
  [2] Update a record
  [3] Display a recod
  [4] Delete a record
  [0] Exit Program
  """)
  opt = int(input("Enter option: "))

  if opt == 1:
      print("Create or add record in the table")
      create()     

  elif opt == 2:
    print("Update a record in the table")
    update()

  elif opt == 3:
    read()

  elif opt == 4:
    print("Delete a record in the table")
    delete()
    
  elif opt == 0:
        while True:
            yes_no = input("Are you sure you want to quit? Y/N: ")
            if yes_no == "y" or yes_no == "Y":
                exit()
            elif yes_no == "n" or yes_no == "N":
                break
            else:
                print("Invalid answer! Only Y/N is accepted")

  else:
    print("OPTION DOES NOT EXIST!")
