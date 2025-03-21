import javax.swing.JFrame;

public class ShapeViewer {
    public static void main(String[] args) {
        //Construct a frame.
        JFrame frame = new JFrame();

        //Set the size of the frame.
        frame.setSize(300, 400);

        //Set the title of the frame.
        frame.setTitle("Green");

        //Set the default close operation.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Add the component to the frame.
        ShapeComponent component = new ShapeComponent();
        frame.add(component);

        //Make the frame visible.
        frame.setVisible(true);
    }
}