#include <iostream>
#include <string>

using namespace std;

int main() {
  int n, q;
  string s, s1, s2, tmp_s;
  char tmp_c;

  cin >> n;
  cin >> s;
  cin >> q;

  s1 = s.substr(0, n);
  s2 = s.substr(n, n);

  int t, a, b, j, k;
  bool rev = false;
  for (int i = 0; i < q; i++) {
    cin >> t >> a >> b;
    if (t == 1) {
      j = (a - 1) % n;
      k = (b - 1) % n;
      if ((b <= n) && !rev || (n < a) && rev) {
        tmp_c = s1[j];
        s1[j] = s1[k];
        s1[k] = tmp_c;
      } else if ((n < a) && !rev || (b <= n) && rev) {
        tmp_c = s2[j];
        s2[j] = s2[k];
        s2[k] = tmp_c;
      } else if ((a <= n) && (n < b) && !rev) {
        tmp_c = s1[j];
        s1[j] = s2[k];
        s2[k] = tmp_c;
      } else if ((a <= n) && (n < b) && rev) {
        tmp_c = s1[k];
        s1[k] = s2[j];
        s2[j] = tmp_c;
      }
    } else {
      rev = !rev;
    }
  }

  if (rev) {
    cout << s2 << s1 << endl;
  } else {
    cout << s1 << s2 << endl;
  }

  return 0;
}
