using System.Diagnostics;

namespace ClassLibrary
{
    public class WorkWithThread
    {
        static private Semaphore? sem;
        public delegate void ProgressBar (int percent);
        public event ProgressBar? Progress;
        public delegate void Time (double integral, long miliseconds);
        public event Time? TimerEnd;

        public WorkWithThread(int CountOfThread, int MaximalOfThread) 
        {
            sem = new(CountOfThread, MaximalOfThread);
        }

        public void Integral()
        {
            sem?.WaitOne();
            Stopwatch timer = new();
            double res = 0;
            int percent = 0;
            double acc = 1e-8;
            timer.Start();
            for(double xn = 0; xn <= 1 + acc; xn += acc)
            {
                res += Math.Sin(xn) * acc;
                if (xn * 100 >= percent)
                {
                    Progress?.Invoke(Convert.ToInt32(xn * 100));
                    percent++;
                }
            }
            timer.Stop();
            TimerEnd?.Invoke(res, timer.ElapsedTicks);
            sem?.Release();
        }
    }
}