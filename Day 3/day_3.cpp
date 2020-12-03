#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    fstream f;
    f.open("input.txt");
    string l;
    vector<string> map;

    int x[5] = {0, 0, 0, 0, 0};     // x position of the toboggan
    int add[5] = {1, 3, 5, 7, 1};   // The slope (on x)
    int trees[5] = {0, 0, 0, 0, 0}; // Counter of trees
    int i = 0;

    while (getline(f, l))
    {
        if (i == 0)
        {
            i++;
            continue;
        }
        for (int j = 0; j < 5; j++)
        {
            if (i % 2 == 0 || j != 4) // On the last slope, the toboggan goes 2 down at time, so if it's on an odd y, skip
            {
                x[j] = (x[j] + add[j]) % (l.size());
                if (l[x[j]] == '#')
                {
                    trees[j]++;
                }
            }
        }
        i++;
    }

    unsigned int mul = 1; // signed int overflows, so I used an unsigned int.
    for (int i = 0; i < 5; i++)
    {
        cout << trees[i] << endl;
        mul *= trees[i];
    }

    cout << fixed << "Part 1: " << trees[1] << "\nPart 2: " << mul << endl;

    return 0;
}
