import javax.swing.JFrame;

public class RectangleViewer {
    public static void main(String[] args) {
        //Create a frame
        JFrame frame = new JFrame();

        //Set the dimensions of the frame.
        frame.setSize(300, 400);

        //Set the title of the frame.
        frame.setTitle("My First Drawing");

        //Set the default close operation.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Add the component to the frame.
        RectangleComponent component = new RectangleComponent();
        frame.add(component);

        //Make the frame visible.
        frame.setVisible(true);
    }
}