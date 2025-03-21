import java.awt.Rectangle;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class TranslateDemo {
    public static void main(String[] args) {
        //Construct a frame and show it.
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);


        //Construct a rectangle and set the frame bounds.
        Rectangle rect = new Rectangle(150, 150, 300, 100);
        frame.setBounds(rect);

        JOptionPane.showMessageDialog(frame, "Click OK to continue!");

        //Move the rectangle and set the frame bounds again.
        rect.translate(-75, -75);
        frame.setBounds(rect);
    }
}