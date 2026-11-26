a = int(input("Enter your age :"))

# if elif else ladder

if (a>=18):
    print("your are valid for voting")
elif (a < 0):
    print("Please enter a valid age")
elif (a == 0):
    print("you are entering 0 which is not a valid age")        
else:
    print("your are not valid for voting")    

print("End of Program")     