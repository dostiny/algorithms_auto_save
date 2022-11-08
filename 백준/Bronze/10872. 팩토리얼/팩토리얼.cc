#include <iostream>

using namespace std;

int factorial (int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);

}

int main() {
    int N, result = 1;
    cin >> N;
    result = factorial(N);
    cout << result;
}