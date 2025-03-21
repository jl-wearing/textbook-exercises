import java.awt.Color;
import java.awt.Rectangle;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JComponent;

public class ShapeComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Construct the shape.
        Rectangle rect = new Rectangle(50, 50, 50, 90);

        //Add the shape to the component.
        g2.setColor(Color.GREEN);
        g2.fill(rect);

        rect.translate(50, 50);
        g2.setColor(Color.RED);
        g2.draw(rect);
    }
}