#problem 1:
cookies = int(input("how mant cookies ya got? : "))
if cookies < 3:
    print("man you dont got enough cookies. you broke person.")
elif cookies < 10:
    print("you got a decent amount ig...")
elif cookies >= 10:
    print("you got too many damn, give yourself the kanye treatment (but don't be racist, homophobic, etc) and lose a lot of it in a week...")

#problem 2: 
jedi = input("Are you a jedi or a sith?: ")
if jedi == "jedi":
    print("you get a green lightsaber")
elif jedi == "sith":
    print("heres a red lightsaber!")
else:
    print("you get a breadstick")
 
 
#problem 3:
for i in range (4, 41, 2):
    print(i, end =" ")
print(" ")

#past this point is what I retook-------------------------------

#problem 4:
ballin = 20
while (ballin < 60):
    ballin = ballin + 2
    print(ballin)

#problem 5:
doExit = False
while doExit == False:
    password = input("ring ring...")
    if password == "hello?":
        doExit = True
        print("we've been trying to reach you about your cars extended warranty!")
    else:
        print("line disconnected.")

#problem 6:
def mathy(a, b, c, d):
    return a+b-c+d

print(mathy(10, 20, 30, 40))

#problem 7: 
def LeafFall(p):
    num = 0
    while num <= p:
        print(num, "leaves fell!!")
        num += 10
        
leaf = int(input("how many times do you want to shake a tree?"))
LeafFall(leaf)

