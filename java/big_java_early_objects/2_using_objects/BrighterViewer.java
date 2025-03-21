import javax.swing.JFrame;
import java.awt.Color;

public class BrighterViewer {
    public static void main(String[] args) {
        //Construct a frame.
        JFrame frame = new JFrame();

        //Set the size of the frame.
        frame.setSize(400, 500);

        //Set the title of the frame.
        frame.setTitle("Color Testing");

        //Set the color of the frame.
        Color color = Color.BLACK;
        frame.getContentPane().setBackground(color);

        //Set the default close operation.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Add the component to the frame.
        BrighterComponent component = new BrighterComponent();
        frame.add(component);

        //Make the frame visible.
        frame.setVisible(true);
    }
}