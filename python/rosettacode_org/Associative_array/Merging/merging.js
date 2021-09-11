(() => {
    'use strict';

    console.log(JSON.stringify(
        Object.assign({},   // Fresh dictinoary
        { // Base
            "name": "Rocket Skates",
            "price": 12.75,
            "color": "yello"
        }, { //update.
            "price": 15.25,
            "color": "red",
            "year": 1974
        }
        ),
        null, 2
    ))
})();
