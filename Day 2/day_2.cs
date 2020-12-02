using System;
using System.IO;

var f = File.ReadAllLines(@"./input.txt");

var validPasswordsPt1 = 0;
var validPasswordsPt2 = 0;

foreach (var pw in f)
{
    var pass = new string[4];
    var temp = pw.Split('-');
    pass[0] = temp[0];
    pass[1] = temp[1].Split(' ')[0];
    pass[2] = temp[1].Split(' ')[1].Replace(":", "");
    pass[3] = temp[1].Split(' ')[2];

    var count = 0;
    foreach (var l in pass[3])
        if (l == pass[2][0])
            count++;

    if (count >= int.Parse(pass[0]) && count <= int.Parse(pass[1]))
        validPasswordsPt1++;

    if (pass[3][int.Parse(pass[0]) - 1] == pass[2][0] ^ pass[3][int.Parse(pass[1]) - 1] == pass[2][0])
        validPasswordsPt2++;
}

Console.WriteLine($"part 1: {validPasswordsPt1} \npart 2: {validPasswordsPt2}");
