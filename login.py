from Breeds import types
import re
import csv
#import maskpass

class Login:
    def signin(self):
        while True:
          print("*********************************************************")
          print("SIGN UP")
          print("*********************************************************")
          filename='bharani.csv'
          Newuser=input("Enter New Username - ")
          NewPassword=input("Enter New Password - ")
          ConfirmPassword=input("Enter Confirm Password - ")
          pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
          pwd = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
          if re.match(pat,Newuser) and re.match(pwd,NewPassword) and NewPassword==ConfirmPassword:
              print("Thank You for Signing In")
              try:
                  with open(filename, 'a', newline="") as f:
                   writer = csv.writer(f,delimiter=",")
                   writer.writerow([Newuser, NewPassword])
              except FileNotFoundError:
                   print("Sorry, File does not exist")
              Login()  
              return
              #return True
          else:
              print("Invalid Entry!! Please try again")
    def login(self):
        print("*********************************************************")
        print("                       LOG IN")
        print("*********************************************************")
        while True:
            print("username - ")
            username=input()
            pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            if re.match(pat,username):
                password=input("Enter Password -")
                pwd = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
                try:
                    with open("bharani.csv","r") as f:
                      reader = csv.reader(f,delimiter=",")
                      for row in reader:
                        if re.match(pwd,password) and row == [username, password]:
                            print("*****Username and Password are valid*****")   
                except FileNotFoundError:
                    print("Sorry, File does not exist")              
                return
                #return True
            else:
                print("""*********************************************************
                                    Wrong Username or Password
                       *********************************************************""")
                
l=Login()


class menu:
    def pet(self):
           
        q1=input("""Only for cash on Delivery, do you want to buy pets 
        ******(yes/no)******    :\t""").strip()   
        if q1 in ("yes"):
         print ()
        elif q1 in ("no") :
         print ("thank you for visiting........")
         exit()
        else:
            print("invalid")
            lj.pet()
     

lj=menu()

#Locations and pets
class Location:
    def area(self):
        choice=input(""" Choose your location pets are available only for  below location:
                     1.    Cuddalore

                     2.    Neyveli

                     3.    vadalure

                     4.    Exit
                     
                     Please select location:  """)
        
        if choice=="1": 
            print("**********Your Selected Cuddalore**********\n")      
            k5=types()
            k5.pets() 
                                       
        elif choice=="2":
            print("your selected Neyveli\n")
            k6=types()
            k6.pets()
            
        elif choice=="3":
            print("your selected vadalure\n")
            k7=types()
            k7.pets()
    
        elif choice=="4":
            print("******Thank you for visiting******")  

        else:
            print("***INVALID OPTION***")
            
                  
lk=Location
                    

