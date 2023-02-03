#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int n, y;

    cin >> n;
    cin >> y;
    y /= 1000;

    if (n <= y)
    {
        float a_temp = (y - n) / 9.0, b_temp;
        int a = 0, b = 0;
        while (a <= a_temp)
        {
            b_temp = (-9 * a + y - n) / 4.0;
            b = floor(b_temp);
            if (b == b_temp && (n - a - b) >= 0)
            {
                cout << a << " " << b << " " << (n - a - b) << endl;
                return 0;
            }
            a++;
        }
    }

    cout << -1 << " " << -1 << " " << -1 << endl;
    return 0;
}