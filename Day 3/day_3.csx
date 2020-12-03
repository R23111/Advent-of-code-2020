using System.IO;

var f = File.ReadAllLines(@"./input.txt");

int[] x = {0, 0, 0, 0, 0};          // x position of the toboggan
int[] add = {1, 3, 5, 7, 1};        // The slope (on x)
int[] trees = {0, 0, 0, 0, 0};      // Counter of trees

for(int i = 1; i < f.Length; i++)
    for (int j = 0; j < 5; j++)    
        if (i % 2 == 0 || j != 4)   // On the last slope, the toboggan goes 2 down at time, so if it's on an odd y, skip
        {
            x[j] = (x[j] + add[j]) % (f[i].Length);
            if (f[i][x[j]] == '#')            
                trees[j]++;            
        } 

uint mul = 1;   // signed int overflows, so I used an unsigned int.
foreach(var t in trees) 
    mul*=(uint)t;

System.Console.WriteLine($"Part 1: {trees[1]}\nPart 2: {mul}");
