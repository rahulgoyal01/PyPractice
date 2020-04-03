if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


score = set(arr)
score = list(score)
score.sort()
print(score[-2])
