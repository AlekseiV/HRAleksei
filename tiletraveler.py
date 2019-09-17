#Start æltum að byrja að búa til grid af 3x3 og gefa tækifæðrið til að færa sig S fyrir suður W Vestur N fyrir norður og E fyrir austur og hann færist um einn eftir því hvað er valið
#markmiðið verður að komast að leiðarenda í forritinu til að vinna leikin

x = 1
y = 1

valid_direction = "nN"
last_tile = False
print("You can travel: (N)orth.")

position = (x,y)

while not last_tile:
    direction = input("Direction: ")
    if not direction in valid_direction: 
        print("Not a valid direction!")
    else:
        if direction == "N" or direction == "n":
            y += 1
            position = (x, y)
            if position == (1, 1) or position == (2, 1):
                valid_direction = "nN" 
                print("You can travel: (N)orth.")
            elif position == (1, 2):
                valid_direction= "nNeEsS"
                print("You can travel: (N)orth or (E)ast or (S)outh.")
            elif position == (1, 3):
                valid_direction= "eEsS" 
                print("You can travel: (E)ast or (S)outh.")
            elif position == (2, 1):
                valid_direction= "nN" 
                print("You can travel: (N)orth.")
            elif position == (2, 2) or position == (3, 3):
                valid_direction= "wWsS"
                print("You can travel: (S)outh or (W)est.")
            elif position == (2, 3): 
                valid_direction= "eEwW"
                print("You can travel: (E)ast or (W)est.")
            elif position == (3, 1):
                print("Victory!")
                last_tile = True
            elif position == (3, 2):
                valid_direction= "nNsS" 
                print("You can travel: (N)orth or (S)outh.")
            elif position == (3, 3):
                valid_direction= "sSwW"
                print("You can travel: (S)outh or (W)est.")

        elif direction == "S" or direction == "s":
            y -= 1
            position = (x, y)
            if position == (1, 1):
                valid_direction = "nN" 
                print("You can travel: (N)orth.")
            elif position == (1, 2):
                valid_direction= "nNeEsS"
                print("You can travel: (N)orth or (E)ast or (S)outh.")
            elif position == (1, 3):
                valid_direction= "eEsS" 
                print("You can travel: (E)ast or (S)outh.")
            elif position == (2, 1):
                valid_direction= "nN" 
                print("You can travel: (N)orth.")
            elif position == (2, 2):
                valid_direction= "wWsS"
                print("You can travel: (S)outh or (W)est.")
            elif position == (2, 3): 
                valid_direction= "eEwW"
                print("You can travel: (E)ast or (W)est.")
            elif position == (3, 1):
                print("Victory!")
                last_tile = True
            elif position == (3, 2):
                valid_direction= "nNsS" 
                print("You can travel: (N)orth or (S)outh.")
            elif position == (3, 3):
                valid_direction= "sSwW"
                print("You can travel: (S)outh or (W)est.")
                
        elif direction == "E" or direction == "e":
            x += 1
            position = (x,y)
            if position == (1, 1):
                valid_direction = "nN" 
                print("You can travel: (N)orth.")
            elif position == (1, 2):
                valid_direction= "nNeEsS"
                print("You can travel: (N)orth or (E)ast or (S)outh.")
            elif position == (1, 3):
                valid_direction= "eEsS" 
                print("You can travel: (E)ast or (S)outh.")
            elif position == (2, 1):
                valid_direction= "nN" 
                print("You can travel: (N)orth.")
            elif position == (2, 2):
                valid_direction= "wWsS"
                print("You can travel: (S)outh or (W)est.")
            elif position == (2, 3): 
                valid_direction= "eEwW"
                print("You can travel: (E)ast or (W)est.")
            elif position == (3, 1):
                print("Victory!")
                last_tile = True
            elif position == (3, 2):
                valid_direction= "nNsS" 
                print("You can travel: (N)orth or (S)outh.")
            elif position == (3, 3):
                valid_direction= "sSwW"
                print("You can travel: (S)outh or (W)est.")