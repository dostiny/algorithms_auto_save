#include <iostream>

using namespace std;

int change(int x) {
    int h, t, n;
    h = x / 100;
    t = (x - h * 100) / 10;
    n = x - (h * 100 + t * 10);
    return n * 100 + t * 10 + h;
}

int max(int x, int y) {
    if (x > y) return x;
    else return y;
}

int main() {
    int num1, num2;
    cin >> num1 >> num2;
    cout << max(change(num1), change(num2));
}