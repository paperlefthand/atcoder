#include <iostream>

using namespace std;

int main()
{
    int count = 0;
    string text;

    cin >> text;

    for (const char c : text)
    {
        if (c == 'v') {
            count += 1;
        } else if (c == 'w') {
            count += 2;
        }
    }
    cout << count << endl;
}