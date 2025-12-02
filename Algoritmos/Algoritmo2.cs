using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Ingrese la primera cadena:");
        string cadena1 = Console.ReadLine();

        Console.WriteLine("Ingrese la segunda cadena:");
        string cadena2 = Console.ReadLine();

        bool esPalindromo1 = EsPalindromo(cadena1);
        bool esPalindromo2 = EsPalindromo(cadena2);

        Console.WriteLine($"\n¿\"{cadena1}\" es palíndromo? {esPalindromo1}");
        Console.WriteLine($"¿\"{cadena2}\" es palíndromo? {esPalindromo2}");

        if (esPalindromo1 && esPalindromo2
        {
            Console.WriteLine("\nAmbas cadenas son palíndromos.");
        }
        else if (esPalindromo1 || esPalindromo2)
        {
            Console.WriteLine("\nSolo una de las cadenas es palíndromo.");
        }
        else
        {
            Console.WriteLine("\nNinguna de las cadenas es palíndromo.");
        }
    }

    static bool EsPalindromo(string texto)
    {
        // Eliminamos espacios y convertimos a minúsculas
        string limpio = texto.Replace(" ", "").ToLower();

        // Invertimos la cadena
        char[] arreglo = limpio.ToCharArray();
        Array.Reverse(arreglo);
        string invertido = new string(arreglo);

        // Comparamos
        return limpio == invertido;
    }
}
