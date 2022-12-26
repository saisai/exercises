'''Remove a defined subset of glyphs from a string'''


# exceptGlyphs :: String -> String -> String
def exceptGlyphs(exclusions):
    print('exclusions', exclusions)

    '''A string from which all instances of a
       given set of glyphs have been removed.
    '''
    def go(s):
        print('s', s)
        return ''.join([
            c for c in s if c not in exclusions
        ])
    return go


# -------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Test'''

    txt = '''
        Rosetta Code is a programming chrestomathy site. 
        The idea is to present solutions to the same 
        task in as many different languages as possible, 
        to demonstrate how languages are similar and 
        different, and to aid a person with a grounding 
        in one approach to a problem in learning another.'''

    print(
        exceptGlyphs('eau')(txt)
    )

txtt = '''
        Rosetta Code is a programming chrestomathy site. 
        The idea is to present solutions to the same 
        task in as many different languages as possible, 
        to demonstrate how languages are similar and 
        different, and to aid a person with a grounding 
        in one approach to a problem in learning another.'''

# MAIN ---
if __name__ == '__main__':
    #main()
    aa = exceptGlyphs('eau')
    print(aa(txtt))