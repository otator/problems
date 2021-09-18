juice = 0.2
donut = 2
burger = 10

# the equtions will be 
# 0.2x + 2y + 10z = 200
# x + y + z = 200
# the above equations are two but we have 3 variables 
# so we need to try the numbers of x, y and z until they met the conditions



# from 1 to 198 beacause we need to buy at least 2 items from the other items on the menu
for i in range(1,199):
    for j in range(1,199):
        for k in range(1,199):
            if i+j+k == 200 and 0.2*i + 2*j + k*10 == 200:
                print("jucie: " + str(i) + ", donuts: " + str(j) + ", burgers: " + str(k))

# The solutions are 
# jucie: 120, donuts: 78, burgers: 2
# jucie: 160, donuts: 29, burgers: 11