ids=[101,102,103,104,105]

try:
    #print(10/1)  # create ZDE object - handover to pvm
    #print(ids[2])#create indexError object
    
    #fp=open('emp.json','r')
    #print(fp.read())
    a = int(input('Enter Number:'))
    print(a)
#except Exception as err:
#    print(err)
except ZeroDivisionError as err:
    print(err)
except IndexError as err:
    print(err)
except FileNotFoundError as err:
    print(err)