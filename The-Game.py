print("You're in a hallway and a thief approaches you and tries to rob you, what do you do?")

Gun = input('Do you take the gun? (y/n) ')
Bullets = 1
Time = 3
Metre = 5


class Bullshoot:
    pass


if Gun == "y":
    BullShoot = input('Do you first check the bullets or instantly shoot the thief? (check/shoot) ')
    if BullShoot == "check":
        if Bullets and Time < 6:
            print('You failed! You took too long checking the bullets of the gun and the thief killed you!')
    elif Bullshoot != 'check':
        print('You won! Luckily there were enough bullets in the gun to kill the thief!')
if Gun is not "y":
    ThrowLet = input('You chose no gun, do you throw the weapon away or do you keep it on the floor? (throw/keep) ')
    if ThrowLet == "throw":
        Metre = int(input('How far do you throw the gun? (In metres) '))
        if Metre or Time >= 6:
            WeaponFist = input('Now, do you try to find a weapon or do you fight with your fists? (weapon/fists) ')
            if WeaponFist == "weapon":
                BarStick = input('You see 2 things, an iron bar and a wooden stick. What do you choose? (bar/stick) ')
                if BarStick == "bar":
                    print(
                        'You won! You knocked them out with the pipe and hit them till they bled to death afterwards.')
                elif BarStick == "stick":
                    print('You failed! The stick broke on impact! The thief picked up the pipe and killed you!')
            if WeaponFist == "fists":
                KnockoutBleed = input(
                    'Now, do you hit them till they bleed or do you knock them out? (bleed/knockout) ')
                if KnockoutBleed == "bleed":
                    print('You won! Your punches eventually let the thief bleed to death!')
                if KnockoutBleed == "knockout":
                    print('You failed! Many years later the thief recognized you and took their revenge!')
        if ThrowLet == "keep":
            WeaponRun = input(
                'The gun is on the floor! Do you try to find a weapon or rush at the thief? (weapon/rush)')
            if WeaponRun == "weapon":
                print('You failed... The thief just picked up the gun and shot you... Dumbass')
            if WeaponRun == "rush":
                if Time <= 3:
                    print('You failed... The thief dodged your rush, picked up the gun and shot you... Dumbass')
