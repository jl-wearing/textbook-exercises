import javax.swing.JFrame;
import java.awt.Color;

public class CarViewer {
    public static void main(String[] args) {
        //Construct a frame.
        JFrame frame = new JFrame();

        //Set the dimensions of the frame.
        frame.setSize(400, 500);

        //Set the title of the frame.
        frame.setTitle("Two Cars");

        //Set the default close operation.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Set the background color of the frame.
        frame.getContentPane().setBackground(Color.MAGENTA);

        //Add the component to the frame.
        CarComponent component = new CarComponent();
        frame.add(component);

        //Make the frame visible.
        frame.setVisible(true);
    }
}