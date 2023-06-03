"""
Inheritance Kalıtım
"""

# class A:
#     def __init__(self):
#         self.a = "A"

#     def soyleA(self):
#         print(self.a)

#     def soyle(self):
#         print("A Sınıfından Çalıştım")


# class B:
#     def __init__(self):
#         self.a = "A"
#         self.b = "B"

#     def soyleA(self):
#         print(self.a)

#     def soyleB(self):
#         print(self.b)

#     def soyle(self):
#         print("B Sınıfından Çalıştım")


######################################### inheritance uygulanınca 
# class A:
#     def __init__(self):
#         self.a = "A"

#     def soyleA(self):
#         print(self.a)

#     def soyle(self):
#         print("A Sınıfından Çalıştım")


# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.b = "B"
    
#     def soyleB(self):
#         print(self.b)


#     def soyle(self):
#         super().soyle()
#         print("----B Sınıfın Çalıştım")


# objA = A() 
# objB = B()
# objB.soyle() 
# objA.soyle()
# objA.soyleA()
# objB.soyleA()






# class A: # parent
#     def __init__(self):
#         self.a = "A"

#     def soyleA(self):
#         print(self.a)

#     def soyle(self):
#         print("A Sınıfından Çalıştım")


# class B(A):  # child
#     def __init__(self):
#         super().__init__()
#         self.b = "B"
    
#     def soyleB(self):
#         print(self.b)


#     def soyle(self):
#         super().soyle()
#         print("----B Sınıfın Çalıştım")


# class C(B):
#     def __init__(self):
#         super().__init__()
#         self.c = "C"

#     def soyleC(self):
#         print(self.c)


# objC = C()
# objC.soyleA()


######################################## Multiple Inheritance
class A: # parent
    def __init__(self):
        self.a = "A"

    def soyleA(self):
        print(self.a)

    def soyle(self):
        print("A Sınıfından Çalıştım")



class B: # parent
    def __init__(self):
        self.b = "B"

    def soyleB(self):
        print(self.b)

    def soyle(self):
        print("B Sınıfından Çalıştım")


class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c = "C"


    def soyleC(self):
        print(self.c)

    def soyle(self):
        B.soyle(self)
    
objC = C()
objC.soyle() 

