import java.util.Calendar;
import java.util.GregorianCalendar;

public class CalTester {
    public static void main(String[] args) {
        //Today's date.
        GregorianCalendar today = new GregorianCalendar();
        
        //Specified date.
        GregorianCalendar myBirthDay = new GregorianCalendar(2024, Calendar.JULY, 19);

        //The add() method is used to add a number of days to a Gregorian calendar object.
        //e.g. to add 10 days: myBirthDay.add(Calendar.DAY_OF_MONTH, 10)

        /*
         * The get() method is used to query a Gregorian calendar object.
         * int dayOfMonth = today.get(Calendar.DAY_OF_MONTH) 
         * int month = today.get(Calendar.MONTH) - 1 = January, 2 = February, ...
         * int year = today.get(Calendar.YEAR)
         * int weekDay = today.get(Calendar.DAY_OF_WEEK) - 1 = Sunday, 2 = Monday, ...
         */
        int dayOfMonth = today.get(Calendar.DAY_OF_MONTH);
        int month = today.get(Calendar.MONTH);
        int year = today.get(Calendar.YEAR);
        int dayOfWeek = today.get(Calendar.DAY_OF_WEEK);

        //Output
        System.out.println(dayOfMonth);
        System.out.println(month);
        System.out.println(year);
        System.out.println(dayOfWeek);
    }
}

/*
 * The GregorianCalendar class describes a point in time, as measured by the Gregorian calendar, the
 * standard calendar that is used throughout the world.
 * 
 * 
 * 
 */