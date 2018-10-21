alpha = {'A':1, 'I':1, 'J':1, 'Q':1, 'Y':1,' ':0,
         'B':2, 'K':2, 'R':2,
         'C':3, 'G':3, 'L':3, 'S':3,
         'D':4, 'M':4, 'T':4,
         'H':5, 'E':5, 'N':5, 'X':5,
         'U':6, 'V':6, 'W':6,
         'O':7, 'Z':7,
         'P':8, 'F':8}
#Dictionary contains the numbers according to each and every alphabets
Name = input(str("ENTER YOUR NAME IN CAPS:")) # Enter your name
total=0
for i in Name:              #Splitting the alphabets in your name and getting the values for it
    find = alpha.get(i)
    #print(find)           #This interates the values according to the given name
    total=find+total
#print(total)              #This prints the total values in our name
m=0
for x in str(total):
    newx = int(x)
    m = m + newx           #This adds up the number of digits present in the total
print("Your numerology number is:",m)

#for i in Name:
    #for i in alpha.items():
        #print(i)
    
