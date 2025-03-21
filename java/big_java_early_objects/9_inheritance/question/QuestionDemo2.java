import java.util.Scanner;

public class QuestionDemo2 {
    public static void main(String[] args) {
        ChoiceQuestion first = new ChoiceQuestion();
        first.setText("What was the original name of the Java language?");
        first.addChoice("Python", false);
        first.addChoice("Duke", false);
        first.addChoice("Oak", true);
        first.addChoice("Gosling", false);

        ChoiceQuestion second = new ChoiceQuestion();
        second.setText("In which country was the inventor of Java born?");
        second.addChoice("Australia", false);
        second.addChoice("Canada", true);
        second.addChoice("Denmark", false);
        second.addChoice("United States", false);

        presentQuestion(first);
        presentQuestion(second);
    }

    public static void presentQuestion(ChoiceQuestion q) {
        q.display();
        Scanner console = new Scanner(System.in);
        String response = console.nextLine().toLowerCase();
        
        if(q.checkAnswer(response)) {
            System.out.println("Correct!");
        }
        else {
            System.out.println("Incorrect!");
        }
    }
}