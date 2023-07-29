#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {

  // 入力
  int n, k;
  cin >> n >> k;
  int d = 0;
  vector<int> nums;
  for (int i{0}; i < n; i++) {
    cin >> d;
    nums.push_back(d);
  }

  // (mod K)の値が等しいもの同士のグループに分割する
  vector<vector<int>> groups(k);
  for (int i = 0; i < n; i++) {
    groups[i % k].push_back(nums[i]);
  }

  // K個のグループをそれぞれソート
  for (int i = 0; i < k; i++) {
    sort(groups[i].begin(), groups[i].end());
  }

  for (int i{0}; i < (n-1); i++) {
    if (groups[i % k][i / k] > groups[(i + 1) % k][(i + 1) / k]) {
      cout << "No\n";
      return 0;
    }
  }

  cout << "Yes\n";
  return 0;
}
