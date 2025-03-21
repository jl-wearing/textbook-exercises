import java.net.URL;
import javax.swing.ImageIcon;
import javax.swing.JOptionPane;

public class ImageViewer{
    public static void main(String[] args) throws Exception{
        URL imageLocation = new URL("https://media.gettyimages.com/id/2123386063/photo/lilys-aging-skin.jpg?s=2048x2048&w=gi&k=20&c=xLCWbTRuVMOGJ7kT51qPIph16IUyqfKp8l7hF5EEDO4=");
        JOptionPane.showMessageDialog(null, "Hello", "Title", JOptionPane.PLAIN_MESSAGE, new ImageIcon(imageLocation));
    }
}