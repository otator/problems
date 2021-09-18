// var juice = 0.2;
// var donut = 2;
// var burger = 10;


// the equtions will be 
// 0.2x + 2y + 10z = 200
// x + y + z = 200
// the above equations are two but we have 3 variables 
// so we need to try the numbers of x, y and z until they met the conditions



// from 1 to 198 beacause we need to buy at least 2 items from the other items on the menu
for(let i=1; i<=198; i++){
    for(let j=1; j<=198; j++){
        for(let k=1; k<=198; k++){
            if(i+j+k == 200 && 0.2*i + 2*j + k*10 == 200)
                console.log("jucie: " + i + ", donuts: " + j + ", burgers: " + k);
        }
    }
}
            

// The solutions are 
// jucie: 120, donuts: 78, burgers: 2
// jucie: 160, donuts: 29, burgers: 11