import java.awt.Rectangle;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JOptionPane;
import javax.swing.JComponent;

public class RectComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Get the dimensions & coordinates for a Rectangle.
        JOptionPane.showMessageDialog(null, "Enter the coordinates & dimensions for the rectangle, OK!", "Drawing Rectangles", 0);
        int x = Integer.parseInt(JOptionPane.showInputDialog("Enter the x coordinate: "));
        int y = Integer.parseInt(JOptionPane.showInputDialog("Enter the y coordinate: "));
        int width = Integer.parseInt(JOptionPane.showInputDialog("Enter the width: "));
        int height = Integer.parseInt(JOptionPane.showInputDialog("Enter the height: "));

        //Construct the Rectangle.
        Rectangle rect = new Rectangle(x, y, width, height);

        //Draw the rectangle.
        g2.draw(rect);
    }
}