import java.util.Random;

public class DieSimulator {
    public static void main(String[] args) {
        Random rand = new Random();

        //Simulating 10 die rolls.
        for(int i = 1; i <= 10; i++) {
            int num = rand.nextInt(6) + 1;
            System.out.printf("Die roll %d: %d\n", i, num);
        }
    }
}