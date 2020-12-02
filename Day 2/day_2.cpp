#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <typeinfo>

using namespace std;

int main()
{
    fstream f;
    f.open("input.txt");
    string l;
    vector<string> passwords;

    int validPasswordsPt1 = 0;
    int validPasswordsPt2 = 0;

    //while there is a new line with a stringm push it (as a int) to 'report'
    while (getline(f, l))
    {
        passwords.push_back(l);
    }
    f.close();

    for (int i = 0; i < passwords.size(); i++)
    {
        string temp[4];
        bool i0 = true, i1 = true, i2 = true;
        int repetitions = 0;

        //Split the string (there must be an easier way to do this...)
        for (int j = 0; j < passwords[i].size(); j++)
        {
            if (passwords[i][j] == '-')
            {
                i0 = false;
                continue;
            }
            else if (i0)
            {
                temp[0] += passwords[i][j];
            }
            else if (i1 && passwords[i][j] == ' ')
            {
                i1 = false;
                continue;
            }
            else if (i1)
            {
                temp[1] += passwords[i][j];
            }
            else if (i2 && passwords[i][j] == ' ')
            {
                i2 = false;
                continue;
            }
            else if (i2)
            {
                if (passwords[i][j] != ':')
                    temp[2] += passwords[i][j];
            }
            else
            {
                temp[3] += passwords[i][j];
            }
        }

        // Part 1:
        for (int k = 0; k < temp[3].size(); k++)
        {
            if (temp[3][k] == temp[2][0])
            {
                repetitions++;
            }
        }
        if (repetitions >= stoi(temp[0]) && repetitions <= stoi(temp[1]))
        {
            validPasswordsPt1++;
        }

        // Part 2:
        if ((temp[3][stoi(temp[0]) - 1] == temp[2][0] && !(temp[3][stoi(temp[1]) - 1] == temp[2][0])) ||
            (temp[3][stoi(temp[1]) - 1] == temp[2][0] && !(temp[3][stoi(temp[0]) - 1] == temp[2][0])))
        {
            validPasswordsPt2++;
        }
    }

    cout << "Part 1: " << validPasswordsPt1 << "\nPart2: " << validPasswordsPt2 << endl;

    return 0;
}
