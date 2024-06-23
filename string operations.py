name = "!! Muhammad Usman Ghani !!!"
print (name)
print (len(name)) #To find the number of characters (length) 
print (name.rstrip("!")) #To remove a character from last
print (name.lower()) #To convert in lower form
print (name.upper()) #To convert in upper form
print (name.replace("Ghani","Danish")) #To replace a character with another
print (name.split(" ")) #To split character and form a list
print (name.split("a")) #To split character and form a list
A = "INTRODUCTION TO PYTHON" 
print (A.capitalize())   # To make the fist alpahbet capital and other small
print (name.center(70)) # To craete Spaces 
print (A.center(70)) 
print (len(A.center(70)))
print (len(name.center(70)))
print (name.count("a")) # To count a specific character in string
print ("End with !!",name.endswith("!!")) #To check if the string end with a specific character
print ("End with man",name.endswith("man,4,12")) 
print ("comtain number and alphabets : ",name.isalnum()) # To check if string contain alphabets and numbers only
print ("Is alphabetic :",name.isalpha()) # To check if string contain alphabets only
print("Is decimal : ",name.isdecimal()) # To check if string contain decimal 
print ("In lower : ",name.islower())  # To check if string is in lower from 
print ("In upper : ",name.isupper()) # To check if string is in upper form 
print ("In Nuemeric : ",name.isnumeric()) #To check if string is in numeric form
print ("Is printable : ",name.isprintable()) # To check if it is printable 
print("Title : ",name.title()) #Converting into title 
print ("Swap Case : ", name.swapcase()) #To swap case
print (name.find("U")) #To find the index of letter
print (name*4) # To print string more times