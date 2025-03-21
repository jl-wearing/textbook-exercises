import java.util.ArrayList;

/**
 * A Question with multiple choices.
 */
public class ChoiceQuestion extends Question {
    private ArrayList<String> choices;

    /**
     * Constructs a choice question with no choices.
     */
    public ChoiceQuestion () {
        choices = new ArrayList<String>();
    }

    /**
     * Adds another choice to this question.
     * @param choice the choice to add.
     * @param correct true if this is the correct choice, false otherwise.
     */
    public void addChoice(String choice, boolean correct) {
        choices.add(choice.toLowerCase());

        if(correct) {
            String choiceString = choices.get(choices.size() - 1);
            setAnswer(choiceString);
        }
    }

    /**
     * Displays the question along with its choices.
     */
    public void display() {
        //Display the question text.
        super.display();

        //Display the possible choices.
        char possibleChoice = 'a';
        for(int i = 0; i < choices.size(); i++){
            System.out.printf("%c.) %s\n", possibleChoice, choices.get(i));
            possibleChoice++;
        }
    }
}