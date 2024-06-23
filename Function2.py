def Average (*Numbers):
    sum = 0
    for i in Numbers:
        sum = sum + i
    print ("Average is : ",sum / len(Numbers))
         
Average (2,334,56,12)         




def Average (*Numbers):
    sum = 0
    for i in Numbers:
        sum = sum + i
    Average = sum / len(Numbers)
    return Average
         
print(Average (2,334,56,12))  