package Scripts;

class Teacher {
    String designation = "Teacher";
    String college = "Beginnersbook";
    void does(){
     System.out.println("Teaching");
    }
 }
 public class inheritanceExample extends Teacher{
    String mainSubject = "Maths";
    public static void main(String args[]){
        inheritanceExample obj = new inheritanceExample();
       System.out.println(obj.college);
       System.out.println(obj.designation);
       System.out.println(obj.mainSubject);
       obj.does();
    }
 }
 