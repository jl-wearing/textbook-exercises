import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JComponent;
import java.awt.Color;

/*
To draw a string, use the drawString() method of the Graphics2D class.
You must specify the x & y coordinates of the basepoint of the first character in the string.
 */

public class StringComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Draw the string.
        g2.setColor(Color.RED);
        g2.drawString("POOP", 50, 100);
    }
}