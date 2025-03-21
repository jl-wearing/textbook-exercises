public class TriangleTester {
    public static void main(String[] args) {
        Triangle t = new Triangle(10);
        System.out.printf("Expected answer: %d\n", (10 * 11) / 2);
        System.out.printf("Actual answer: %d\n", t.getArea());
    }
}