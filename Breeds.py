import sys
#White labrador
class Breeds1:
    def breed1(self):       
        d.detail()
        print(            """******Your pet "White labrador" is delivery as soon (Your order id - Wlab001)******

        _______________________________Have a nice day________________________________________
                                                                                            
                                                                                            """)
        sys.exit()       
a=Breeds1()
#Black labrador
class Breeds:
    def breed (self):        
        d.detail()
        print(            """******Your pet "Black labrador" is delivery as soon (Your order id - Blab001)******

        _______________________________Have a nice day________________________________________
                                                                                            
                                                                                            """)
        sys.exit()
b=Breeds()                              
#Roman rottweiler
class Breeds3:
    def Breed (self):
        d.detail()
        print(            """******Your pet "Roman rottweiler" is delivery as soon (Your order id - Rrot001)******

        _______________________________Have a nice day________________________________________
                                                                                            
                                                                                            """)
        sys.exit()
c=Breeds3()
#American rottweiler
class Breeds4:
    def Breed (self):        
        d.detail() 
        print(            """******Your pet "American rottweiler" is delivery as soon (Your order id - Arot001)******

        _______________________________Have a nice day________________________________________
                                                                                            
                                                                                            """)
        sys.exit()
d=Breeds4()
#British shorthair
class Breed5:
    def cat1(self):
        d.detail()
        print(            """******Your pet "British shorthair" is delivery as soon (Your order id - Bcat001)******

        _______________________________Have a nice day________________________________________
                                                                                            
                                                                                            """)
        sys.exit()
d=Breed5() 
#Persian cats
class Breed6:
    def cat2(self):
        d.detail()             
        print(              """******Your pet "Persian cat" is delivery as soon (Your order id - Pcat001)******

        _______________________________Have a nice day_________________________________________
                                                                                                                                                                                        
                                                                                            """)              
        sys.exit()    

    def detail(self):
        print("Please give your details for Delivery Purpose:\n")
        q2=input("Enter your Name : ")
        q3=input("Enter your Address : ")
        q4=input("Enter your mobile no : ")
        print("""**********Thanks for booking********** \n""")
             
d=Breed6() 

class types:
    def pets(self):
         pets=input("""Which pet do you want to buy:
                      1.Dogs

                      2.Cats 

                      3.Exit

                      Please select:""").strip()
         if pets=="1":
                 print("*******************You selected (Dogs)******************")
                 dog=input("""Dogs lists :
                              1.labrador retriver

                              2.Rottweiler

                              Please select:    """).strip()
                                      
                 if dog=="1":
                  print("***************You selected labrador***************")
                  labrador=input("""Which variety do you want:
                                  1.White labrador- age  : 45 days puppy  (Available-1 Male Puppy) 
                                  
                                  2.Black labrador- age  : 50 days puppy (Available-1 Female Puppy)
                                  
                                  Please select:  """)
                  if labrador=="1":
                      print("""you selected ***White labrador***
                                PRICE = RS:15000""") 
                      q1=input("""Do you want to Buy !
                                Payment:# Only for cash on Delivery #
                                Yes/No   :""").strip()
                      if q1 in ("yes","Yes"):
                         ko=Breeds1()
                         ko.breed1()
                      elif q1 in ("no","No"):
                          print ("Thank u for visiting")
                      else:
                          print("**Invalid option**")
                          
                  elif labrador=="2":
                      print("""you selected ***Black labrador***
                                PRICE = RS:9000""") 
                      q1=input("""Do you want to Buy !
                                Payment:# Only for cash on Delivery #
                                Yes/No   :""").strip()
                      if q1 in ("yes","Yes"):
                         kl=Breeds()
                         kl.breed()
                      elif q1 in ("no","No"):
                          print ("Thank u for visiting")
                      else:
                       print("**Invalid option**")
                  else:
                       print("**Invalid option**")
                         
                 if dog=="2":
                  print("***You selected Rottweiler***")
                  Rottweiler=input("""Which variety do you want:
                                  1.Roman Rottweiler- age  : 48 days puppy -(Available-1 Male Puppy) 
                                  2.American Rottweiler- age  : 52 days puppy -(Available-1 Male Puppy) 
                                  
                                  Please select:  """)
                  if Rottweiler=="1":
                      print("""you selected ***Roman Rottweiler***
                                PRICE = RS:30000""") 
                      q1=input("""Do you want to Buy !
                                Payment:# Only for cash on Delivery #
                                Yes/No   :""").strip()
                      if q1 in ("yes","Yes"):
                         k2=Breeds3()
                         k2.Breed()
                      elif q1 in ("no","No"):
                          print ("Thank u for visiting")
                      else:
                       print("**Invalid option**")

                  elif Rottweiler=="2":
                      print("""you selected ***American Rottweiler***
                                PRICE = RS:40000""") 
                      q1=input("""Do you want to Buy !
                                Payment:# Only for cash on Delivery #
                                Yes/No   :""").strip()
                      if q1 in ("yes","Yes"):
                         k2=Breeds4()
                         k2.Breed()
                      elif q1 in ("no","No"):
                          print ("Thank u for visiting")
                      else:
                       print("**Invalid option**")
                  else:
                      print("**invalid option**")
                                    
                 #if dog=="3":
                 #  print("You selected Bulldog ")       
                 #  print("""**********Now Bulldog is not available**********
                                
                 #                    ***Thank you for visiting***""")    
                 #  sys.exit()  


         elif pets=="2":
                print("*******************you selected (Cats)*******************")
                cats=input("""Cats lists:
                            
                              1.British shorthair - (Available-1 Male kitten -30days )
                              2.Persian cat- (Available- 1 Male kitten- 40days)

                              Please select:  """)  
                                          
                if cats=="1":
                      print("""You selected ***British shorthair*** 
                                 price = 40000""")
                      q1=input("""Do you want to Buy !
                                Payment:# Only for cash on Delivery #
                                Yes/No   :""").strip()
                      if q1 in ("yes","Yes"): 
                        k4=Breed5()
                        k4.cat1()
                      elif q1 in ("no","No"):
                          print ("Thank u for visiting")  
                      else:
                       print("**Invalid option**") 
                         
                elif cats=="2":
                      print("""You selected ***Persian cat***
                               price = 35000 """)
                      q1=input("""Do you want to Buy !
                                Payment:# Only for cash on Delivery #
                                Yes/No   :""").strip()
                      if q1 in ("yes","Yes"): 
                        k4=Breed6()
                        k4.cat2()
                      elif q1 in ("no","No"):
                          print ("Thank u for visiting") 
                      else:
                       print("**Invalid option**")
                else:
                      print("**invalid option**") 

         elif pets=="3":
          print("Thank you for visiting........")  

         else:
          print("**-Invalid option-**")

    
                  
t=types() 

            