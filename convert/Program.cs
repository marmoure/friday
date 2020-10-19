using System;
using System.Diagnostics;
using System.IO;

namespace convert
{
    class Program
    {
        static void Main(string[] args)
        {
            if(args.Length != 1)
            {

                Console.WriteLine("no args");
                System.Environment.Exit(1);
            }
            string fileName = args[0];
            
            fileName = fileName.Split(@"\")[fileName.Split(@"\").Length -1];
            fileName = fileName.Split(".")[0];


            string filePath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), $"./vids/{fileName}.mp4");


            //Console.WriteLine("FFMPEG");
            string ffmpeg = @".\ffmpeg\ffmpeg.exe";
            string argument = $"-i {args[0]} {filePath}";

            Process p = new Process();
            p.StartInfo.FileName = ffmpeg;
            p.StartInfo.Arguments = argument;

            p.Start();
            p.WaitForExit();
            p.Close();
            
           
        }
    }
}
