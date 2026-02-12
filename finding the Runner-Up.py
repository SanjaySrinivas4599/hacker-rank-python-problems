if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    runnerups = []
    maxscore = max(arr)
    for score in arr: 
        if score != maxscore:
            runnerups.append(score)
    print(max(runnerups))
