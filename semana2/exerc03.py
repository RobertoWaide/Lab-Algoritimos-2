def check(list):
    result = 0
    bigger = 0
    for i in range(3):
        bigger = 0
        for j in list[i]:
            if j > bigger:
                bigger = j
        result += bigger
    return result

def main():
    list = [
    [17,42,9],
    [5,23,88],
    [63,12,30]]
    result = check(list)
    print(result)

main()
