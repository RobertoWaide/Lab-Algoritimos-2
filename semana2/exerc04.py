def check(list):
    result = 0
    smaller = 999
    bigger = 0
    for i in range(3):
        bigger = 0
        smaller = 999
        for j in list[i]:
            if j > bigger:
                bigger = j
            if j < smaller:
                smaller = j
        for h in list[i]:
            if h != bigger and h != smaller:
                result += h
    return result

def main():
    list = [
        [69,3,2],
        [420,13,16],
        [5,10,8]]
    result = check(list)
    print(result)

main()
