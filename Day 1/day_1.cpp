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
    vector<int> report;

    while (getline(f, l))
    {
        report.push_back(stoi(l));
    }
    f.close();

    for (int i = 0; i < report.size(); i++)
    {
        for (int j = i; j < report.size(); j++)
        {
            if (report.at(i) + report.at(j) == 2020)
            {
                cout << "Part 1: " << (report.at(i) * report.at(j)) << endl;
            }
            for (int k = j; k < report.size(); k++)
            {
                if (report.at(i) + report.at(j) + report.at(k) == 2020)
                {
                    cout << "Part 2: " << (report.at(i) * report.at(j) * report.at(k)) << endl;
                }
            }
        }
    }

    return 0;
}
