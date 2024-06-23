A = {1,2,3,4,5,"Muhammad","Usman","Ghani"}
B = {4,5,6,7,8,"Ghani","Khan","Danish"}
print (A , B)
print ("Union",A.union(B))
A.update(B)
print("Update",A)
print ("Intersection", A.intersection(B))
print ("Symmetric Difference",A.symmetric_difference(B))
A.add("The great")
print (A)
B.pop()
print (B)
B.clear()
print (B)
A.remove("Usman")
print (A)
C = {3,4,5,6,"Usman","Ghani","Danish"}
print (A.isdisjoint(C))
print  (A.issubset(C))
print (A.issuperset(C))




