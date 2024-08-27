class MyComplexNumber:
    # Constructor methods
    def __init__(self, real = 0, imag = 0):
        print("MyComplexNumber constructor executing...")
        self.real_part = real
        self.imag_part = imag
        
    def displayComplex(self):
        print("{0} + {1}oriel".format(self.real_part,self.imag_part))    
        
        
# create a new object against MyComplexNumber class
cmplx1 = MyComplexNumber(40,50)

# calling displayComplex() function
cmplx1.displayComplex()        

# create another object against myComplexNumber class
# and create a new attribute 'new_attribute'
cmplx2 = MyComplexNumber(60,70)
cmplx2.new_attribute =80 

print(cmplx2.real_part, cmplx2.imag_part, cmplx2.new_attribute)
# output (60,70,80)

# Deleting object attribute and the object 
print(cmplx1)
del cmplx1.real_part
del cmplx1

print(cmplx1)