import javax.swing.JFrame;

public class StringViewer {
    public static void main(String[] args) {
        //Construct a frame.
        JFrame frame = new JFrame();

        //Set the size of the frame.
        frame.setSize(300, 400);

        //Set the title of the frame.
        frame.setTitle("Words on a frame!");

        //Set the default close operation.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Add the component to the frame.
        StringComponent component = new StringComponent();
        frame.add(component);

        //Make the frame visible.
        frame.setVisible(true);
    }
}