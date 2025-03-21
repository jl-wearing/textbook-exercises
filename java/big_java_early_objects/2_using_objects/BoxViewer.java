import javax.swing.JFrame;

public class BoxViewer {
    public static void main(String[] args) {
        //Construct a frame.
        JFrame frame = new JFrame();

        //Set the size of the frame.
        frame.setSize(300, 400);

        //Set the title of the frame.
        frame.setTitle("A box to store goods.");

        //Set the default close operation.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Add the component to the frame.
        BoxComponent component = new BoxComponent();
        frame.add(component);

        //Make the frame visible.
        frame.setVisible(true);
    }
}