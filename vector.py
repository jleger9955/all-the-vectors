# instructions
# create a vector class
# that should...
# add vectors
# scale vector
# norm or len
# dot product
# override __str__ and __repr__


class Vector():

    def __init__(self, *vec):
        self.vec = vec
        self.dimension = len(self.vec)

    def __add__(self, v):
        return Vector(*[self.vec[n] + v.vec[n] for n in range(self.dimension)])

    def __len__(self):
        return self.norm()

    def __str__(self):
        return str(self.vec)

    def __repr__(self):
        return self.__str__()

    def norm(self):
        sqrs = [self.vec[n]**2 for n in range(self.dimension)]
        norm = sum(sqrs)**(1 / 2)
        return norm

    def scale(self, scalefactor):
        return Vector(*[self.vec[n] * scalefactor for n in range(self.dimension)])

    def dotprd(self, v):
        return sum([self.vec[n] * v.vec[n] for n in range(self.dimension)])
