import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
x=input("what is your name?")
print("Hello dear",x)
printTimeStamp("Краснощок")