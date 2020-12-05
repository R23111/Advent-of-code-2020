#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int GetRow(string ticket)
{
    int max = 127;
    int min = 0;

    for (int i = 0; i < ticket.size(); i++)
    {
        if (ticket[i] == 'F')
            max = (min + max) / 2;
        else if (ticket[i] == 'B')
            min = (min + max) / 2;
        else
            break;
    }
    return max;
}

int GetCol(string ticket)
{
    int max = 7;
    int min = 0;

    for (int i = 0; i < ticket.size(); i++)
    {
        if (ticket[i] == 'L')
            max = (min + max) / 2;
        else if (ticket[i] == 'R')
            min = (min + max) / 2;
        else
            continue;
    }
    return max;
}

int main()
{
    fstream f;
    f.open("input.txt");
    string l;
    vector<string> tickets;
    vector<int> ids;

    while (getline(f, l))
    {
        tickets.push_back(l);
        ids.push_back(GetRow(l) * 8 + GetCol(l));
    }
    f.close();

    int maxId = 0;
    int myId = 0;

    for (int i = 0; i < tickets.size(); i++)
    {
        bool hasNext = false;
        if (maxId < ids[i])
            maxId = ids[i];

        for (int j = 0; j < tickets.size(); j++)
        {
            if ((ids[i] + 1) == ids[j])
                hasNext = true;
        }

        if (!hasNext && ids[i] != maxId)
            myId = ids[i] + 1;
    }

    cout << "Part 1: " << maxId << "\nPart 2: " << myId << endl;

    return 0;
}
