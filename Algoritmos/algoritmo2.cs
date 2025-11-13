using System;

class Verificador
{
    static void Main()
    {
        // Leer número del usuario
        Console.Write("Ingrese un número entero: ");
        int n = Convert.ToInt32(Console.ReadLine());

        // Verificar si es par o impar
        if (n % 2 == 0)
        {
            Console.WriteLine($"El número {n} es PAR");
        }
        else
        {
            Console.WriteLine($"El número {n} es IMPAR");
        }

        // Calcular el cuadrado
        int cuadrado = n * n;

        Console.WriteLine($"El cuadrado de {n} es: {cuadrado}");
    }
}
