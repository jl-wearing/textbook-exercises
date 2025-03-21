import javax.swing.JFileChooser;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class PopulationEfficient {
    public static void main(String[] args) throws FileNotFoundException {
        JFileChooser chooser = new JFileChooser();

        Scanner in = null;
        if(chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
            File file = chooser.getSelectedFile();
            in = new Scanner(file);
        }

        while(in.hasNextLine()) {
            String line = in.nextLine();

            int i = 0;
            while(!Character.isDigit(line.charAt(i))) { i++;}

            String country = line.substring(0 , i).trim();
            int population = Integer.parseInt(line.substring(i));
            System.out.printf("%s, %d\n",country, population);
        }
    }
}