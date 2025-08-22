# que: write a program tht takes 5 numbers from user input , stores them in a list
# a) print the list 
# b) print maximum and minimum number from the list

number= []

num_1= int(input(" enter first value:"))
num_2= int(input(" enter second value:"))
num_3 = int(input(" enter third value :"))
num_4 = int(input(" enter fourth value:"))
num_5 = int(input(" enter fifth value : "))

number.append(num_1)
number.append(num_2)
number.append(num_3)
number.append(num_4)
number.append(num_5)

print(" Original number list:",number)

number.sort()
print(" Sorted list:", number.sort())            #returns none 

min_number= number[0]
print("minimum numb:",min_number)

max_numb= number[4]
print("maximum numb:",max_numb)