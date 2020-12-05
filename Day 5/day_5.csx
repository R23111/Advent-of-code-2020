using System.IO;
using System.Collections.Generic;

int getRow(string ticket)
{
    int max = 127;
    int min = 0;
    foreach (var c in ticket)
        if (c == 'F')
            max = (min + max) / 2;
        else if (c == 'B')
            min = (min + max) / 2 + 1;
        else
            break;
    return max;
}

int getCol(string ticket)
{
    int max = 7;
    int min = 0;
    foreach (var c in ticket)
        if (c == 'L')
            max = (min + max) / 2;
        else if (c == 'R')
            min = (min + max) / 2 + 1;
        else
            continue;
    return max;
}

var f = File.ReadAllLines("./input.txt");
var ids = new List<int>();
int maxId = 0;
int myId = 0;

foreach (var ticket in f)
{
    var id = getRow(ticket) * 8 + getCol(ticket);
    ids.Add(id);
    if (maxId < id)
        maxId = id;
}

foreach (var id1 in ids)
{
    var hasNext = false;
    foreach (var id2 in ids)
        if ((id1 + 1 == id2))
            hasNext = true;
    if (!hasNext && id1 != maxId)
        myId = id1 + 1;
}

System.Console.WriteLine($"Part 1: {maxId}\nPart 2: {myId}");

