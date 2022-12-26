console.log(
(() => {

    // GENERIC FUNCTIONS ------------------------------------------------------
    //
    // concat :: [[a]] -> [a] | [String] -> String
    const concat = xs =>
        xs.length > 0 ? (() => {
            const unit = typeof xs[0] === 'string' ? '' : [];
            return unit.concat.apply(unit, xs);
        })() : [];

    // group :: Eq a => [a] -> [[a]]
    const group = xs => groupBy((a, b) => a === b, xs);

    // groupBy :: (a -> a -> Bool) -> [a] -> [[a]]
    const groupBy =(f, xs) => {
        const dct = xs.slice(1)
            .reduce((a, x) => {
                const
                    h = a.active.length > 0 ? a.active[0] : undefined,
                    blnGroup = h !== undefined && f(h, x);
                return {
                    active: blnGroup ? a.active.concat([x]) : [x],
                    sofar: blnGroup ? a.sofar : a.sofar.concat([a.active])
                };
            }, {
                active: xs.length > 0 ? [xs[0]] : [],
                sofar: []
            });
        return dct.sofar.concat(dct.active.length > 0 ? [dct.active] : []);
    }

    // intercalate :: String -> [a] -> String
    const intercalate = (s, xs) => xs.join(s);

    // map :: (a -> b) -> [a] -> [b]
    const map = (f, xs) => xs.map(f);


    // show :: a -> String
    const show =(...x) =>
        JSON.stringify.apply(
            null, x.length > 1 ? [x[0], null, x[1]] : x
        );

    // stringChars :: String -> [Char]
    const stringChars = s => s.split('');

    // TEST -------------------------------------------------------------------
    return show(
        intercalate(', ',
        map(concat, group(stringChars('gHHH5YY++///\\')))
           )
    );

})()
);