#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <climits>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <sstream>
#include <ctime>
#include <numeric>
#include <iterator>
#include <functional>
#include <bitset>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <array>
#include <typeinfo>
#include <initializer_list>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define REP(i, a, b) for (int i = (a); i < (b); i++)
#define RREP(i, a, b) for (int i = (a); i > (b); i--)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define TRvi(it, c) for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define inf 0x3f3f3f3f
#define EPS 1e-10
#define PI acos(-1.0)
#define scan(x) scanf("%d", x)
#define ll long long
#define mp make_pair
#define pb push_back
#define sqr(x) ((x) * (x))
#define LSOne(x) x & (-x)
#define debug(x) cout << #x << " " << x << endl;

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef ONLINE_JUDGE
    //  freopen("in.txt" , "r" , stdin);
    //  freopen("out.txt" , "w" , stdout);
    #endif
    int n;
    while (cin >> n){
        if (n == 0) break;
        int k;
        cin >> k;
        map<pair<int, int>, int> pyr;
        for (int i = 0; i < k; i++){
            int x = 0, y = 0;
            while (x + y != n - 1){
                if (pyr[{x, y}] == 0){
                    pyr[{x, y}] = 1;
                    x++;
                }
                else{
                    pyr[{x, y}] = 0;
                    y++;
                }
            }
        }
        cout << y << endl;
    }
    return 0;
}
