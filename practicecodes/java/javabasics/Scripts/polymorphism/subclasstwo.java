package Scripts.polymorphism;

public class subclasstwo  extends subclass{
    private double fee = 0.99;


    public double getPrise()
    {
        return super.getPrise() + fee;
    }
    
}
