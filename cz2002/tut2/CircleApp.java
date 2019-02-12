import java.util.Scanner;

public class CircleApp{
    public static void main(String[] args){
        System.out.println("==== Circle Computation ====");
        System.out.println("|1. Create a new circle    |");
        System.out.println("|2. Print Area             |");
        System.out.println("|3. Print Circumference    |");
        System.out.println("============================");

        int option = 0;
        Circle circ = new Circle(0);

        while(option != 4){
            System.out.println("Choose option(1-3):");
            Scanner sc = new Scanner(System.in);
            option = sc.nextInt();

            switch(option){
                case 1:
                    System.out.println("Enter the radius to compute the area and circumference");
                    double rad = sc.nextDouble();
                    circ = new Circle(rad);

                    System.out.println("A new circle is created");
                    break;

                case 2:
                    circ.printArea();
                    break;

                case 3:
                    circ.printCircumference();
                    break;

                case 4:
                    System.out.println("Thank you!!");
                    break;
            }
        }
    }
}
