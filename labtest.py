a=int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division:"))


from addition import addition
from sub import sub
from multiply import multiplication
from divide import division

if a==1:
	addition()
elif a==2:
	sub()
elif a==3:
	multiplication()
elif a==4:
	division()
else:
	print("Error")