import java.awt.Color;
import javax.swing.JFrame;

public class CenteredSquareViewer {
    public static void main(String[] args) {
        //Construct a frame.
        JFrame frame = new JFrame();

        //Set the size of the frame.
        frame.setSize(300, 400);

        //Set the title of the frame.
        frame.setTitle("Centered Squares");

        //Set the background color of the frame.
        Color bgColor = Color.BLACK;
        frame.getContentPane().setBackground(bgColor);

        //Set the default close operation.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Add the component to the frame.
        CenteredSquareComponent component = new CenteredSquareComponent();
        frame.add(component);

        //Make the frame visible.
        frame.setVisible(true);
    }
}