import java.io.IOException;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.net.URL;

public class ReadWebPage {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        String address = "https://horstmann.com/index.html";
        URL pageLocation = new URL(address);

        //Read from webpage.
        Scanner in = new Scanner(pageLocation.openStream());
        PrintWriter outFile = new PrintWriter("horstmann.txt");

        //Process.
        int counter = 0;
        while(counter < 10) {
            outFile.printf("%s%n", in.nextLine());
            counter++;
        }

        //Close the Scanner & PrintWriter.
        in.close();
        outFile.close();
    }
}