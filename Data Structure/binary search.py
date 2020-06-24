

# Author : 5hifaT

# Github        : https://github.com/jspw

# Gists         : https://gist.github.com/jspw

# linkedin      : https://www.linkedin.com/in/mehedi-hasan-shifat-2b10a4172/

# Stackoverflow : https://stackoverflow.com/story/jspw

# Dev community : https://dev.to/mhshifat

def binary_search(ar, value):

    start = 0
    end = len(ar)-1

    while(start <= end):
        mid = (start+end)//2
        print("start : {},end : {},mid {}".format(
            start, end, mid), end="\n")
        if(ar[mid] == value):
            return mid

        if(ar[mid] > value):
            end = mid-1

        else:
            start = mid+1

    return -1


def main():
    for _ in range(int(input())):
        ar = list(map(int, input().split()))
        value = int(input())
        pos = binary_search(ar, value)
        if(pos != -1):
            print("{}  found  at  position : {}".format(value, pos), end=" ")
        else:
            print("{} not found".format(value), end="\n")


if __name__ == "__main__":
    main()
