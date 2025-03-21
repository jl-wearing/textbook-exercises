import java.util.Random;

public class LotteryPicker {
    public static void main(String[] args) {
        Random rand = new Random();

        //Represent the lottery numbers.
        int[] numbers = new int[6];

        //Generate lottery numbers.
        //Lottery numbers range from 1 to 49 inclusive.
        for(int i = 0; i < numbers.length; i++) {
            numbers[i] = rand.nextInt(49) + 1;
        }

        System.out.printf("Play this combination - it'll make you rich: \n");
        for(int i = 0; i < numbers.length; i++) {
            System.out.printf("%d ", numbers[i]);
        }
        System.out.println();
    }
}