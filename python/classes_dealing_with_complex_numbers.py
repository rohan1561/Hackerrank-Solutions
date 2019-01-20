class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, x):
        r = self.real+x.real
        i = self.imaginary+x.imaginary
        return Complex(r, i)

    def __sub__(self, x):
        r = self.real-x.real
        i = self.imaginary-x.imaginary
        return Complex(r, i)

    def __mul__(self, x):
        r = self.real*x.real-self.imaginary*x.imaginary
        i = self.real*x.imaginary+self.imaginary*x.real
        return Complex(r, i)

    def __div__(self, x):
        det = x.real**2+x.imaginary**2
        return self.__mul__(Complex(x.real/det, -x.imaginary/det))
    
    def mod(self):
        return Complex(((self.real)**2 + (self.imaginary)**2)**0.5, 0)

    def __repr__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary > 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % abs(self.imaginary)
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


