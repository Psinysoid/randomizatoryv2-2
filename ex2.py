import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
x=input("Введіть ваш зріст у см")
y=input("введіть вашу масу в кг")
x1=int(x)*0.4
y1=int(y)/2.2
imt=(y1**2)/x1
print(imt)
printTimeStamp("Gus")