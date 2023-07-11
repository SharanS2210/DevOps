from login import Login
from login import menu
from login import Location

print("__________________________________________________________________________________________")
print("*************welcome to pet selling system*************")
print("__________________________________________________________________________________________")
print("*************Available pets*************")
print(""">>Labrador:
          *white labrador-45days puppy
          *Black labrador-50days puppy""")
print(""">>Rotweiller:
          *Roman-48 days puppy
          *American-52 days puppy""")
print(""">>Cat:
          *British short hair-30 days
          *Persian cat-40 days""")

print("1.SignUP")
print("2.Login")
print("3.Exit")
while True:
    choice=int(input("Enter your Choice-"))
    if choice==1:
        g=Login()
        g.signin()
        g.login()
        break
    elif choice==2:
        g=Login()
        g.login()
        break
    elif choice==3:
        print("********Thank you for visiting********")
        exit()
    else:
        print("******Invalid option******")
        
lc=menu()
lc.pet()
dd=Location()
dd.area()





