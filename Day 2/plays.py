def main():
    file = open("plays.txt", "r")
    opponent_play = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
    }

    my_play = {
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }
    
    my_score = 0
    opponent_score = 0

    for row in file:
        index =row.split()
        if opponent_play[index[0]] == "Rock" and my_play[index[1]] == "Scissors":
            my_score += 3
            opponent_score += 7
        
        elif opponent_play[index[0]] == "Rock" and my_play[index[1]] == "Paper":
            my_score += 8
            opponent_score += 1

        elif opponent_play[index[0]] == "Paper" and my_play[index[1]] == "Rock":
            my_score += 1
            opponent_score += 8

        elif opponent_play[index[0]] == "Paper" and my_play[index[1]] == "Scissors":
            my_score += 9
            opponent_score += 2

        elif opponent_play[index[0]] == "Scissors" and my_play[index[1]] == "Rock":
            my_score += 7
            opponent_score += 3

        elif opponent_play[index[0]] == "Scissors" and my_play[index[1]] == "Paper":
            my_score += 2
            opponent_score += 9

        elif opponent_play[index[0]] == "Rock" and my_play[index[1]] == "Rock":
            my_score += 4
            opponent_score += 4

        elif opponent_play[index[0]] == "Paper" and my_play[index[1]] == "Paper":
            my_score += 5
            opponent_score += 5

        elif opponent_play[index[0]] == "Scissors" and my_play[index[1]] == "Scissors":
            my_score += 6
            opponent_score += 6

    print(f'I scored {my_score}, my opponent scored {opponent_score}')

    file.close()

def main2():
    file = open("plays.txt", "r") 
    score = 0 
    points = {
        "AX": 4, "AY": 8, "AZ": 3,
        "BX": 1, "BY": 5, "BZ": 9,
        "CX": 7, "CY": 2, "CZ": 6,
    }

    for row in file:
        clean = row.strip("\n").replace(" ", "")
        score += points[clean]

    print(score)
    file.close()

def main3():
    file = open("plays.txt", "r") 
    score = 0 
    points = {
        "AX": 3, "AY": 4, "AZ": 8,
        "BX": 1, "BY": 5, "BZ": 9,
        "CX": 2, "CY": 6, "CZ": 7,
    }

    for row in file:
        clean = row.strip("\n").replace(" ", "")
        score += points[clean]

    print(score)
    file.close()

if __name__ == "__main__":
    # main()
    main2()
    main3()

  