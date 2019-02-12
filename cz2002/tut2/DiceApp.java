import java.util.Scanner;

public class DiceApp{
    public static void main(String[] args){
        int value1 = 0;
        int value2 = 0;
        Dice d = new Dice();
        Scanner sc = new Scanner(System.in);
        int key;
        
        System.out.println("Press <key> to roll the first dice");
        key = sc.nextInt();
        d.setDiceValue();
        value1 = d.getDiceValue();
        d.printDiceValue();

        System.out.println("Press <key> to roll the second dice");
        key = sc.nextInt();
        d.setDiceValue();
        value2 = d.getDiceValue();
        d.printDiceValue();

        int total = value1 + value2;

        System.out.println("Your total number is: " + total);
        
    }
}
