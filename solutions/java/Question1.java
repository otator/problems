package solutions.java;
public class Question1{
  public static void main(String[] args){

    // double juice = 0.2;
    // int donut = 2;
    // int burger = 10;
    // the equtions will be 
    // 0.2x + 2y + 10z = 200
    // x + y + z = 200
    // the above equations are two but we have 3 variables 
    // so we need to try the numbers of x, y and z until they met the conditions



    // from 1 to 198 beacause we need to buy at least 2 items from the other items on the menu
    for(int i=1; i<=198; i++){
      for(int j=1; j<=198; j++){
          for(int k=1; k<=198; k++){
              if(i+j+k == 200 && 0.2*i + 2*j + k*10 == 200)
                  System.out.println("jucie: " + i + ", donuts: " + j + ", burgers: " + k);
          }
      }
    }
              

    // The solutions are 
    // jucie: 120, donuts: 78, burgers: 2
    // jucie: 160, donuts: 29, burgers: 11
  

  }
}