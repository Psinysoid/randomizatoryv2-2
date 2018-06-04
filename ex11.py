import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
x=input("введіть ваш зріст у см")
m=int(x)/2.54
g=int(x)/100
v=g/float(3.3)
print(m,"Дюймів")
print(v,"Футів")
printTimeStamp("Краснощок")


