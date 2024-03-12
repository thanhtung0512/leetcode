#include<bits/stdc++.h>
using namespace std;

#define ll                 long long int
#define lld                long double
#define vi                 vector<ll>
#define pb                 push_back
#define MOD                (ll)(1e9 + 7)
#define rep(i,a,b)         for(ll i = a; i<b; ++i)
#define f(a)               for(ll i = 0; i<a; ++i)
#define all(a)             (a).begin(),(a).end()
#define present(c,x)       ((c).find(x) != (c).end())
#define cpresent(c,x)      (find(all(c),x) != (c).end())
#define p(a)               cout << a << endl;
#define p2(a,b)            cout << a << " " << b << endl;
#define fast_io            ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define __main__           signed main()


bool isPerfectSquare(long long x) {
    long long sq = sqrt(x);
    return sq * sq == x;
}

bool check(long long p, int q, long long N) {
    long long res = 1;
    for (int i = 0; i < q; ++i) {
        if (abs(res) > abs(N / p)) return false; // To prevent overflow
        res *= p;
    }
    return res == N;
}

void findPandQ(long long N) {
    if(N<0 && isPerfectSquare(N)) {
        cout << "Majin Buu" << endl;
        return;
        
    }
    if (N == 1 || N == -1) {
        cout << "Piccolo" << endl;
        return;
    }
    
    for (int q = 2; q <= 64; ++q) {
        long long low = 1, high = pow(10, 16), mid, p;
        bool found = false;

        while (low <= high) {
            mid = low + (high - low) / 2;
            p = (q % 2 == 0) ? mid : N < 0 ? -mid : mid; // Adjust p based on the parity of q and sign of N

            if (check(p, q, N)) {
                found = true;
                break;
            } else if (pow(p, q) < abs(N)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        if (found) {
            cout << "Piccolo" << endl;
            return;
        }
    }

    cout << "Majin Buu" << endl;
}

ll gcd(ll a, ll b) {
    return b == 0 ? a : gcd(b, a % b);
}
ll lcm(ll a, ll b) {
    return a * (b / gcd(a, b));
}

__main__{
    int T;
    cin>> T;
    while (T--) {
long long N;
    cin >> N;
    findPandQ(N);

    }
    
    return 0;

}