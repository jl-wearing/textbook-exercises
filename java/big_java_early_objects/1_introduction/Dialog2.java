import javax.swing.JOptionPane;

public class Dialog2{
    public static void main(String[] args){
        String name = JOptionPane.showInputDialog("What is your name?");
        System.out.println(name);
    }
}