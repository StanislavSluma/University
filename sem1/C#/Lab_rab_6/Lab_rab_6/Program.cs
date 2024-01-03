using Lab_rab_6;
using System.Collections.Generic;
using System.Reflection;

class Program
{
    static void Main(string[] args)
    {
        Employee[] employee_arr = {new Employee("First", 18, true), new Employee("Second", 18, false), new Employee("Third", 18, true), new Employee("Forth", 18, false), new Employee("Fifth", 18, true)};
        var assembly = Assembly.LoadFrom(@"D:\AA_curs2\sem1\C#\Lab_rab_6\FileServiceLib\bin\Debug\net7.0\FileServiceLib.dll");
        Type? FileService = assembly.GetType("FileServiceLib.FileService`1").MakeGenericType(typeof(Employee));

        var fs = Activator.CreateInstance(FileService);

        MethodInfo? readfile = FileService.GetMethod("ReadFile");
        MethodInfo? savedata = FileService.GetMethod("SaveData");
        savedata?.Invoke(fs, new object[] { employee_arr, @"D:\AA_curs2\sem1\C#\Lab_rab_6\Employee.JSON" });
        var read = readfile?.Invoke(fs, new object[] { @"D:\AA_curs2\sem1\C#\Lab_rab_6\Employee.JSON" });
        IEnumerable<Employee>? readiable = (IEnumerable<Employee>?)read;
        foreach (var employee in readiable)
        {

            Console.WriteLine($"Name: {employee.Name}, Age: {employee.Age}, Merried: {employee.Merried}");
        }
    }
}
