using System;
using System.IO;

namespace Day_1
{
    class Program
    {
        static void Main(string[] args)
        {
            var f = File.ReadAllLines(@"./input.txt");


            for (int i = 0; i < f.Length; i++)
                for (int j = i; j < f.Length; j++)
                {
                    if (int.Parse(f[i]) + int.Parse(f[j]) == 2020)
                        Console.WriteLine($"Part 1: {int.Parse(f[i]) * int.Parse(f[j])}");
                    for (int k = j; k < f.Length; k++)
                        if (int.Parse(f[i]) + int.Parse(f[j]) + int.Parse(f[k]) == 2020)
                            Console.WriteLine($"Part 2: {int.Parse(f[i]) * int.Parse(f[j]) * int.Parse(f[k])}");

                }
        }
    }
}
