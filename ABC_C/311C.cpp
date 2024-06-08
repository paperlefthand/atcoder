#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {

  // 入力
  int n;
  cin >> n;
  int d = 0;
  vector<int> A;
  for (int i{0}; i < n; i++) {
    cin >> d;
    A.push_back(d);
  }

  // すでに通ったノードのインデックス
  vector<int> vec;

  // A0(頂点1の行き先)からスタート
  int index = 0;

  vector<int>::iterator itr;
  for (int i{0}; i <= n; i++) {
    itr = find(vec.begin(), vec.end(), index);
    // 通ったことがあるか
    if (itr == vec.end()) {
      // なければ, インデックスを更新
      vec.push_back(index);
      index = A[index] - 1;
    } else {
      vector<int>::iterator itr2;
      for (itr2 = itr; itr2 != vec.end(); itr2++) {
        std::cout << A[*itr2] << " ";
      }
      std::cout << "\n";
      return 0;
    }
  }
}