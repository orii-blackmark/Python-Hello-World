class MyComplexNumber:
    # Constructor methods
    def __init__(self, real = 0, imag = 0):
        print("MyComplexNumber constructor executing...")
        self.real_path = real
        self.imag_part = imag
        
    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part,self.image_part))    
        