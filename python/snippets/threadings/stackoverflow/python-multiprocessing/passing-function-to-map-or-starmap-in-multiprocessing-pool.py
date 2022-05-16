import multiprocessing as mp 

def sumP(a, b):
    return (a * b) / (a - b + 1)

f1, f2, f3 = 24, 31, 45

if __name__ == "__main__":
    pool1 = mp.Pool(processes=3)
    new_rows2 = pool1.starmap(sumP, [(f1, f2), (f2, f3), (f1, f3)]) 
    print(new_rows2)
    
    # https://stackoverflow.com/questions/69535321/passing-function-to-map-or-starmap-in-multiprocessing-pool