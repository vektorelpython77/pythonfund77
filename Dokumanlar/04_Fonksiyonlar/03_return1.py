""" 
return 
yield 
""" 

def fonk1(a,b):
    print(a+b)

def fonk2(a,b):
    return a+b
    print("ÇALIŞMAZ")

fonk1(2,3)
print(fonk1(2,3)) #None
print(fonk2(2,3)) #5 çünkü return sayıları dışarı gönderdi
