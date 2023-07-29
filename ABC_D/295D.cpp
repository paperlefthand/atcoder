#include <iostream>
#include <string>

using namespace std;

bool happy(string s) {
  if (s.length()%2 == 0) {
    
  }
}

int main() {
  string s;
  cin >> s;
  int answer = 0;
  int n = s.length();
  string s_sub;

  int i = 2;
  while (i <= n) {
    for (int j = 0; j <= (n - i); j++) {
      s_sub = s.substr(j, i);
      if (happy(s_sub)) {
        answer++;
      }
    }
    i += 2;
  }
  // set<int> socks;
  // int d = 0;
  // int answer = 0;

  // for (int i = 0; i < n; i++) {
  //   cin >> d;
  //   if (socks.find(d) == socks.end()) {
  //     socks.insert(d);
  //   } else {
  //     answer++;
  //     socks.erase(d);
  //   }
  // }

  cout << answer << endl;

  return 0;
}
