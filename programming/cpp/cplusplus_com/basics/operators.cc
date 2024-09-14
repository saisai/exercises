#include <iostream>
using namespace std;

int main() {
    int y, x = 3;
    y = ++x;
    cout << y << x << endl;

    int a, b = 3;
    a = b++;
    cout << a << b << endl;
    cout << a << endl;
    return 0;
}
