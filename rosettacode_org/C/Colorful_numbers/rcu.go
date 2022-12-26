package rcu

import (
    "fmt"
    "rcu"
)

// Returns the larger of two ints.
func Max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

// Returns the smaller of two ints.
func Min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

// Returns the absolute value of an int.
func Abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

// Returns the greatest common divisor of two ints.
func Gcd(x, y int) int {
    for y != 0 {
        x, y = y, x%y
    }
    return x
}

// Returns the least common multiple of two ints.
func Lcm(x, y int) int { return Abs(x*y) / Gcd(x, y) }

// Returns whether or not an int is prime.
func IsPrime(n int) bool {
    switch {
    case n < 2:
        return false
    case n%2 == 0:
        return n == 2
    case n%3 == 0:
        return n == 3
    default:
        d := 5
        for d*d <= n {
            if n%d == 0 {
                return false
            }
            d += 2
            if n%d == 0 {
                return false
            }
            d += 4
        }
        return true
    }
}

// Sieves for primes up to and including 'limit'.
// Returns a bool slice 'c' of size (limit + 1) where:
// c[i] is false if 'i' is prime or true if 'i' is composite.
// Optionally processes even numbers >= 4.
func PrimeSieve(limit int, processEven bool) []bool {
    limit++
    // True denotes composite, false denotes prime.
    c := make([]bool, limit) // all false by default
    c[0] = true
    c[1] = true
    if processEven {
        for i := 4; i < limit; i += 2 {
            c[i] = true
        }
    }
    p := 3 // Start from 3.
    for {
        p2 := p * p
        if p2 >= limit {
            break
        }
        for i := p2; i < limit; i += 2 * p {
            c[i] = true
        }
        for {
            p += 2
            if !c[p] {
                break
            }
        }
    }
    return c
}

// Returns a slice of all primes up to and including 'limit'.
func Primes(limit int) []int {
    c := PrimeSieve(limit, false)
    if limit < 2 {
        return []int{}
    }
    primes := []int{2}
    for i := 3; i < len(c); i += 2 {
        if !c[i] {
            primes = append(primes, i)
        }
    }
    return primes
}

// Sieves for primes up to and including 'n' and returns how many there are.
// Uses an algorithm better suited to counting than the one used in the PrimeSieve method.
func PrimeCount(n int) int {
    if n < 2 {
        return 0
    }
    if n == 2 {
        return 1
    }
    count := 1
    k := (n-3)/2 + 1
    marked := make([]bool, k) // all false by default
    limit := (int(math.Sqrt(float64(n)))-3)/2 + 1
    for i := 0; i < limit; i++ {
        if !marked[i] {
            p := 2*i + 3
            s := (p*p - 3) / 2
            for j := s; j < k; j += p {
                marked[j] = true
            }
        }
    }
    for i := 0; i < k; i++ {
        if !marked[i] {
            count++
        }
    }
    return count
}

// Returns the prime factors of 'n' in order using a wheel with basis [2, 3, 5].
func PrimeFactors(n int) []int {
    if n < 2 {
        return []int{}
    }
    inc := []int{4, 2, 4, 2, 4, 6, 2, 6}
    var factors []int
    for n%2 == 0 {
        factors = append(factors, 2)
        n = n / 2
    }
    for n%3 == 0 {
        factors = append(factors, 3)
        n = n / 3
    }
    for n%5 == 0 {
        factors = append(factors, 5)
        n = n / 5
    }
    for k, i := 7, 0; k*k <= n; {
        if n%k == 0 {
            factors = append(factors, k)
            n = n / k
        } else {
            k += inc[i]
            i = (i + 1) % 8
        }
    }
    if n > 1 {
        factors = append(factors, n)
    }
    return factors
}

// Returns all the divisors of 'n' including 1 and 'n' itself.
func Divisors(n int) []int {
    if n < 1 {
        return []int{}
    }
    var divisors []int
    var divisors2 []int
    i := 1
    k := 1
    if n%2 == 1 {
        k = 2
    }
    for ; i*i <= n; i += k {
        if n%i == 0 {
            divisors = append(divisors, i)
            j := n / i
            if j != i {
                divisors2 = append(divisors2, j)
            }
        }
    }
    if len(divisors2) > 0 {
        ReverseInts(divisors2)
        divisors = append(divisors, divisors2...)
    }
    return divisors
}

// Returns all the divisors of 'n' excluding 'n'.
func ProperDivisors(n int) []int {
    d := Divisors(n)
    c := len(d)
    if c <= 1 {
        return []int{}
    }
    return d[0 : len(d)-1]
}

// Reverses a slice of ints in place.
func ReverseInts(s []int) {
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
}

// Returns a slice of an int's digits in base b.
func Digits(n, b int) []int {
    if n == 0 {
        return []int{0}
    }
    var digits []int
    for n > 0 {
        digits = append(digits, n%b)
        n /= b
    }
    ReverseInts(digits)
    return digits
}

// Returns the sum of an int's digits in base b.
func DigitSum(n, b int) int {
    sum := 0
    for n > 0 {
        sum += n % b
        n /= b
    }
    return sum
}

// Returns the sum of a slice of ints.
func SumInts(a []int) int {
    sum := 0
    for _, i := range a {
        sum += i
    }
    return sum
}

// Returns the maximum of a slice of ints (64-bit assumed)
func MaxInts(a []int) int {
    max := -1 << 63
    for _, i := range a {
        if i > max {
            max = i
        }
    }
    return max
}

// Returns the minimum of a slice of ints (64-bit assumed)
func MinInts(a []int) int {
    min := 1<<63 - 1
    for _, i := range a {
        if i < min {
            min = i
        }
    }
    return min
}

// Adds thousand separators to an int.
func Commatize(n int) string {
    s := fmt.Sprintf("%d", n)
    if n < 0 {
        s = s[1:]
    }
    le := len(s)
    for i := le - 3; i >= 1; i -= 3 {
        s = s[0:i] + "," + s[i:]
    }
    if n >= 0 {
        return s
    }
    return "-" + s
}

// Prints a slice of ints in tabular form with a given row and column size
// and optionally comma separators.
func PrintTable(s []int, rowSize, colSize int, commas bool) {
    for i := 0; i < len(s); i++ {
        if !commas {
            fmt.Printf("%*d ", colSize, s[i])
        } else {
            fmt.Printf("%*s ", colSize, Commatize(s[i]))
        }
        if (i+1)%rowSize == 0 {
            fmt.Println()
        }
    }
    if len(s)%rowSize != 0 {
        fmt.Println()
    }
}
