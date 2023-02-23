import numpy
for i in numpy.arange(0.0,2.0001,.2):
    for j in numpy.arange(1.0,4.0,1.0):
        if ( (i >0.0 and i <1.00) or (i>1.00 and i <2.00)):
            print("I={:.1f} J={:.1f}".format(i,i+j))
        else:
            a = int(i)
            b = int(j)
            c = a+b
            print("I={} J={}".format(a,c))
