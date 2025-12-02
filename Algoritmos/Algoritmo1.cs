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

        // Menú de operaciones
        Console.WriteLine("Selecciona una operación:");
        Console.WriteLine("1. Suma");
        Console.WriteLine("2. Resta");
        Console.WriteLine("3. Multiplicación");
        Console.WriteLine("4. División");
        int opcion = Convert.ToInt32(Console.ReadLine());

        double resultado = 0;

        // Switch-case para seleccionar operación
        switch (opcion)
        {
            case 1:
                resultado = num1 + num2;
                Console.WriteLine($"La suma de {num1} + {num2} es: {resultado}");
                break;
            case 2:
                resultado = num1 - num2;
                Console.WriteLine($"La resta de {num1} - {num2} es: {resultado}");
                break;
            case 3:
                resultado = num1 * num2;
                Console.WriteLine($"La multiplicación de {num1} * {num2} es: {resultado}");
                break;
            case 4:
                resultado = num1 / num2;
                Console.WriteLine($"La división de {num1} / {num2} es: {resultado}");
                break;
            default:
                Console.WriteLine("Opción no válida");
                break;
        }
    }
}