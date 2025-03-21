//Simulating an airconditioner dile using the RangeInput class.

public class AirConditioner {
    public static void main(String[] args) {
        RangeInput airconRange = new RangeInput(10, 25);
        
        //Increase the temperature.
        airconRange.up();
        airconRange.up();

        //Get the current temperature.
        System.out.println(airconRange.getValue());
        System.out.println();

        //Decrease the temperature by 5 degrees celsius.
        for(int i = 0; i < 5; i++) { airconRange.down(); }

        //Get the current temperature.
        System.out.println(airconRange.getValue());
        System.out.println();

        //Testing the min and max ranges.
        RangeInput test = new RangeInput(10, 20);
        //Attempt to decrease the range below 10.
        for(int i = 0; i < 10; i++) {
            System.out.println(test.getValue());
            test.down();
        }
        System.out.println();
        //Attempt to increase the range above 20.
        for(int i = 0; i < 15; i++) {
            System.out.println(test.getValue());
            test.up();
        }
        System.out.println();
    }
}