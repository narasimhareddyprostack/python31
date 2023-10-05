#given number is KA - Vehicle reg or not ?
#KA03AB4087
#KA01JK8289

#KA[012][0-9][A-Z]{2}\d{4}
import re 
vNo=input("Enter Vehicle Registration Number:")

result=re.fullmatch("KA[012][0-9][A-Z]{2}\d{4}", vNo)

if result:
    print("Yes! Given Number is proper - KA Registration Number")
else:
    print("Not - valid Number")
