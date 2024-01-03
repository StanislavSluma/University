using ClassLibrary;
using System.Diagnostics;
using System.Runtime.CompilerServices;
using System.Text.Json;
using System.Threading;

class Programm
{
    static void Main(string[] args)
    {
        int AmountThread = 4;
        int InitCount = 2;

        WorkWithThread work = new(InitCount, AmountThread);
        Console.CursorVisible = false;
        object locker = new();
        work.Progress += (int percent) =>
        {
            lock (locker)
            {
                if (percent == 0)
                {
                    Console.SetCursorPosition(0, Int32.Parse(Thread.CurrentThread.Name) * 2);
                    Console.Write($"Поток {Thread.CurrentThread.Name} [");
                    Console.SetCursorPosition(110, Int32.Parse(Thread.CurrentThread.Name) * 2);
                    Console.Write($"] {percent}%");
                }
                else
                {
                    Console.SetCursorPosition(8 + percent, Int32.Parse(Thread.CurrentThread.Name) * 2);
                    Console.ForegroundColor = ConsoleColor.DarkCyan;
                    Console.Write("=>");
                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                    Console.SetCursorPosition(112, Int32.Parse(Thread.CurrentThread.Name) * 2);
                    Console.Write($"{percent}%");
                    Console.ResetColor();
                }
            }
        };
        work.TimerEnd += (double integral, long milisec) =>
        {
            lock (locker)
            {
                Console.SetCursorPosition(0, Int32.Parse(Thread.CurrentThread.Name) * 2 + 1);
                Console.Write($"Результат: {integral}, Затраченное время: {milisec}ms");
                Console.SetCursorPosition(0, AmountThread * 2 + 1);
            }
        };

        /*Thread thread1 = new(work.Integral);
        Thread thread2 = new(work.Integral);
        thread1.Name = "0";
        thread2.Name = "1";
        thread1.Priority = ThreadPriority.Highest;
        thread2.Priority = ThreadPriority.Lowest;
        thread1.Start();
        thread2.Start();*/
        for (int i = 0; i < AmountThread; i++)
        {
            Thread thread = new(work.Integral);
            thread.Name = $"{i}";
            thread.Start();
        }
    }
}
