import javax.swing.JFileChooser;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class PopEff2 {
    public static void main(String[] args) throws FileNotFoundException {
        JFileChooser chooser = new JFileChooser();

        Scanner in = null;
        if(chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
            File file = chooser.getSelectedFile();
            in = new Scanner(file);
        }

        while(in != null && in.hasNextLine()) {
            String line = in.nextLine();
            Scanner lineScanner = new Scanner(line);

            String country = "";
            while(!lineScanner.hasNextInt()) {
                country = country + " " + lineScanner.next();
            }
            int population = lineScanner.nextInt();
            lineScanner.close();

            System.out.printf("%s, %d\n", country, population);
        }
    }
}