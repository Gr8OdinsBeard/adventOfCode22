def assignments():
    file = open("assignments.txt", "r")
    contained = 0

    lines = file.readlines()
    for row in lines:
        ranges = row.strip('\n').replace(" ", "").split(',')
        range1 = ranges[0].split('-')
        range2 = ranges[1].split('-')

        if int(range1[0]) >= int(range2[0]) and int(range1[1]) <= int(range2[1]):
                contained += 1
        elif int(range2[0]) >= int(range1[0]) and int(range2[1]) <= int(range1[1]):
                contained += 1

    print(contained)

def overlap():
    file = open("assignments.txt", "r")
    overlap = 0

    lines = file.readlines()
    for row in lines:
        ranges = row.strip('\n').replace(" ", "").split(',')
        range1 = ranges[0].split('-')
        range2 = ranges[1].split('-')
        start1 = int(range1[0])
        stop1 = int(range1[1])
        start2 = int(range2[0])
        stop2 = int(range2[1])

        if start1 in range(start2, stop2 + 1) or stop1 in range(start2, stop2 + 1):
            overlap += 1
        elif start2 in range(start1, stop1 + 1) or stop2 in range(start1, stop1 + 1):
            overlap += 1    

    print(overlap)

if __name__ == "__main__":
    assignments()
    overlap()