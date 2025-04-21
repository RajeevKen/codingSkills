package Scripts.polymorphism;

// public class overridingExp {
    
// }
class Vehicle{  
    //defining a method  
    void run(){System.out.println("Vehicle is moving");}  
  }  
  //Creating a child class  
  class overridingExp extends Vehicle{  
    //defining the same method as in the parent class  
    void run(){System.out.println("car is running safely");}  
    
    public static void main(String args[]){  
        overridingExp obj = new overridingExp();//creating object  
    obj.run();//calling method  
    }  
  }
