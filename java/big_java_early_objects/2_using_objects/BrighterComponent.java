import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.Color;
import javax.swing.JComponent;

public class BrighterComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Construct a rectangle.
        Rectangle rect = new Rectangle(0, 0, 150, 90);

        //Add the shape to the component.
        Color color = new Color(50, 100, 150);
        g2.setColor(color);
        g2.fill(rect);

        rect.translate(150, 150);
        color = color.brighter();

        //Add the shape to the component.
        g2.setColor(color);
        g2.fill(rect);
    }
}