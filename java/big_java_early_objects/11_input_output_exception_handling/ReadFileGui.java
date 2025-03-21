import javax.swing.JFileChooser;
import java.io.File;
import java.io.PrintWriter;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class ReadFileGui {
    public static void main(String[] args) throws FileNotFoundException {
        JFileChooser chooser = new JFileChooser();
        Scanner in = null;
        if(chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
            File inFile = chooser.getSelectedFile();
            in = new Scanner(inFile);

            PrintWriter out = new PrintWriter("guiread.txt");
            while(in.hasNext()) {
                out.printf("%s%n", in.nextLine());
            }

            in.close();
            out.close();
        }
        else {
            System.out.printf("Cancelled!");
        }
    }
}