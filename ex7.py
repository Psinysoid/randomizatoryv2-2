import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
x= input("введіть температуру в Цельсіях")
f = 273
g = 32
print(int(f)+ int(x))
print(int(g)+ int(x))
printTimeStamp("Краснощок")