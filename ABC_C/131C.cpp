#include <iostream>
#include <vector>

using namespace std;

int gcd(long int a, long int b)
{
    if (a < b)
    {
        return gcd(b, a);
    }
    else if (a == b)
    {
        return a;
    }

    long int r = 0;
    while (b > 0)
    {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main()
{
    long int a, b, c, d;

    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;

    long int lcm = (c * d) / gcd(c, d);

    // (1~bにあるcの倍数の数)-(1~(a-1)にあるcの倍数の数)
    long int div_by_c = (b / c) - (a - 1) / c;
    long int div_by_d = (b / d) - (a - 1) / d;
    long int div_by_lcm = (b / lcm) - (a - 1) / lcm;

    long int count = (b - a + 1) - div_by_c - div_by_d + div_by_lcm;

    cout << count << endl;
}