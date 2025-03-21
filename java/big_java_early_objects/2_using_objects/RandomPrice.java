import java.util.Random;

public class RandomPrice {
    public static void main(String[] args) {
        Random rand = new Random();

        double minPrice = 10.00;
        double maxPrice = 19.95;
        double result = minPrice + (rand.nextDouble() * (maxPrice - minPrice));
        
        //Output
        System.out.printf("%.2f\n", result);
    }
}