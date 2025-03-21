import java.awt.Rectangle;

public class ObjectConstruction {
    public static void main(String[] args) {

        //Constructor.
        Rectangle box = new Rectangle(5, 5, 20, 30);
        System.out.println(box.toString());

        //An accessor method accesses the data of an object without modifying the object.
        System.out.println(box.getX());
        System.out.println(box.getY());
        System.out.println(box.getWidth());
        System.out.println(box.getHeight());

        //A mutator method alters the internal state of an object.
        System.out.println();
        box.translate(10, 10);
        System.out.println(box);

        //The setSize() methods alters the width and height of a rectangle.
        box.setSize(50, 100);
        System.out.println();
        System.out.println(box.toString());

        //setLocation() alters the x & y coordinates of a rectangle.
        System.out.println();
        box.setLocation(0, 0);
        System.out.println(box.toString());
    }
}

/*
 * Accessor methods of the Rectangle class:
 * getX(), getY(), getWidth(), getHeight()
 * 
 * Mutator methods of the Rectangle class:
 * translate(), setSize(), setLocation()
 */

//The API lists the classes & methods of the Java library.
//A package is a collection of classes with a related purpose.
//The Rectangle class belongs to the jawa.awt package - awt stands for abstract windowing toolkit which contains classes for drawing windows and graphical shapes.
//To use the Rectangle class, you must import its package.