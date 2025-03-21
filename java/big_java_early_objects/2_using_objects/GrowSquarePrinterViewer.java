import javax.swing.JFrame;
import java.awt.Color;

public class GrowSquarePrinterViewer {
    public static void main(String[] args) {
        //Construct a frame.
        JFrame frame = new JFrame();

        //Set the size of the frame.
        frame.setSize(300, 400);

        //Set the title of the frame.
        frame.setTitle("Two Squares!");

        //Set the default close operation.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Set the background color of the frame.
        Color bgColor = Color.BLACK;
        frame.getContentPane().setBackground(bgColor);

        //Add the component to the frame.
        GrowSquarePrinterComponent component = new GrowSquarePrinterComponent();
        frame.add(component);

        //Make the frame visible.
        frame.setVisible(true);
    }
}