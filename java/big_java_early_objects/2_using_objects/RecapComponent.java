import java.awt.Rectangle;
import javax.swing.JComponent;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Point2D;
import java.awt.geom.Line2D;
import java.awt.Color;
import java.awt.Font;       //To change the font & font size, you must use a font object.

public class RecapComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Draw the shapes.
        Rectangle rect = new Rectangle(10, 10, 35, 100);
        Ellipse2D.Double ellipse = new Ellipse2D.Double(45, 45, 30, 80);
        Point2D.Double from = new Point2D.Double(100, 100);
        Point2D.Double to = new Point2D.Double(180, 180);
        Line2D.Double line = new Line2D.Double(from, to);

        //Adding colors.
        Color rectColor = Color.GREEN;
        g2.setColor(rectColor);

        //Changing the font.
        Font font = new Font("Serif", Font.PLAIN, 36);
        g2.setFont(font);

        //Add the shapes to the component.
        g2.fill(rect);
        g2.setColor(Color.BLACK);
        g2.draw(ellipse);
        g2.draw(line);
        g2.drawString("Message", 0, 150);
    }
}