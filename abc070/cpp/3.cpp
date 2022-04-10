#include <iostream>
#include <vector>
#include <string>

using namespace std;

int gcd(int a, int b) {

    if(a<0) {
        return gcd(-a, b);
    }
    if(b<0) {
        return gcd(a, -b);
    }

    if (a<b) {
        return gcd(b, a);
    } else if (a==b) {
        return a;
    }

    int r = 0;
    while (b>0) {
        r = a % b;
        a = b;
        b = r;
    }
    return a;

}

int lcm(int a, int b) {
    
    if(a<0) {
        return lcm(-a, b);
    }
    if(b<0) {
        return lcm(a, -b);
    }

    int result = (a*b)/gcd(a,b);
    return result;

}

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};
    int a = lcm(24, 30);
    cout << a;
    
    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}