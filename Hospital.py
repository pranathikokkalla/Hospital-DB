import subprocess as sp
from typing import Counter
import pymysql
import pymysql.cursors


def View_Table(rows):
 a = []
 a.append(list(rows[0].keys()))
    
 for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
 print(tabulate(a, tablefmt="psql", headers="firstrow"))




def Ins_new_Doctor():
    global cur
    row = {}
    print("Enter the new doctor's details: ") 

    row["Fees"] = int(input("Doctor Fee: "))
    row["Starting Hour"] = input("Working Hours of Doctor(start time): ")
    row["Ending Hour"] = input("Working Hours of Doctor(finish time): ")
    row["Staff Id"] = int(input("Staff Id of the doctor: "))
    try:
        query = "INSERT INTO Doctor VALUES('%d', '%s', '%s', '%d')" % (row["Fees"],row["Starting Hour"], row["Ending Hour"], row["Staff Id"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    return

def Ins_new_Nurse():
    global cur
    row = {}
    print("Enter the new Nurse's details: ") 

    row["Staff Id"] = int(input("Staff Id of the nurse: "))
    row["Nurse Id"] = int(input("Staff Id of the supervisor nurse: "))
    row["No. of days per month"] = int(input("No. of working days per month: "))
    try:
        query = "INSERT INTO `Nurse` VALUES('%d', '%d','%d')" % (row["Staff Id"],row["Nurse Id"],row["No. of days per month"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return    
    return

def Ins_new_Staff():
    global cur
    row = {}
    print("Enter the new Staff's details: ")

    row["Staff Id"] = int(input("Staff Id: "))
    row["First_Name"] = input("First Name: ")
    row["Middle_Name"] = input("Middle Name: ")
    row["Last_Name"] = input("Last Name: ")
    row["Dept_Id"] = int(input("Department Id: "))
    row["Date"] = int(input("Birth date: "))
    row["Month"] = int(input("Birth month: "))
    row["Year"] = int(input("Birth year: "))
    row["Salary"] = int(input("Salary: "))
    row["Gender"] = input("Gender: ")
    row["H.no"] = input("House no: ")
    row["Pin_Code"] = int(input("Pin code: "))
    row["Street.no"] = int(input("Street no: "))
    row["City"] = input("City: ")
    row["State"] = input("State: ")
    try:
        query = "INSERT INTO Staff VALUES('%d', '%d', '%d', '%d', '%d', '%d', '%s', '%d', '%d','%s','%s','%s','%s','%s','%s')" % (
            row["Staff Id"],row["Dept_Id"], row["Date"], row["Month"],row["Year"],row["Salary"],row["H.no"],row["Pin_Code"],
            row["Street.no"],row["City"],row["State"],row["Gender"], row["First_Name"], row["Middle_Name"], row["Last_Name"]
            )
        cur.execute(query)
        con.commit()
    except Exception as e:
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    
    i=int(input("Is the staff a Doctor or a Nurse?: (choose 1 if Doctor (or) choose 2 if Nurse): "))
    if(i==1):
        Ins_new_Doctor()
    if(i==2):
        Ins_new_Nurse()    
    return  



    
# def Aggre_1():
#     i = input("Enter the month whose avg bill cost u want to find: ")
#     try:
#      global cur
#      query2= """INSERT INTO Charge (bill,`Patient Id`,`Bill number`)
#     SELECT `Doctor Cost`+`Room Cost` AS bill, `Patient Id`, `Bill number`
#     FROM Billing WHERE NOT EXISTS (SELECT * FROM Charge) ;"""
#      cur.execute(query2)
#      con.commit()
#      query3="""SELECT AVG(bill) FROM Charge,Billing WHERE `Date of Bill` LIKE '' AND Charge.`Bill number`=Billing.`Bill number`""" %(i)
#      cur.execute(query3)
#      con.commit()
#      x= cur.fetchall()
#      View_Table(x)
#      con.commit()
#      query5="DELETE FROM Charge;"
#      cur.execute(query5)
#      con.commit()
#     except Exception as e:
#         print(e)
#     return
def Aggre_2():
    try:
        global cur
        query="""SELECT NEW.`Dept_Id` , NEW.try AS No_of_ppl
FROM Staff, (SELECT COUNT(`Dept_Id`) AS try,`Dept_Id` FROM Staff GROUP BY `Dept_Id` ) AS NEW
ORDER BY NEW.try DESC
LIMIT 1;"""
        cur.execute(query)
        x= cur.fetchall()
        View_Table(x)
        con.commit()
    except Exception as e:
        print(e)
    return
def Selec_1():
    try:
     global cur
     query="SELECT * FROM Inpatient"
     cur.execute(query)
     x= cur.fetchall()
     View_Table(x)
     con.commit()
    except Exception as e:
        print(e)
    return
def Selec_2():
    try:
     global cur
     query="SELECT * FROM Outpatient"
     cur.execute(query)
     x= cur.fetchall()
     View_Table(x)
     con.commit()
    except Exception as e:
        print(e)
    return

def Proj_1():
    inp=int(input("\n Value:"))   
    try:
        global cur
        query=""" SELECT
  Inpatient.`First name`,
  Inpatient.`Middle name`,
  Inpatient.`Last name`
FROM
  (
    SELECT
      *
    FROM
      Billing
    WHERE
      (`Room Cost` + `Doctor Cost`) > %d
  ) AS TABLE1,
  Inpatient
WHERE
  TABLE1.`Patient Id` = Inpatient.`Patient Id`;""" %(inp)
        cur.execute(query)
        x= cur.fetchall()
        View_Table(x)
        con.commit()
    except Exception as e:
        return

    
def Proj_2():
      inp=int(input("\n Value:")) 
      try:
        global cur
        query="""SELECT First_Name,Middle_Name,Last_Name FROM  Staff where Staff.Salary > %d;""" %(inp)
        cur.execute(query)
        x= cur.fetchall()
        View_Table(x)
        con.commit()
      except Exception as e:
        return
       
def Search_1(): ############################################# need to change ##############################################
   # inp=input("\n Value:")
    try:
     global cur
     query="SELECT First_Name,Middle_Name,Last_Name FROM Staff AS S , Doctor AS D WHERE D.`Staff Id`= S.`Staff Id` AND First_Name Like 'A%';" 
     cur.execute(query)
     x= cur.fetchall()
     View_Table(x)
     con.commit()
    except Exception as e:
        print(e)
    return

def Search_2():
    try:
     global cur
     query="SELECT `Bill Number` FROM Billing  WHERE `Bill Number`  Like '%1'"
     cur.execute(query)
     x= cur.fetchall()
     View_Table(x)
     con.commit()
    except Exception as e:
        print(e)
    return

def Analysis_1():
    try:
     global cur
    
     query2= """INSERT INTO Charge (bill,`Patient Id`,`Bill number`)
    SELECT `Doctor Cost`+`Room Cost` AS bill, `Patient Id`, `Bill Number`
    FROM Billing WHERE NOT EXISTS (SELECT * FROM Charge);"""
     cur.execute(query2)
     con.commit()
     query3="""SELECT AVG(bill) FROM Charge
    INTO @X;"""
     cur.execute(query3)
     con.commit()
     query4="""SELECT
  Inpatient.`First name`,
  Inpatient.`Middle name`,
  Inpatient.`Last name`
FROM
  Charge,
  Billing,Inpatient
WHERE
  Billing.`Patient Id` = Charge.`Patient Id` AND
  Charge.`Patient Id` = Inpatient.`Patient Id` AND Inpatient.`Last name` Like 'K%'
  AND bill > @X ;
 """  
     cur.execute(query4)
     x= cur.fetchall()
     View_Table(x)
     con.commit()
    # print("wnfnkje")
     query5="DELETE FROM Charge;"
     cur.execute(query5)
     con.commit()
    # print("wnfnkje2")
   
    except Exception as e:
        print(e)
    return
    
# def Analysis_2():
#     try:
#      global cur
#      query="""SELECT AVG(Salary) FROM Staff INTO @A;"""
#      cur.execute(query)
#      con.commit()
#      query2="""SELECT First_Name,Last_Name,Middle_Name 
# FROM Staff  
# WHERE Salary > @A AND `Staff Id` like '%3';"""
#      cur.execute(query2)
#      con.commit()
#      x= cur.fetchall()
#      View_Table(x)
#      con.commit()
#     except Exception as e:
#         print(e)
#     return


def Aggre():
    print("CHOOSE AN OPTION:(print the corresponding number)\n")
    # print("1.Avg bill cost for month")
    print("1.Dept with max staff")
    inp = input("\nCHOICE ? ")
    if(inp == '1'):
      Aggre_2()
    # elif(inp == '2'):
    #   Aggre_2()
    return

def Selec():
    inp=input("\nEnter the name of the table which you want to select: ")
    try:
     global cur
     query="SELECT * FROM %s;" %(inp)
     cur.execute(query)
     x= cur.fetchall()
     View_Table(x)
     con.commit()
    except Exception as e:
        print(e)
    return

def Proj():
    print("CHOOSE AN OPTION:(print the corresponding number)\n")
    print("1.Inpatients with bill greater than the value entered")
    print("2.Staff whose salary is greater than the value entered")
    inp = input("\nCHOICE ? ")
    if(inp == '1'):
      Proj_1()
    elif(inp == '2'):
      Proj_2()
    return

def Search():
    print("CHOOSE AN OPTION:(print the corresponding number)\n")
    print("1.Doctors whose name starts with the letter ‘A’")
    print("2. Bill numbers ending with 1")
    inp = input("\nCHOICE ? ")
    if(inp == '1'):
      Search_1()
    elif(inp == '2'):
      Search_2()
    return

def Analysis():
    print("CHOOSE AN OPTION:(print the corresponding number)\n")
    print("1.Inpatients whose last name starts with the ‘K’ whose bill is greater than the average bill cost.")
    #print("2. Name of the staff with staff id ending with 3 who made more than the average salary")
    inp = input("\nCHOICE ? ")
    if(inp == '1'):
      Analysis_1()
    # elif(inp == '2'):
    #   Analysis_2()
    return
    
def Del_Staff():
    id=int(input("Enter the Staff Id of the saff that has resigned: "))
    try:
            query1="""INSERT INTO Doctor_1 (`Staff_Id`)
            SELECT `Staff Id`
            FROM Doctor
            WHERE `Staff Id`=%d;""" % (id)
            cur.execute(query1)
            con.commit()

            query2="""INSERT INTO Nurse_New (`Staff_Id`)
            SELECT `Staff Id`
            FROM Nurse
            WHERE `Staff Id`=%d;""" % (id)
            cur.execute(query2)
            con.commit()

            id1=int(input("Staff id of the staff to re-assign these patients: "))
            
            query3="""UPDATE Treatment SET `Staff Id` = %d WHERE EXISTS
            (SELECT `Staff Id` FROM Doctor_1) AND `Staff Id`=%d;""" % (id1,id)        # Assigning the patients of that staff to another staff
            cur.execute(query3)
            con.commit()
            
            query4="""UPDATE Treatment SET `Staff Id` = %d WHERE EXISTS
            (SELECT `Staff Id` FROM Nurse_New) AND `Staff Id`=%d;""" % (id1,id)
            cur.execute(query4)
            con.commit()

            query5="DELETE FROM Staff where `Staff Id`=%d;" % (id)
            cur.execute(query5)
            con.commit()

            query6="DELETE FROM Doctor_1;"
            cur.execute(query6)
            con.commit()

            query7="DELETE FROM Nurse_New;"
            cur.execute(query7)
            con.commit()

    except Exception as e:
        print(e)



def Upd_Sal():

     
        id = int(input("Enter the Staff Id for the Staff whose salary you want to update : "))
        try:
            salary = int(input("Enter the new salary: "))
       

            query = "UPDATE Staff SET Salary = %d WHERE `Staff Id` = %d;" % (
            salary, id)
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)

   
        return

def Upd_room():

        id1 = int(input("Enter the Floor number of the room whose cost needs to be updated : "))
        id2 = int(input("Enter the Room number of the room whose cost needs to be updated : "))
        try:
            cost = int(input("Enter the new cost: "))
    
            query = "UPDATE Room SET `Cost per day` = %d WHERE `Room No` = %d AND `Floor No`=%d;" % (
            cost, id2,id1)
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)

   
        return


def Ins_new_Patient():
    global cur
    row = {}
    row1 = {}
    row2={}
    print("Enter the new Patients's details: ")

    row["Patient Id"] = int(input("Patient Id: "))
    row["Date"] = int(input("Birth Date: "))
    row["Month"] = int(input("Birth Month: "))
    row["Year"] = int(input("Birth Year: "))
    row["Gender"] = input("Gender: ")
    row["Height"] = int(input("Heigth: "))
    row["Weight"] = int(input("Weight: "))

    try:
        query = "INSERT INTO `Patient Info` VALUES('%d', '%d', '%d', '%d', '%s', '%d', '%d')" % (
            row["Patient Id"],row["Date"], row["Month"],row["Year"],row["Gender"],row["Height"],row["Weight"] 
            )
        cur.execute(query)
        con.commit()
    except Exception as e:
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    
    i=int(input("Is the Patient getting admitted ? (if Yes choose 1, else choose 2): "))
    if(i==1):
        print("Enter the new InPatients's details: ")
        row1["First name"] = input("Fist Name: ")
        row1["Middle name"] = input("Middle Name: ")
        row1["Last name"] = input("Last Name: ")
        row1["H.no"] = input("H.no: ")
        row1["Pin_code"] = int(input("Pin Code: "))
        row1["Street no."] = int(input("Street No: "))
        row1["City"] = input("City: ")
        row1["State"] = input("State: ")
        row1["Date of admission"] = input("Date of Admission: ")
        row1["Date of discharge"] = input("Date of Discharge: ")
        row1["Staff Id"] = int(input("Id of the Doctor who treats the patient: "))
        
        row1["Room No"] = int(input("Room No: "))
        row1["Floor No"] = int(input("Floor No: "))
        row1["Bill number"] = int(input("Bill number: "))
        row1["Room_cost"] = int(input("Room Cost: "))
        row1["doc_cost"] = int(input("Doctor Cost: "))

        try:

           query = "INSERT INTO `Inpatient` VALUES('%d','%s', '%s', '%s','%s','%d','%d','%s','%s','%s','%s')" % (
             row["Patient Id"],row1["First name"],row1["Middle name"], row1["Last name"],row1["H.no"],row1["Pin_code"],row1["Street no."],row1["City"],
             row1["State"],row1["Date of admission"],row1["Date of discharge"]
            )
           cur.execute(query)
           con.commit()

        except Exception as e:
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return

        try:

            query = "INSERT INTO `Billing` VALUES('%d','%d','%d','%d','%s')" % (
             row1["Bill number"],row["Patient Id"],row1["Room_cost"],row1["doc_cost"],row1["Date of discharge"]
            )
            cur.execute(query)
            con.commit()
        except Exception as e:
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
        row1["Staff Id"] = int(input("Id of the Nurse who treats the patient: "))
        try:
           query = "INSERT INTO `Hospital Stay` VALUES('%d','%d', '%d', '%d','%d')" % (
             row1["Bill number"],row["Patient Id"],row1["Staff Id"], row1["Room No"],row1["Floor No"]
            )
           cur.execute(query)
           con.commit()
        except Exception as e:
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
        try:
            query= """UPDATE Room SET Status = 1;"""
            cur.execute(query)
            con.commit()
        except Exception as e:
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return

    if(i==2):
        print("Enter the new OutPatients's details: ")

    
        row2["First name"] = input("First Name: ")
        row2["Middle name"] = input("Middle Name: ")
        row2["Last name"] = input("Last Name: ")
        row2["H.no"] = input("H.no: ")
        row2["Pin_code"] = int(input("Pin Code: "))
        row2["Street no."] = int(input("Street no.: "))
        row2["City"] = input("City : ")
        row2["State"] = input("State: ")
        row2["Staff Id1"] = int(input("Id of the Doctor who treats the patient: "))
        row2["Staff Id2"] = int(input("Id of the Nurse who treats the patient: "))
        row2["Bill number"] = int(input("Bill number: "))
        row2["doc_cost"] = int(input("Doctor Cost: "))
        row2["Date"] = input("Date of Appointment: ")
        try:
           query = "INSERT INTO `Outpatient` VALUES('%d','%s', '%s', '%s','%s','%d','%d','%s','%s')" % (
            row["Patient Id"], row2["First name"],row2["Middle name"], row2["Last name"],row2["H.no"],row2["Pin_code"],row2["Street no."],row2["City"],
             row2["State"]
            )
           cur.execute(query)
           con.commit()
        except Exception as e:
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
        row_contact = []
        try:
          num = int(input("Number of Contact numbers the patient has: "))
        except Exception as e:
          print(e)
          print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")

        for i in range(num):
         row_contact.append(input("Contact number: "))

        for i in range(num):
         try:
            query = "INSERT INTO `Contact_number` VALUES('%s', '%d')" % (
                 row_contact[i],row["Patient Id"])
            cur.execute(query)
            con.commit()
         except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
        try:
          
           query = "INSERT INTO `Billing` VALUES('%d','%d','%d','%d','%s')" % (
             row2["Bill number"],row["Patient Id"],0,row2["doc_cost"],row2["Date"]
            )
           cur.execute(query)
           con.commit()
        except Exception as e:
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
        try:
           query = "INSERT INTO `Treatment` VALUES('%d','%d','%d')" % (
             row2["Bill number"],row2["Staff Id1"],row["Patient Id"]
            )
           cur.execute(query)
           con.commit()
        except Exception as e:
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return 
        try:
           query = "INSERT INTO `Treatment` VALUES('%d','%d','%d')" % (
             row2["Bill number"],row2["Staff Id2"],row["Patient Id"]
            )
           cur.execute(query)
           con.commit()
        except Exception as e:
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return     
        
    
    
    row_issues = []
    try:
        num = int(input("Number of issues the patient has: "))
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
    for i in range(num):
        row_issues.append(input("Issue: "))

    for i in range(num):
        try:
            query = "INSERT INTO `Issues` VALUES('%s', '%d')" % (
                 row_issues[i],row["Patient Id"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return 

   

    return


def Ins_new_Staff():
    global cur
    row = {}
    print("Enter the new Staff's details: ")

    row["Staff Id"] = int(input("Staff Id: "))
    row["First_Name"] = input("First Name: ")
    row["Middle_Name"] = input("Middle Name: ")
    row["Last_Name"] = input("Last Name: ")
    row["Dept_Id"] = int(input("Department Id: "))
    row["Date"] = int(input("Birth date: "))
    row["Month"] = int(input("Birth month: "))
    row["Year"] = int(input("Birth year: "))
    row["Salary"] = int(input("Salary: "))
    row["Gender"] = input("Gender: ")
    row["H.no"] = input("House no: ")
    row["Pin_Code"] = int(input("Pin code: "))
    row["Street.no"] = int(input("Street no: "))
    row["City"] = input("City: ")
    row["State"] = input("State: ")
    try:
        query = "INSERT INTO Staff VALUES('%d', '%d', '%d', '%d', '%d', '%d', '%s', '%d', '%d','%s','%s','%s','%s','%s','%s')" % (
            row["Staff Id"],row["Dept_Id"], row["Date"], row["Month"],row["Year"],row["Salary"],row["H.no"],row["Pin_Code"],
            row["Street.no"],row["City"],row["State"],row["Gender"], row["First_Name"], row["Middle_Name"], row["Last_Name"], 
            )
        cur.execute(query)
        con.commit()
    except Exception as e:
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

          
    i=int(input("Is the staff a Doctor or a Nurse?: (choose 1 if Doctor (or) choose 2 if Nurse): "))
    if(i==1):
        Ins_new_Doctor()
    if(i==2):
        Ins_new_Nurse()    
    return
    
def InsOp():
    print("Welcome!\n")
    print("Choose which insertion you want to make\n")
    print("CHOOSE AN OPTION:(print the corresponding number)\n")
    print("1.Insert new Patient")
    # print("3.Insert new Bill")
    print("2.Insert new Staff")


    inp = input("\nCHOICE ? ")
    if(inp == '1'):
     Ins_new_Patient()
    # elif(inp == '2'):
    #   Ins_new_Bill()
    elif(inp == '2'):
     Ins_new_Staff()
    return

def UpdOp():
    print("Welcome!\n")
    print("Choose which informaation do you want to update\n")
    print("CHOOSE AN OPTION:(print the corresponding number)\n")
    print("1.Update the salary of the Staff")
    print("2.Update the cost of Rooms")
    # print("3.Update the Status of the rooms when a patient enters or leaves")

    inp = input("\nCHOICE ? ")
    if(inp == '1'):
     Upd_Sal()
    elif(inp == '2'):
     Upd_room()
    # elif(inp == '3'):
    #  Upd_stat_room()
    return

def DelOp():
    print("Welcome!\n")
    print("Choose which informaation do you want to delete\n")
    print("CHOOSE AN OPTION:(print the corresponding number)\n")
    print("1.Delete the staff that has resigned")

    inp = input("\nCHOICE ? ")
    if(inp == '1'):
     Del_Staff()
    return

def Misc():

    print("Welcome!\n")
    print("Choose which type of retrivals you want to make\n")
    print("CHOOSE AN OPTION:(print the corresponding number)\n")
    print("1.Selection")
    print("2.Projection")
    print("3.Aggregate")
    print("4.Search")
    print("5.Analysis")

    inp = input("\nCHOICE ? ")
    if(inp == '1'):
     Selec()
    elif(inp == '2'):
     Proj()
    elif(inp == '3'):
     Aggre()
    elif(inp == '4'):
     Search()
    elif(inp == '5'):
     Analysis()

    return



while(1):
    from tabulate import tabulate
    tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")
    

    try:
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='lol4',
                              cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(e)
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
        continue
   
    with con:
         print("Established!\n")
         cur = con.cursor()
         while(1):
           # tmp = sp.call('clear',shell=True)
            
            print("CHOOSE AN OPTION:(print the corresponding number)\n")
            print("1.Insert Options")
            print("2.Update Options")
            print("3.Deletion Options")
            print("4.Misc Options")
            print("5.To quit")

            inp = input("\nCHOICE ? ")
            if(inp == '1'):
                InsOp()
            elif(inp == '2'):
                UpdOp()
            elif(inp == '3'):
                DelOp()
            elif(inp == '4'):
                Misc()
            elif(inp == '5'):
                    exitflag = 1
                    print("Bye")
                    break    

         break

