import re

def crane():
    s1 = ["V", "C", "D", "R", "Z", "G", "B", "W"]
    s2 = ["G", "W", "F", "C", "B", "S", "T", "V"]
    s3 = ["C", "B", "S", "N", "W"]
    s4 = ["Q", "G", "M", "N", "J", "V", "C", "P"]
    s5 = ["T", "S", "L", "F", "D", "H", "B"]
    s6 = ["J", "V", "T", "W", "M", "N"]
    s7 = ["P", "F", "L", "C", "S", "T", "G"]
    s8 = ["B", "D", "Z"]
    s9 = ["M", "N", "Z", "W"]
    message = []
    count = 1

    print("\nBefore crane moves:\n")
    for num in range(1,10):
        print(f'Stack {num}: {eval("s"+str(num))}')

    file = open("crane.txt", "r")
    
    for line in file:
        clean = list(re.sub('[a-z]', '', line).strip("\n").replace(" ", ""))
        if len(clean) == 3:
            moves = int(clean[0])
            from_list = "s"+clean[1]
            to_list = "s"+clean[2]
        else:
            moves = int(clean[0] + clean[1])
            from_list = "s"+clean[2]
            to_list = "s"+clean[3]
            
        move_stack = eval(from_list)
        to_stack = eval(to_list)

        for move in range(moves):
            if move_stack:
                lift = move_stack.pop(-1)
                to_list = to_stack.append(lift)
            else:
                pass

        count += 1

    print("\nAfter crane moves:\n")
    for num in range(1,10):
        print(f'Stack {num}: {eval("s"+str(num))}')

    print("\n")

if __name__ == "__main__":
    crane()