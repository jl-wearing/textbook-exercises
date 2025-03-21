import java.util.Scanner;

public class QuestionDemo3 {
    public static void main(String[] args) {
        Question first = new Question();
        first.setText("Who was the inventor of Java?");
        first.setAnswer("James Gosling");

        ChoiceQuestion second = new ChoiceQuestion();
        second.setText("In which country was the inventor of Java born?");
        second.addChoice("Australia", false);
        second.addChoice("Canada", true);
        second.addChoice("Denmark", false);
        second.addChoice("United States", false);

        presentQuestion(first);
        presentQuestion(second);
    }

    //Dynamic method lookup.
    public static void presentQuestion(Question q) {
        q.display();
        Scanner in = new Scanner(System.in);
        String answer = in.nextLine();

        if(q.checkAnswer(answer)){
            System.out.println("Correct!");
        }
        else {
            System.out.println("Incorrect!");
        }
    }
}