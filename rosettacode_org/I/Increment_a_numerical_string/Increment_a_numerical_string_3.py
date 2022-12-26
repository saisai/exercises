# Dropping or keeping any non-numerics in the string
 
 
# succString :: Bool -> String -> String
def succString(blnPruned):
    
    def go(x):        
        try:
            return [str(1 + (float(x) if '.' in x else int(x)))]
        except ValueError as e:
            print('e ', e, 'blnPruned ', blnPruned, 'a ', [x])           
            return [] if blnPruned else [x]
    return lambda s: ' '.join(concatMap(go)(s.split()))

def main():
    print(
            '\n'.join(
                [succString(bln)(
                    '41.0 pine martens in 1491 -1.5 mushrooms ≠ 136'
                    ) for bln in [False, True]]
                )
            )

# GENERIC ---------------------------------------------------
 
# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    
    def test(xs):
        
        return [ys[0] for ys in [f(x) for x in xs] if ys]
    return test
    
    #return lambda xs: (
    #        [ys[0] for ys in [f(x) for x in xs] if ys]
    #        )
            
            
print(concatMap('41.0 pine martens in 1491 -1.5 mushrooms ≠ 136'))            

if __name__ == '__main__':
    main()

