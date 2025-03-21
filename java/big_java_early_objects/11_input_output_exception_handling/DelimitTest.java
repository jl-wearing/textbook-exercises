import java.util.Scanner;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

public class DelimitTest {
    public static void main(String[] args) throws FileNotFoundException {
        //Input.
        Scanner console = new Scanner(System.in);
        System.out.printf("Enter the input filename: ");
        String input = console.next();
        System.out.printf("\nEnter the output filename: ");
        String output = console.next();
        console.close();

        //Process.
        Scanner file = new Scanner(new File(input));
        file.useDelimiter("[^A-Za-z0-9]");
        PrintWriter toFile = new PrintWriter(output);

        while(file.hasNext()) {
            String name = file.next();
            String occupation = file.next();
            int age = file.nextInt();

            //Output.
            toFile.printf("%s\t%s\t%d%n", name, occupation, age);
        }

        //Close the Scanner & PrintWriter.
        file.close();
        toFile.close();
    }
}