import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
d=input("к-сть днів")
h=input("к-сть годин")
m=input("к-сть хвилин")
s=input("к-сть секунд")
d1=int(d)*86400
h1=int(h)*3600
m1=int(m)*60
print(d1,"к-сть секунд за проміжок днів")
print(h1,"к-сть секунд за проміжок годин ")
print(m1,"к-сть секунд за проміжок хвилин")
print(s,"проміжок секунд")
printTimeStamp("Псіна")