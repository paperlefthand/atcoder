#include <iostream>

using namespace std;

int main()
{
    int n, k;
    cin >> n;
    cin >> k;

    for (int i = 1; i <= n; i++)
    {
        int result = i;
        int temp;

        for (int j = 0; j < k; j++)
        {
            temp = result;
            while (temp > 0)
            {
                result -= (temp % 10);
                temp /= 10;
            }
        }
        cout << result << endl;
    }
}