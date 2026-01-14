import time
import random
from inputimeout import inputimeout, TimeoutOccurred
import os

game_start_time = time.time()
player_health = 250
potion = 0
monster_health = 300
player_attack = 50
names = ["Dragon", "Ogre", "Vampire", "Zombie", "Skeleton"]


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


print(
    "Hi! Welcome to your nightmare. Are you ready to venture into the dark and scary mansion?"
)
print("""                                                                      
                                               /\      /\
                                               ||______||
                                               || ^  ^ ||
                                               \| |  | |/
                                                |______|
              __                                |  __  |
             /  \       ________________________|_/  \_|__
            / ^^ \     /=========================/ ^^ \===|
           /  []  \   /=========================/  []  \==|
          /________\ /=========================/________\=|
       *  |        |/==========================|        |=|
      *** | ^^  ^^ |---------------------------| ^^  ^^ |--
     *****| []  [] |           _____           | []  [] | |
    *******        |          /_____\          |      * | |
   *********^^  ^^ |  ^^  ^^  |  |  |  ^^  ^^  |     ***| |
  ***********]  [] |  []  []  |  |  |  []  []  | ===***** |
 *************     |         @|__|__|@         |/ |*******|
***************   ***********--=====--**********| *********
***************___*********** |=====| **********|***********
 *************     ********* /=======\ ******** | *********

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

  __ __  ____ __ __ ____  ______   ___ ___        __ __  ___  __ __  _____  ___ 
 |  |  |/    |  |  |    \|      | /  _]   \      |  |  |/   \|  |  |/ ___/ /  _]
 |  |  |  o  |  |  |  _  |      |/  [_|    \     |  |  |     |  |  (   \_ /  [_ 
 |  _  |     |  |  |  |  |_|  |_|    _]  D  |    |  _  |  O  |  |  |\__  |    _]
 |  |  |  _  |  :  |  |  | |  | |   [_|     |    |  |  |     |  :  |/  \ |   [_ 
 |  |  |  |  |     |  |  | |  | |     |     |    |  |  |     |     |\    |     |
 |__|__|__|__|\__,_|__|__| |__| |_____|_____|    |__|__|\___/ \__,_| \___|_____|


                           WELCOME TO PHASMOPHOBIA!
                   WE ARE NOT RESPONSIBLE FOR POTENTIAL DEATH!

                              ====))-------------
            Game By: Saikarthick, Sidharth, Lithish, Shashank, Shreyaas
                              -------------((====

*****************************************************************************

""")


def life_system():
    if player_health <= 0:
        print("You have died! Goodbye!")
        return True
    return False


random_monster = random.choice(names)


def attack_system(m_health, p_health, p_attack, p_potion):
    while p_health > 0 and m_health > 0:
        att_monster = input("Do you want to attack, run or heal? \n")
        if att_monster == "attack":
            m_health -= p_attack
            print("the", random_monster, "health is now", m_health)
            if m_health <= 0:
                print("You defeated the monster and successfully escaped!")
                print("CONGRATULATIONS! YOU WON!")
                return
            print("the", random_monster, "attacks you")
            p_health -= 60
            print("your health is now", p_health)
            if p_health <= 0:
                print("You have died! Goodbye!")
                return
        elif att_monster == "run":
            print("the monster rips your flesh apart and you die")
            print("GAME OVER!")
            return
        elif att_monster == "heal":
            if p_potion >= 1:
                p_health += 100
                p_potion -= 1
                print("You healed 100 health! Your health is now", p_health)
                print("You have", p_potion, "potions left.")
            else:
                print("you dont have any potions left!")
        else:
            print("Invalid input! Try again!")


name = input("What is your name? \n")

print(f"{name}, you are currently locked up in a room chained to a wall.")
print("""
       .::::::::::.                        .::::::::::.
    .::::''''''::::.                      .::::''''''::::.
  .:::'          `::::....          ....::::'          `:::.
 .::'             `:::::::|        |:::::::'             `::.
.::|               |::::::|_ ___ __|::::::|               |::.
`--'               |::::::|_()__()_|::::::|               `--'
 :::               |::-o::|        |::o-::|               :::
 `::.             .|::::::|        |::::::|.             .::'
  `:::.          .::\-----'        `-----/::.          .:::'
    `::::......::::'                      `::::......::::'
      `::::::::::'                          `::::::::::'   
                                                          """)
time.sleep(2)

start = input("You manage to break free, where do you go?[left/right/up] \n")
print("""                            

                       :=     
                       :#=    
  .%%%%%%%%%%%%%%%%%%%%%%%=   
   %%%%%%%%%%%%%%%%%%%%%%%%=  
   %%%%%%%%%%%%%%%%%%%%%%%%%. 
   %%%%%%%%%%#%%%%%%%%%%%%%.  
   +********+**++++++++*%%.   
                       :%     
                       .      

       #                      
      %%                      
     %%#********************: 
   .%%#%%%%%%%%%%%%%%#%%%%%%- 
   %%#%%%%%%%%%%%%%%%%%%%%%%- 
   .%%%%%%%%%%%%%%%%%%%%%%%%- 
     #%%####################- 
      #%                      
       #                      
                              """)

if start == "left":
    print("You see an abandoned room, it seems dangerous...")
    print("""

    |____________________________________________|
    |__||  ||___||  |_|___|___|__|  ||___||  ||__|
    ||__|  |__|__|  |___|___|___||  |__|__|  |__||
    |__||  ||___||  |_|___|___|__|  ||___||  ||__|
    ||__|  |__|__|  |    || |    |  |__|__|  |__||
    |__||  ||___||  |    || |    |  ||___||  ||__|                                                            
    ||__|  |__|__|  |    || |    |  |__|__|  |__||
    |__||  ||___||  |    || |    |  ||___||  ||__|
    ||__|  |__|__|  |    || |    |  |__|__|  |__||                                                             
    |__||  ||___||  |   O|| |O   |  ||___||  ||__|
    ||__|  |__|__|  |    || |    |  |__|__|  |__||
    |__||  ||___||  |    || |    |  ||___||  ||__|
    ||__|  |__|__|__|____||_|____|  |__|__|  |__||
    |LLL|  |LLLLL|______________||  |LLLLL|  |LLL|
    |LLL|  |LLL|______________|  |  |LLLLL|  |LLL|
    |LLL|__|L|______________|____|__|LLLLL|__|LLL|

                                              """)
    time.sleep(1)
    dangerous_room_enter = input(
        "Do you still wish to go in?[yes/no/run to escape gate]\n")
    if dangerous_room_enter == "yes":
        print("You enter the room...")
        time.sleep(1)
        print("you find a shiny sword! It increases your damage by 50!")
        print("""O\\\\\[=================-""")
        damage_increase_random = random.randint(1, 3)
        player_attack = player_attack * damage_increase_random
        attack_system(monster_health, player_health, player_attack, potion)

    elif dangerous_room_enter == "run to escape gate":
        print("you encounter a small room before the exit...")
        time.sleep(2)
        print("the room is filled with fire...")
        time.sleep(1)
        fire_room = input("do you want to risk running through?[yes/no]\n")
        if fire_room == "yes":
            print("you risk it...")
            time.sleep(2)
            print("you trip...")
            time.sleep(2)
            print("you burn in the fire")
            time.sleep(1)
            print("you died")
            print("GAME OVER!")

        elif fire_room == "no":
            print("you decided not to use the fire path")
            time.sleep(1)
            print("8174")
            time.sleep(1)
            clear()
            print("you see the exit!")
            time.sleep(2)
            print("you see an arch door")
            time.sleep(1)
            print("the gate has a padlock")
            time.sleep(1)
            padlock = input("type the 4-digit code you saw before: ")
            if padlock == "8174":
                print("you enter the code...")
                time.sleep(1)
                print("it is processing...")
                time.sleep(1)
                print("you wrote the correct password!")
                print("congrats! you escaped the dungeon!")
                print("YOU WIN!")
            else:
                print("you enter the code...")
                time.sleep(1)
                print("it is processing...")
                time.sleep(1)
                print("Code Error!")
                print("A piston breaks the stone underneath you...")
                time.sleep(1)
                print("you fall down")
                time.sleep(1)
                print("you hit the ground too hard and died")
                print("GAME OVER!")

    elif dangerous_room_enter == "no":
        print("You decide to not go in the room.")
        no_room_enter = input(
            "Do you want to go to the right or left?[left/right]\n")
        print("""                            

                               :=     
                               :#=    
          .%%%%%%%%%%%%%%%%%%%%%%%=   
           %%%%%%%%%%%%%%%%%%%%%%%%=  
           %%%%%%%%%%%%%%%%%%%%%%%%%. 
           %%%%%%%%%%#%%%%%%%%%%%%%.  
           +********+**++++++++*%%.   
                               :%     
                               .      

               #                      
              %%                      
             %%#********************: 
           .%%#%%%%%%%%%%%%%%#%%%%%%- 
           %%#%%%%%%%%%%%%%%%%%%%%%%- 
           .%%%%%%%%%%%%%%%%%%%%%%%%- 
             #%%####################- 
              #%                      
               #                      
                                      """)
        if no_room_enter == "left":
            print("you fell in a hole and lost health!")
            player_health -= 50
            print("You now have", player_health, "health left.")
            if life_system():
                exit()
            time.sleep(2)
            print("You see the monster!")
            print("""
                                            ,--,  ,.-.
               ,                   \,       '-,-`,'-.' | ._
              /|           \    ,   |\         }  )/  / `-,',
              [ ,          |\  /|   | |        /  \|  |/`  ,`
              | |       ,.`  `,` `, | |  _,...(   (      .',
              \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\
               \  \_\,``,   ` , ,  /  |         )         _,/
                \  '  `  ,_ _`_,-,<._.<        /         /
                 ', `>.,`  `  `   ,., |_      |         /
                   \/`  `,   `   ,`  | /__,.-`    _,   `\
               -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                \_,,.) /\    ` /  / ) (-,, ``    ,        |
               ,` )  | \_\       '-`  |  `(               \
              /  /```(   , --, ,' \   |`<`    ,            |
             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
       ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
      (-, \           ) \ ('_.-._)/ /,`    /
      | /  `          `/ \\ V   V, /`     /
   ,--\(        ,     <_/`\\     ||      /
  (   ,``-     \/|         \-A.A-`|     /
 ,>,_ )_,..(    )\          -,,_-`  _--`
(_ \|`   _,/_  /  \_            ,--`
 \( `   <.,../`     `-.._   _,-`

 """)
            time.sleep(1)
            attack_system(monster_health, player_health, player_attack, potion)
        elif no_room_enter == "right":
            print("You see something shiny...")
            time.sleep(1)
            print("it is shaped like a crescent...")
            time.sleep(1)
            take_the_bow = input("Do you want to pick it up?[yes/no]\n")
            if take_the_bow == "yes":
                print("it is a bow of light! your attack damage increased!")
                bow_random_attack = random.randint(1, 3)
                player_attack = player_attack * bow_random_attack

                print("""    
           4$$-.
           4   ".     
           4   ".                                        
           4    ^.                                       
           4     $                                       
           4     'b                                      
           4      "b.                                    
           4        $                                    
           4        $r                                   
           4        $F                                   
-$b========4========$b====*P=-                           
           4       *$$F                                  
           4        $$"                                  
           4       .$F                                   
           4       dP                                    
           4      F                                      
           4     @                                       
           4     .                                        
           J.   @                                         
          '$$  #  """)
                print("the monster sees you and wants to fight...")
                attack_system(monster_health, player_health, player_attack,
                              potion)
            else:
                print("You decide not to pick it up.")
                print("the monster sees you and wants to fight...")
                attack_system(monster_health, player_health, player_attack,
                              potion)

elif start == "right":
    print("You fall down a hole and lose 75 health!")
    print("""
@@@@%#@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@*#@@#+@@@@@@@@
%@@@@@@@@@@@@@@@+%@@@@@@@@+.*@@@@%%@@@@@@@#*@@%=@@@@@@@
@@@@@@@@@@@@@@@+%@@@@@@@+  .@@@@@@@@@@@@@@@@@@-@@@@@@@@
@@@@@@@@@@@%+@@*#@@@@@@@:   #@@@@@@@*++*%@@@@@=@@@@@@@@
@@@@@@@@@@@%+@@+#@@@@@@@.   *@@@@*.      .*@@@@@@@@#@@@
@@@@#..@@@@%+@@*#@@@%@@@.   *@@@=  .%-     :@@@@#:  =@@
@@@@+. +@@@%*@@@@@@@@@@@:   =@@%   .-. +%:  *@@=.  .#@@
@@@@*.    .+%@@@@@@@@@@@:    #@%  -@#:      #@:    *@@@
%@@@%-        .=%@@@@@@@%.   .*@*.-%@+     +%:   .*@@@@
#@@@@@@%#=:      :%@@@@@@@-    ..--.    .-%*.   :#@@@@@
*@@@@@@@@@@@#.    .+@@@@@@#:        .=#%*:     :@@@@@@@
*:*@@@@@@@%##.     -@@@@+.                  :*@@@@@@@@%
*+..=*=:..    .-.    .%*.               .-*%@@@@@@@@@@@
%.              -:.              .=@@@@@@@@@@@@@@@@@@@@
#@#.  .:-=+*+.    ..             :%@@@@##@@@@@@@@@@@@@@
@@@@@@@@@@@@@:                .#@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@+.            :*@@@@@@@@@@@@@@@@@@@@@@@@@
=@@@@@@@@@@%%@@@@@+:      .+%@@@@@@@@@@@@@@@@@@%#@@@@@""")
    player_health -= 75
    if life_system():
        exit()
    print(
        "In the distance, you find a potion that heals your health but an ogre blocks the way."
    )
    print("It will let you pass only if you answer the question correctly.")
    answer = 0
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    conjunction = "and"
    try:
        answer = inputimeout(f'Multiply {num1} {conjunction} {num2}: ', timeout=5)
        if int(answer) == num1 * num2:
            print("The ogre lets you pass!")
            print("You grab the healing potion")
            choice = input("Do you drink it now? [yes/no] \n")
            if choice == "yes":
                player_health += 100
                potion = 0
                print("""
                    ( - )
                    ( - )
                . - ' - ' -  .
                |-  . . .  -|
                |-  . . .  -|
                |-  . . .  -|
                '-  {Heal} -'
                 \[ Potion ]/
                  \________/

                """)
                print("You drink the potion and heal 100 health!")
                print("Your health is now", player_health)
            else:
                potion += 1
                print("You save the potion for later.")
                print("You now have", potion, "potion(s).")

            time.sleep(1)
            print("You start to venture outside the mansion...")
            print(
                "You discover two paths, one to the left and one to the right."
            )
            time.sleep(1)
            path = input("Which path do you choose? [left/right]\n")
            if path == "left":
                print("You encounter a wild", random_monster, "!")
                time.sleep(1)
                attack_system(monster_health, player_health, player_attack,
                              potion)

            elif path == "right":
                fake_potion = input(
                    "You find what looks like a green potion. Do you drink it? [yes/no]\n"
                )

                time.sleep(1)
                if fake_potion == "yes":
                    time.sleep(1)
                    print("The potion contained poison. You died!")
                    print("GAME OVER!")

                elif fake_potion == "no":
                    time.sleep(1)
                    print(
                        "Lucky you! So glad you did not drink the bottle of poison."
                    )
                    print("Now...")
                    time.sleep(1)
                    print(
                        "Find the secret one digit number to unlock the door! You have 3 tries!"
                    )
                    random_number = random.randint(0, 9)

                    won = False
                    for x in range(3):
                        guess = int(input("Guess the one digit number: "))

                        if guess == random_number:
                            print(
                                "Congratulations! You almost escaped the haunted mansion. Just one last thing..."
                            )
                            won = True
                            break
                        elif guess > random_number:
                            print(
                                "Your number is higher than the secret number. Try again!"
                            )
                        elif guess < random_number:
                            print(
                                "Your number is lesser than the secret number. Try again!"
                            )

                    if won:
                        count = 0
                        while count < 5:
                            try:
                                last = inputimeout(
                                    'Type "I am not afraid of the dark" exactly. You have 25 seconds total.\n',
                                    timeout=25)
                                if last == "I am not afraid of the dark":
                                    count += 1
                                    print(f"Good! {count}/5 completed.")
                                else:
                                    print(
                                        "Please type that sentence exactly."
                                    )
                            except TimeoutOccurred:
                                print(
                                    "You took too long to type the sentence. You died!"
                                )
                                print("GAME OVER!")
                                exit()

                        print("You typed it 5 times!")
                        print("The door opens...")
                        print("You escape the haunted mansion!")
                        print("CONGRATULATIONS! YOU WIN!")
                    else:
                        print("You failed to guess the number. The answer was", random_number)
                        print("GAME OVER!")

        else:
            print("The ogre does not let you pass!")
            print("The ogre attacks you!")
            print("GAME OVER!")

    except TimeoutOccurred:
        print("You didn't answer in time!")
        print("The ogre attacks you for not speaking to him! You Died!")
        print("GAME OVER!")

elif start == "up":
    print("you see a ladder...")
    time.sleep(1)
    ladder = input("type 'climb' to climb the ladder: \n")
    time.sleep(1)
    if ladder == "climb":
        print("you see a wolf...")
        time.sleep(1)
        print("the wolf runs up to you")
        time.sleep(1)
        print("the wolf rips you apart")
        time.sleep(1)
        print("the wolf feasts on you")
        time.sleep(1)
        print("you died...")
        time.sleep(3)
        print("you respawn")
        time.sleep(2)
        print("you win because the monsters liked your attention span!")
        print("CONGRATULATIONS! YOU WIN!")
    else:
        print("You didn't climb. You stand there confused.")
        print("The ladder collapses on you.")
        print("GAME OVER!")
else:
    print("Invalid choice! The floor collapses beneath you.")
    print("GAME OVER!")
