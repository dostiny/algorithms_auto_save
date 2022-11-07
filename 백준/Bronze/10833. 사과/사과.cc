#include <iostream>

using namespace std;

int main() {
    int n, a, student, apple, result = 0;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> student >> apple;
        result += apple % student;
    }
    cout << result;
    return 0;
}