const libs =
      `des_system_lib   std synopsys std_cell_lib des_system_lib dw02 dw01 ramlib ieee
        dw01             ieee dw01 dware gtech
          dw02             ieee dw02 dware
            dw03             std synopsys dware dw03 dw02 dw01 ieee gtech
              dw04             dw04 ieee dw01 dware gtech
                dw05             dw05 ieee dware
                  dw06             dw06 ieee dware
                    dw07             ieee dware
                      dware            ieee dware
                        gtech            ieee gtech
                          ramlib           std ieee
                            std_cell_lib     ieee std_cell_lib
                              synopsys`;

// A map of the input data, with the keys as the packages, and the values as
// and array of packages on which it depends.


const D = libs
    .split("\n")
    .map(e => e.split(' ').filter(e => e != ''))
    .reduce((p, c) =>
        p.set(c[0], c.filter((e, i) => i > 0 && e !== c[0] ? e : null)), new Map());

[].concat(...D.values()).forEach(e => {
    D.set(e, D.get(e) || [])
});

// The above map rotated so that it represents a DAG of the form
// // Map {
// //    A => [ A, B, C ],
// //    B => [C],
// //    C => []
// // }
// // where each key represents a node, and the array contains the edges.
//
// }

const G = [...D.keys()].reduce((p, c) =>
    p.set(
        c,
        [...D.keys()].filter(e => D.get(e).includes(c))
    ), new Map());

// An array of leaf nodes; nodes with 0 in degrees.
const Q = [...D.keys()].filter(e => D.get(e).length == 0);

// the result array
const S = [];
while (Q.length) {
    const u = Q.pop();
    S.push(u);
    G.get(u).forEach(v => {
        D.set(v, D.get(v).filter(e => e !== u));
        if(D.get(v).length == 0) {
            Q.push(v);
        }
    });
}

console.log('Solution ', S);

