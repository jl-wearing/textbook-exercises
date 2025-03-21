public class HollePrinter {
    public static void main(String[] args) {
        String greeting = "Hello, World!";
        greeting = greeting.replace("e", "z");
        greeting = greeting.replace("o", "e");
        greeting = greeting.replace("z", "o");
        
        //Output
        System.out.println(greeting);
    }
}