function ack(m, n) {
    return m === 0 ? n + 1 : ack(m - 1, n === 0 ? 1 : ack(m, n- 1));
}

console.log(ack(0, 0));
console.log(ack(4, 3));
