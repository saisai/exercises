function ack(M, N) {
    for(; M > 0; M--) {
        N = N === 0 ? 1 : ack(M, N - 1);
    }
    return N + 1;
}

console.log(ack(0, 0));
console.log(ack(4, 3));
