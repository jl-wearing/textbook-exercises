/*
To draw an ellipse, you specify its bounding box.
i.e. - You specify the x & y coordinates of the top left corner, the width and height of the bounding box.
You must use either the Ellipse2D.Float or Ellipse2D.Double classes to construct Ellipse objects.
e.g. - Ellipse2D.Double means Double is an inner class inside the Ellipse2D class.
NOTE: - You only include the outer class in the import statement.

To draw a circle, simply set the width and height to be the same.
 */

import java.awt.geom.Ellipse2D;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JComponent;

public class EllipseComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Construct an ellipse.
        Ellipse2D.Double drawing = new Ellipse2D.Double(50, 50, 100, 60);

        //Add the ellipse to the component.
        g2.draw(drawing);
    }
}