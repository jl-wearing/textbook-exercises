/*
There are 2 ways to draw lines:
First Method is to use the Line2D.Double class.
Second method is to construct 2 points and pass them as arguments to a Line2D.Double constructor.
 */

import java.awt.geom.Line2D;
import java.awt.geom.Point2D;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JComponent;

public class LineComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Draw the lines.
        Line2D.Double line1 = new Line2D.Double(10, 10, 69, 69);    //First method.

        //Second method:
        Point2D.Double from = new Point2D.Double(40, 40);
        Point2D.Double to = new Point2D.Double(150, 200);
        Line2D.Double line2 = new Line2D.Double(from, to);

        //Add the lines to the component.
        g2.draw(line1);
        g2.draw(line2);
    }
}