import javax.swing.JComponent;
import java.awt.Graphics;
import java.awt.Graphics2D;

public class CarComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Construct a Car shape.
        Car car1 = new Car(0, 0);       //Top left corner.

        int xBottomLeft = getWidth() - 60;
        int yBottomLeft = getHeight() - 30;
        Car car2 = new Car(xBottomLeft, yBottomLeft);

        //Add the Car to the component.
        car1.draw(g2);
        car2.draw(g2);
    }
}