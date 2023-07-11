import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Bharani@890',database="pets")
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE console") #creating new database in sql
#mycursor.execute("show DATABASEs ")
#mycursor.execute("truncate ta ble users ")

def Pets(Name,Mobile_number,Pet_Name,Pet_color,Pet_age):
    res=mydb.cursor()
    sql="insert into Details(Name,Mobile_number,Pet_Name,Pet_color,Pet_age) values (%s,%s,%s,%s,%s)"
    user=(Name,Mobile_number,Pet_Name,Pet_color,Pet_age)
    res.execute(sql,user)
    mydb.commit()
    print("Your Details are enter sucessfully")


while True:
    print ("*************Welcome to pet Register system*************")
    print("1.Register a Pets ")
    print("2.Exit")


    choice=int(input("Enter your choice :  "))
    if choice==1:
        Name=input("Enter your Name : ")
        Mobile_number=input("Enter your Mobile Number: ")
        Pet_Name=input("Enter pet name with (M/f):   ")
        Pet_color=input("Enter pet color : ")
        Pet_age=input("Enter pet age : ")
        Pets(Name,Mobile_number,Pet_Name,Pet_color,Pet_age)
        print("***************Thank you for Registering***************")
        quit()

    elif choice==2:
        print("Thank you for visiting")
        quit()

    else:
        print("invalid option")