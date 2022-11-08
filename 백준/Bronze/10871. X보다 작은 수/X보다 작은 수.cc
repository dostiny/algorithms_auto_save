#include <iostream>

using namespace std;

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(0); 
    cout.tie(0);
    int N, A, num;
    cin >> N >> A;
    for (int i = 0; i < N; ++i) {
        cin >> num;
        if (num < A) {
            cout << num << " ";
        }
    }
}