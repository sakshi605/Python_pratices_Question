Y= int(input ("which Year you want to check : "))
if Y%4 ==0 :
    if Y%100==0:
        if Y%400==0:
            print("Leap Year")
        else : 
            print ("not Leap Year")
else :
    print ("not Leap Year")