import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import javax.swing.JFileChooser;
import java.util.StringTokenizer;

public class Population {
    public static void main(String[] args) throws FileNotFoundException {
        //Input.
        JFileChooser chooser = new JFileChooser();
        Scanner file = null;

        if(chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
            File doc = chooser.getSelectedFile();
            file = new Scanner(doc);
        }
        else {
            System.out.printf("Cancelled!\n");
        }

        //Process.
        while(file.hasNextLine()) {
            StringTokenizer line = new StringTokenizer(file.nextLine());

            //Build the country name.
            String country = "";
            int population = 0;
            while(line.hasMoreTokens()) {
                String st = line.nextToken();
                
                if(!Character.isDigit(st.charAt(0))) {
                    country = country + " " + st;
                }
                else {
                    population = Integer.parseInt(st);
                }
            }
            System.out.printf("Country: %s, Population: %d\n", country, population);
        }
    }
}