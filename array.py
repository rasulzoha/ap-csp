#Write a program that saves all odd numers between -6 and 47
#into a list

#check to see if a number is odd
#if it is, place it into the list
#print the list at the to check your work 

#taking the list elements and storing it in li
li=list(range(-6,38)) 
  print('odd numbers in the list')
for l in li:
    if l % 2 != 0: #running the loop to check the odd numbers
       print(l, end = " ")
