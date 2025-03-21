//Testing the implementation of the Counter Class.

public class CounterTester {
    public static void main(String[] args) {
        Counter c1 = new Counter();
        Counter c2 = new Counter(5);

        System.out.println(c1.getCount());
        System.out.println(c2.getCount());
        System.out.println();

        c1.click();
        c1.click();
        c2.click();
        System.out.println(c1.getCount());
        System.out.println(c2.getCount());
        System.out.println();

        c2.reset();
        c1.undo();
        System.out.println(c1.getCount());
        System.out.println(c2.getCount());
        System.out.println();

        Counter c3 = new Counter(2);
        System.out.println(c3.getCount());
        c3.undo();
        System.out.println(c3.getCount());
        c3.undo();
        System.out.println(c3.getCount());
        c3.undo();
        System.out.println(c3.getCount());
        c3.undo();
        System.out.println(c3.getCount());
    }
}