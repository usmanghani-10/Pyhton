name = input("Enter your name : ")
city = input("Enter your city name : ")
programm = input("Enter your programm : ")
department = input("Enter your department : ")
semester = input("Enter semester : ")
GPA = float(input("Enter your GPA : "))

intro = f'''Hello ! My name is {name} from {city} ,
I am doing {programm},{department} and currently in {semester}
and I have got {GPA: .2f} GPA''' 
print (intro)