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

