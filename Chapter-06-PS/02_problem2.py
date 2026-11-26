a = int(input("Enter marks hindi :"))
b = int(input("Enter marks English :"))
c = int(input("Enter marks Maths :"))
total_percentage = (a + b + c)/3

if (total_percentage >= 40 and a >= 33 and b >= 33 and c >= 33):
    print("you are pass :", total_percentage)

else:
    print("you are fail try again next year!")