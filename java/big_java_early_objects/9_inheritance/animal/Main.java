public class Main {
    public static void main(String[] args) {
        Animal one = new Animal();
        Animal two = new Dog();
        Animal three = new Cat();

        one.makeSound();
        two.makeSound();
        three.makeSound();
    }
}

/*
This example raises an important point:
The implementation of the method that executes is determined by the
type of the object itself, and not the type of the variable that references
the object.
 */