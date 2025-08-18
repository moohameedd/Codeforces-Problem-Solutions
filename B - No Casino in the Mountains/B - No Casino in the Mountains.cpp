// Code by Mohamed (C++ version)

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        // Convert array to string
        string s = "";
        for (int i = 0; i < n; i++) {
            s += to_string(a[i]);
        }

        // Build pattern of k zeros
        string m(k, '0');

        int nb = 0;
        size_t pos;
        while ((pos = s.find(m)) != string::npos) {
            nb++;
            s.erase(pos, k + 1); // remove substring starting at pos
        }

        cout << nb << "\n";
    }

    return 0;
}
