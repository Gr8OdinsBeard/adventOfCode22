import string
def rucksack_sort():

    file = open("rucksack.txt", "r")
    priority = []
    priority_sum = 0

    for i in range(1,53):
        if i <= 26 :
            priority.append(list(string.ascii_lowercase)[i-1])
        else:
            priority.append(list(string.ascii_uppercase)[i-27])

    for row in file:
        compartment1 = set(row[:len(row)//2])
        compartment2 = set(row[len(row)//2:])
        common_el = (compartment1 & compartment2)
        priority_sum += priority.index(min(common_el)) + 1

    print(priority_sum)

    file.close()

def group_sort():
    file = open("rucksack.txt", "r")
    priority = []
    priority_sum = 0
    start = 0
    end = 2

    for i in range(1,53):
        if i <= 26 :
            priority.append(list(string.ascii_lowercase)[i-1])
        else:
            priority.append(list(string.ascii_uppercase)[i-27])

    lines = file.readlines()
    while end <= 299:
        compartment1 = lines[start]
        compartment2 = lines[start+1]
        compartment3 = lines[end]
        compartment1 = compartment1.strip("\n")
        compartment2 = compartment2.strip("\n")
        compartment3 = compartment3.strip("\n")
        common_el = (set(compartment1) & set(compartment2))
        common_el = (common_el & set(compartment3))
        print(common_el)
        start += 3
        end += 3
        priority_sum += priority.index(min(common_el)) + 1

    print(priority_sum)

    file.close()

if __name__ == "__main__":
    rucksack_sort()
    group_sort()