#include <iostream>
#include <algorithm>

using namespace std;

int arr[1001];

int main() {
    int cnt, n;
    cin >> cnt;
    for (int i = 0; i < cnt; i++) {
        cin >> n;
        arr[i] = n;
    }
    sort(arr, arr + cnt);
    for (int i = 0; i < cnt; i++) {
        cout << arr[i] << "\n";
    }
}