import javax.swing.JFrame;

public class FrameViewer {
    public static void main(String[] args) {
        //1. Create a frame object.
        JFrame frame = new JFrame();

        //2. Set the dimensions of the frame.
        frame.setSize(300, 400);

        //3. Set the title of the frame.
        frame.setTitle("An empty title");

        //4. Set the default close operation.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //5. Make the frame visible.
        frame.setVisible(true);
    }
}

/*
Swing is the graphical user interface library in Java.
The x in javax denotes that Swing started off as a java extension before it was incorporated into the java library.
*/