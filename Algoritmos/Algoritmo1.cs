using System;
class Program
{
    static void Main()
    {
        // Pedir al usuario el primer número
        Console.Write("Ingresa el primer número: ");
        double num1 = Convert.ToDouble(Console.ReadLine());

        // Pedir al usuario el segundo número
        Console.Write("Ingresa el segundo número: ");
        double num2 = Convert.ToDouble(Console.ReadLine());

        // Calcular la suma
        double suma = num1 + num2;

        // Mostrar el resultado
        Console.WriteLine($"La suma de {num1} + {num2} es: {suma}");
    }
}