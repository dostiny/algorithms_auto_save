#include <iostream>

using namespace std;

int main() {
    int N, A;
    int arr[10001];
    cin >> N >> A;
    for (int i = 0; i < N; ++i) cin >> arr[i];
    for (int i = 0; i < N; i++) {
        if (arr[i] < A) cout << arr[i] << " ";
    }
}