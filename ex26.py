import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
a=input("")
b=input("")
c=input("")
if a==b==c: print("трикутник рівносторонній")
elif a==b or a==c or b==c : print("трикутник рівнобедренний")
else: print("трикутник різносторонній")
printTimeStamp("Олійник")