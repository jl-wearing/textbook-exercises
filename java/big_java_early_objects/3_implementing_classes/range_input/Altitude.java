//Simulating allowable altitude levels in an aircraft.

public class Altitude {
    public static void main(String[] args) {
        RangeInput autoPilot = new RangeInput(32_000, 32_500);

        System.out.printf("Current Altitude: %d\n", autoPilot.getValue());

        //Testing the ceiling.
        for(int i = 0; i < 251; i++) {
            autoPilot.up();

            if(autoPilot.getValue() >= autoPilot.maxValue()) {
                System.out.printf("Too High! Descending to allowable altitude levels!\n");
            }
        }

        //Testing the floor.
        for(int i = 0; i < 501; i++) {
            autoPilot.down();

            if(autoPilot.getValue() <= autoPilot.minValue()) {
                System.out.printf("WOOP! WOOP! PULL UP!\n");
            }
        }
    }


}