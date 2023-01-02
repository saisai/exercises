
const result = (() => {
  "use strict";

  const showBinary = n =>
     showIntAtBase_(2)(n);

  const showIntAtBase_ = base =>
    n => n.toString(base);

  const main = () => [5, 50, 9000]
    .map(n => `${n} -> ${showBinary(n)}`)
    .join("\n");

  return main();
})();

console.log(result);
