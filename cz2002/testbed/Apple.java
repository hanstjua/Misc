public class Apple extends Fruit{
    public Apple(){
        super("red","sweet-sour",0.0);
    }

    public Apple(double mass){
        super("red","sweet-sour", mass);
    }

    public void bite(){
        System.out.println("Crunch");
    }
}
