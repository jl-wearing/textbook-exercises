import javax.swing.JFrame;

public class EllipseViewer {
    public static void main(String[] args) {
        //Construct a frame.
        JFrame frame = new JFrame();

        //Set the size of the frame.
        frame.setSize(300, 400);

        //Set the title of the frame.
        frame.setTitle("My first Ellipse!");

        //Set the default close operation.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Add the component to the frame.
        EllipseComponent component = new EllipseComponent();
        frame.add(component);

        //Make the frame visible.
        frame.setVisible(true);
    }
}