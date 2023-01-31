#include <iostream>

using namespace std;

int main()
{
    int rate;
    cin >> rate;
    string contest;

    if (rate < 1200)
    {
        contest = "ABC";
    }
    else if (rate < 2800)
    {
        contest = "ARC";
    }
    else
    {
        contest = "AGC";
    }

    cout << contest << endl;
}