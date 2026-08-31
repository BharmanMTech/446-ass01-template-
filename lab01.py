import random

area = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

dirty = True

def printGrid():
    print()
    for x in area:
        print(x)


def placeDirt():
    z = random.randrange(3,7)
    for x in range(int(z)):
        x = random.randrange(0,5)
        y = random.randrange(0,5)
        area[y][x] = 1

def placeVacuum():
    x = random.randrange(0,5)
    y = random.randrange(0,5)
    area[y][x] += 2

def checkA():
    
    global dirty

    dirtiness = sum(sum(x) for x in area)
    if(dirtiness > 2):
        pass
    else:
        dirty = False

def checkC():

    for y, sublist in enumerate(area):
        for x, value in enumerate(sublist):
            if (value >= 2):
                
                if (value > 2):
                    area[y][x] -= 1
                elif(value == 2):
                    direction = random.randrange(0,4)

                    if(direction == 0):
                        if y == 0 :
                            continue
                        else:
                            area[y][x] -= 2
                            y -= 1
                            area[y][x] += 2 
                            

                    elif(direction == 1):
                        if y == 4 :
                            continue
                        else:
                            area[y][x] -= 2
                            y += 1
                            area[y][x] += 2 
                            

                    elif(direction == 2):
                        if x == 0 :
                            continue
                        else:
                            area[y][x] -= 2
                            x -= 1
                            area[y][x] += 2 
                            

                    elif(direction == 3):
                        if x == 4 :
                            continue
                        else:
                            area[y][x] -= 2
                            x += 1
                            area[y][x] += 2 
                            

def main():
    placeDirt()
    placeVacuum()
    printGrid()

    #for x in range(10):
    while dirty == True:
        
        checkA()
        checkC()
        printGrid()


if __name__ == "__main__":
    main()

# Brock Harman
# CSCI 446 Fall 2026
# Programming Assignment #1
# I declare that I am the author of this work, take full responsibility for it, and have disclosed any material external assistance.
# I used the google ai overview to help write the dirtiness check in checkA and the enumerate search in checkC
# I used w3school to the check the purpose of multiple functions used in the program.