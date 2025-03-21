import java.util.GregorianCalendar;
import java.util.Calendar;

public class GregorianExercise {
    public static void main(String[] args) {
        //Today's date.
        GregorianCalendar today = new GregorianCalendar();

        //Output the date that is 100 days from today.
        today.add(Calendar.DAY_OF_MONTH, 100);
        System.out.printf("Date 100 days from today: %s %d, %s, %d.\n", getDayOfWeek(today), today.get(Calendar.DAY_OF_MONTH), getMonth(today), today.get(Calendar.YEAR));

        //My birthday.
        GregorianCalendar myBirthDay = new GregorianCalendar(2024, Calendar.JULY, 19);
        //Output the weekday of my birthday.
        System.out.printf("The day of my birth will be a: %s.\n", getDayOfWeek(myBirthDay));

        //Output the date 10_000 days from my birthday.
        myBirthDay.add(Calendar.DAY_OF_MONTH, 10_000);
        System.out.printf("The date 10_000 days from my birthday: %s %d %s %d\n", getDayOfWeek(myBirthDay), myBirthDay.get(Calendar.DAY_OF_MONTH), getMonth(myBirthDay), myBirthDay.get(Calendar.YEAR));
    }

    public static String getDayOfWeek(GregorianCalendar cal) {
        int dayOfWeek = cal.get(Calendar.DAY_OF_WEEK);

        switch (dayOfWeek) {
            case 1:
                return "Sunday";
            case 2:
                return "Monday";
            case 3:
                return "Tuesday";
            case 4:
                return "Wednesday";
            case 5:
                return "Thursday";
            case 6:
                return "Friday";
            case 7:
                return "Saturday";
        }
        return "Invalid Data!";
    }

    public static String getMonth(GregorianCalendar cal) {
        int month = cal.get(Calendar.MONTH);

        switch (month) {
            case 1:
                return "January";
            case 2:
                return "February";
            case 3:
                return "March";
            case 4:
                return "April";
            case 5:
                return "May";
            case 6:
                return "June";
            case 7:
                return "July";
            case 8:
                return "August";
            case 9:
                return "September";
            case 10:
                return "October";
            case 11:
                return "November";
            case 12:
                return "December";
        }

        return "Invalid Data!";
    }
}