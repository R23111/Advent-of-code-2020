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
                for (int j = i; j < f.Length; j++) //As i*j gives the same result as j*i, we can start the check at the last i index
                {
                    if (int.Parse(f[i]) + int.Parse(f[j]) == 2020)
                        Console.WriteLine($"Part 1: {int.Parse(f[i]) * int.Parse(f[j])}"); //part 1 answer
                    for (int k = j; k < f.Length; k++)
                        if (int.Parse(f[i]) + int.Parse(f[j]) + int.Parse(f[k]) == 2020)
                            Console.WriteLine($"Part 2: {int.Parse(f[i]) * int.Parse(f[j]) * int.Parse(f[k])}"); //part 2 answer

                }
        }
    }
}
