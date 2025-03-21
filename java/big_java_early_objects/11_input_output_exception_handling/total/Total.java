import java.util.Scanner;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

public class Total {
    public static void main(String[] args) throws FileNotFoundException {
        //Input.
        Scanner in = new Scanner(System.in);
        System.out.printf("Enter the input filename: ");
        String input = in.next();
        System.out.printf("\nEnter the output filename: ");
        String output = in.next();

        Scanner inFile = new Scanner(new File(input));      //Read from the file.
        PrintWriter outFile = new PrintWriter(output);      //Write to the file.
        
        //Process.
        double total = 0.0;
        while(inFile.hasNextDouble()) {
            double num = inFile.nextDouble();
            outFile.printf("%15.2f%n", num);
            total = total + num;
        }

        //Output.
        outFile.printf("Total: %8.2f%n", total);

        //Close the File and PrintWriter.
        inFile.close();
        outFile.close();
        in.close();
    }
}