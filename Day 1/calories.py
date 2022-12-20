def main():
    file = open("calories.txt", "r")
    current_count = 0
    calorie = []
    for x in file:
        if x == '\n':
            calorie.append(current_count)
            current_count = 0
        else:
            current_count += int(x)
    calorie.sort()
    return calorie

def top_elf(l):
    print(l[-1])

def top_three_elves(l):
    print(sum(l[-3:]))

if __name__ == "__main__":
    l = main()
    top_elf(l)
    top_three_elves(l)