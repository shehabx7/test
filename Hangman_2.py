import random
def guessing():
    trials = 0
    arr = ['all', 'names', 'games', 'play', 'arabic', 'english', 'french']  # all as test case
    rand = random.choice(arr)
    star_Arr = list(len(rand) * '*')
    guessed_letters = []
    print(rand)
    while trials < 7:
        alpha = input("guess! : ")
        if alpha in guessed_letters:
            trials += 1
            print(f"Already guessed letter.You have {7 - trials} trials left")
            continue
        if alpha in rand:
            for i in range(0, len(rand)):
                if rand[i] == alpha:
                    guessed_letters.append(alpha)
                    star_Arr[i] = alpha
                    print("right guess")
                    print(star_Arr)
                if '*' not in star_Arr:
                    print("Winner")
                    return # break
        else:

            trials += 1
            print(f"Wrong guess. You have {7 - trials} attempts left.")

    else:
        print(f'Game Over the name is {rand}')


guessing()
