Salary = int(input("Enter Salary : "))
Service_Duration = int(input("Enter Duration of your Service in years : "))
if Service_Duration > 5:
    print("Congraculation Your New Salary is : ",Salary + (0.05*Salary))
else:
    print("No increment for you, WalaikumSalam !'_'")
    
    
    
    
Width = int(input("Enter Width : "))
Breath = int(input("Enter Breath : "))
if Width == Breath:
    print("It is Square !")
else:
    print("It is Rectangle !")    
    
    
    
 
Total_Classes = 672
print ("Total Classes = 672 ")    
Class_Attended = int(input("Enter number of classes you attended : ")) 
Percentage_Attendance = Class_Attended/Total_Classes*100   
print ("Your Percentage Attendance is : ",Percentage_Attendance," %")
if Percentage_Attendance > 75:
    print("You can gave the EXAM , Marhaba ")
else:
    print("You are having short attendance , Fi Amanillah Ya Habibi")
    
    
    
    
    
    
Year = int(input("Enter year : "))
if Year % 4 == 0:
    print ("It is leap Year ")
else:
    print ("It is not leap year ")        
    
    
    
    
    
Gender = input("Enter Your Gender ")
Age = int(input("Enter your age "))
if Gender.lower() == "male":
    if Age >= 20 and Age <= 30:
        print ("You can work anywhere !")
    elif Age >= 31 and Age <= 60:
        print ("You Will work only in Urban Areas ")
    else :
        print ("Invalid Age")
        

if Gender.lower() == "female":
    if Age >= 20:
        print ("You will work only in Urban Areas ")
    else: 
        print ("invalid Age")
            
    
         
    