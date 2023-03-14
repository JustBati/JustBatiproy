internal class Program
{
    private static void Main(string[] args)
    {
        // Primer paso 
        //Hola mundo
        Console.WriteLine("Hello, World!");
        // Segundo paso 
        //Variables y uso de ellas para impresion en consola
        string Name = "Jenny Rivera";
        Console.WriteLine($"\tUna artista famosa de banda mexicna fue: {Name}");

        //Tercer paso
        //Uso de metodos
        string Text1 = "En esta parte probamos la concatenacion de cadenas mediante la utilidad de Console.WriteLine";
        Console.WriteLine($"{Text1}\n como a su vez el texto anterior tiene un total de {Text1.Length}");

        string Text2 = "[     Aqui tenemos un texto con multiples espacios a la izquierda y la derecha        ]";
        Console.WriteLine(Text2);
         
        
        
    }
}
