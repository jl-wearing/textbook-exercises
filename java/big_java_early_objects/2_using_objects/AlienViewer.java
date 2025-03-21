import javax.swing.JFrame;

public class AlienViewer {
    public static void main(String[] args) {
        //Construct a frame.
        JFrame frame = new JFrame();

        //Set the size of the frame.
        frame.setSize(200, 200);

        //Set the title of the frame.
        frame.setTitle("An Alien");

        //Set the default close operation.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Add the component to the frame.
        AlienComponent component = new AlienComponent();
        frame.add(component);

        //Make the frame visible.
        frame.setVisible(true);
    }
}