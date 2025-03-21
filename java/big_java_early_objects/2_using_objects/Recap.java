import javax.swing.JFrame;
import java.awt.Color;

public class Recap {
    public static void main(String[] args) {
        //Construct a frame.
        JFrame frame = new JFrame();

        //Set the size of the frame.
        frame.setSize(500, 600);

        //Set the title of the frame.
        frame.setTitle("Recapping What I learnt!");

        //Set the default close operation.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Set the color of the frame.
        frame.getContentPane().setBackground(Color.MAGENTA);

        //Add the component to the frame.
        RecapComponent component = new RecapComponent();
        frame.add(component);

        //Make the frame visible.
        frame.setVisible(true);
    }
}