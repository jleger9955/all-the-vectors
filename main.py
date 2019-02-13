# read in the vectors.txt file
# create a  list of vectors
# scale the first and last vector by 3
# add them all together and find
# that new vector
# find the norm of the final vector
# also find the dot product between the 2nd and 3rd vector
import vector as v


vectors = []
with open('vectors.txt') as f:
    for line in f:
        strvec = line.strip().split(',')
        intvec = [int(n) for n in strvec]
        vectors.append(v.Vector(*intvec))


dim = vectors[0].dimension
vectors[0] = vectors[0].scale(3)
vectors[-1] = vectors[-1].scale(3)

sumvector = v.Vector(*[0 for n in range(dim)])

for n in range(len(vectors)):
    sumvector += vectors[n]

print('The list of vectors is: ', vectors)
print('The sum of all vectors is: ', sumvector)
print('The norm of the sum of vectors is: ', sumvector.norm())
print('The dot product of the 2nd and 3rd vectors is: ', vectors[1].dotprd(vectors[2]))
