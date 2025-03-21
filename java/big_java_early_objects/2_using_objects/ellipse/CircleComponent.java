import java.awt.geom.Ellipse2D;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JComponent;

public class CircleComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Construct a circle.
        Ellipse2D.Double circle = new Ellipse2D.Double(50, 50, 69, 69);

        //Add the circle to the frame.
        g2.draw(circle);
    }
}