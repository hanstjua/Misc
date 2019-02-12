import java.util.Random;

public class Dice{
    private int valueOfDice;

    public Dice(){
        this.valueOfDice=0;
    }

    public void setDiceValue(){
        Random rand = new Random();
        this.valueOfDice = rand.nextInt(6) + 1;
    }

    public int getDiceValue(){
        return this.valueOfDice;
    }

    public void printDiceValue(){
        System.out.println("Current Value is " + this.getDiceValue());
    }
}

// Note 1: May consider using Math.random() instead since it's a static method and requires no object to be created prior to usage //
