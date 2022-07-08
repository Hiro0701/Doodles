import random

L = ['Rock', 'Scissor', 'Paper']
Answer = ['Yes', 'No']

again = True

def choice():
    E = input("Which game do you want to play? \n1. Normal Rock Scissor Paper \n2. One of two version \n")
    if E == '1':
        normal(again)
    elif E == '2':
        two_one(again)

def normal(again):

    while again:
        A = input("Your choice is: ")
        B = random.choice(L)

        proper = False

        if A not in L:
            proper = False
        else:
            proper = True

        while not proper:
            A = input("You typed wrong. Please type it again: ")

            if A in L:
                proper = True

        if A == B:
            print("It's a draw!")
        else:
            if A == 'Rock':
                if B == 'Scissor':
                    print("You win!")
                else:
                    print("You lose!")
            elif A == 'Scissor':
                if B == 'Rock':
                    print("You lose!")
                else:
                    print("You win!")
            else:
                if B == 'Rock':
                    print("You win!")
                else:
                    print("You lose!")

        proper1 = False
        while not proper1:
            C = input("Do you want to play this game one more time: ")
            if C == Answer[0]:
                proper1 = True
            elif C == Answer[1]:
                proper2 = False
                while not proper2:
                    D = input("Do you want to play another game: ")
                    if D == Answer[0]:
                        proper1 = True
                        choice()
                    elif D == Answer[1]:
                        proper1 = True
                        again = False
                    else:
                        print("You typed wrong")
            else:
             print("You typed wrong.")


def two_one(again):

    while again:
        A = input("Your two choices are: ").split()
        B = random.choice(L)

        proper = False

        while len(A) != 2:
            A = input("You didn't type two choices. Please type two choices ").split()

        for i in A:
            if i not in L:
                proper = False
            else:
                proper = True

        while not proper:
            A = input("You typed wrong. Please type it again: ").split()

            for i in A:
                if i in L:
                    proper = True

        E = input(f"Please choose one option you want to pick: {A[0]} or {A[1]}. ")

        if E not in A:
            proper = False
        else:
            proper = True

        while not proper:
            E = input("You typed wrong. Please type it again: ")

            if E in L:
                proper = True

        if E == B:
            print("It's a draw!")
        else:
            if E == 'Rock':
                if B == 'Scissor':
                    print("You win!")
                else:
                    print("You lose!")
            elif E == 'Scissor':
                if B == 'Rock':
                    print("You lose!")
                else:
                    print("You win!")
            else:
                if B == 'Rock':
                    print("You win!")
                else:
                    print("You lose!")

        proper1 = False
        while not proper1:
            C = input("Do you want to play this game one more time: ")
            if C == Answer[0]:
                proper1 = True
            elif C == Answer[1]:
                proper2 = False
                while not proper2:
                    D = input("Do you want to play another game: ")
                    if D == Answer[0]:
                        proper1 = True
                        proper2 = True
                        choice()
                    elif D == Answer[1]:
                        proper1 = True
                        proper2 = True
                        again = False
                    else:
                        print("You typed wrong")
            else:
                print("You typed wrong.")

choice()