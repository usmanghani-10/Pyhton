import time
Time = time.strftime("%H:%M:%S")
print("Time : ",Time)
Hour = time.strftime("%H")
print("Hour : ",Hour)
Minute = time.strftime("%M")
print ("Minute : ",Minute)
Second = time.strftime("%S")
print ("Second : ",Second)
if Time >= "06:00:00" and Time < "12:00:00":
    print ("Good Morning")
elif Time >= "12:00:00" and Time < "14:00:00":
    print ("Good AfterNoon")
elif Time >= "14:00:00" and Time < "19:00:00":
    print ("Good Noon")
elif Time >= "19:00:00" and Time < "22:00:00":
    print ("Good Evening")
elif Time >= "22:00:00" and Time < "06:00:00":
    Print ("Good Night")