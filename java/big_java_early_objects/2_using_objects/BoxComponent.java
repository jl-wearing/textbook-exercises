import java.awt.geom.Line2D;
import java.awt.Rectangle;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JComponent;

public class BoxComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Draw the shapes.
        Rectangle r1 = new Rectangle(20, 20, 40, 100);
        Rectangle r2 = new Rectangle(40, 70, 40, 100);      //I could also use the translate() method.
        Line2D.Double topLeft = new Line2D.Double(20, 20, 40, 70);
        Line2D.Double topRight = new Line2D.Double(60, 20, 80, 70);
        Line2D.Double bottomLeft = new Line2D.Double(20, 120, 40, 170);
        Line2D.Double bottomRight = new Line2D.Double(60, 120, 80, 170);

        //Add the shapes to the component.
        g2.draw(r1);
        g2.draw(r2);
        g2.draw(topLeft);
        g2.draw(topRight);
        g2.draw(bottomRight);
        g2.draw(bottomLeft);
    }
}