import time
import multiprocessing

import numpy as np

def getnpx(mt, age, interest):
    val = 1
    initval = 1
    for i in range(age, 55):
        val = val * mt[i]
        intval = val / (1 + interest) ** (i + 1 - age)
        initval = initval + intval
        
    return initval

def getnpx2(mt, age, interest):
    val = mt[age]
    initval = 1
    for i in range(age + 2, 55):
        val *= mt[i - 1]
        if mt[age]==0:
            intval =0
        else:
            intval = val / (1 + interest) ** (i - age - 1) / mt[age]
        initval = initval + intval
    return initval

def getnpxtocert(mt, age, maxvalue):
    val = mt[age]
    for i in range(age + 1, min(maxvalue, 7)):
        val = val * mt[i]
    return val

def calcannfactprelim(pval, age, intrate, certper):
    npx = getnpx(pval, age + int(certper), intrate)
    npx2 = getnpx2(pval, age + int(certper), intrate)

    if certper == 0:
        index = 1
        index2 = pval[age + int(certper)]

    else:
        index = getnpxtocert(pval, age,
                             age + int(certper)) 
        index2 = getnpxtocert(pval, age,age + int(certper) + 1)

    return index*npx+index2*npx2

pval = np.array([0.000291,0.00027,0.000257,0.000294,0.000325,0.00035,0.000371,0.000388,0.000402,0.000414,0.000425,0.000437,0.011016,0.012251,0.013657,0.015233,0.016979,0.018891,0.020967,0.023209,0.025644,0.028304,0.03122,0.034425,0.037948,0.041812,0.046037,0.050643,0.055651,0.06108,0.066948,0.073275,0.080076,0.08737,0.095169,0.103455,0.112208,0.121402,0.131017,0.14103,0.151422,0.162179,0.173279,0.184706,0.196946,0.210484,0.225806,0.243398,0.263745,0.287334,0.314649,0.346177,0.382403,0.423813,0.470893])
age=3
intrate=0.04
certper=1

start=time.time()
print(calcannfactprelim(pval, age, intrate, certper))
print(time.time()-start)


def calcannfactprelim_v(pval, age, intrate, certper):
    with multiprocessing.Pool(2) as pool:
        a1 = pool.apply_async(getnpx, (pval, age, intrate, certper,))
        a2 = pool.apply_async(getnpx2, (pval, age, intrate, certper,))
        result1 = a1.get()
        result2 = a2.get()

    # both processes finished
    if certper == 0:
        index = 1
        index2 = pval[age + int(certper)]

    else:
        index = getnpxtocert(pval, age,
                             age + int(certper)) 
        index2 = getnpxtocert(pval, age,age + int(certper) + 1)
    return index*a1+index2*a2
if __name__ == '__main__':
    start=time.time()
    print(calcannfactprelim_v(pval, age, intrate, certper))
    print(time.time()-start)
    
    # https://stackoverflow.com/questions/69488431/python-how-to-use-multiprocessing-to-different-functions-with-return