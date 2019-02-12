public abstract class Fruit{
    private static int totalFruit = 0;

    protected String color;
    protected String taste;
    protected double mass;

    public Fruit(){
        this.color = "NA";
        this.taste = "NA";
        this.mass = 0.0;
        totalFruit++;
    }

    public Fruit(String color, String taste, double mass){
        this.color = color;
        this.taste = taste;
        this.mass = mass;
        totalFruit++;
    }

    public void getTotalFruit(){
        System.out.println("Total number of fruits: " + this.totalFruit);
    }

    public abstract void bite();
}
