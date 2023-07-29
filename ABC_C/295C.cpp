#include <iostream>
#include <set>

using namespace std;

int main() {
  int n;
  cin >> n;
  set<int> socks;
  int d = 0;
  int answer = 0;

  for (int i = 0; i < n; i++) {
    cin >> d;
    if (socks.find(d) == socks.end()) {
      socks.insert(d);
    } else {
      answer++;
      socks.erase(d);
    }
  }

  cout << answer << endl;

  return 0;
}
