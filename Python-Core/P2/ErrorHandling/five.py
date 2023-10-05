fp=open('emp.json')
try:
    fp=open('empone.json','r')
    print(fp.read())
except (ZeroDivisionError,IndexError,FileNotFoundError) as err:
    print(err)
finally:
    print('finally block execute - irrespecitve of try and exept')
    fp.close()