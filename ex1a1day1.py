import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
x=float(input())
'кількість контейнерів <= 1л {:.2f}'.format(x)
z=float(input())
'кількість контейнерів > 1л {:.2f}'.format(z)
print(x * 0.10,"$","cума за кількість контейнерів <= 1л",z * 0.25,"$","cума за кількість контейнерів > 1л")
printTimeStamp("Краснощок")
