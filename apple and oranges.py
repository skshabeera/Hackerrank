def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    count_apples=0
    count_oranges=0
    for d in apples:
        if a+d in range(s,t+1):
            count_apples+=1
    for d in oranges:
        if b+d in range(s,t+1):
            count_oranges+=1
    print(count_apples)
    print(count_oranges)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)


