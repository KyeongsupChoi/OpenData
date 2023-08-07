
babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
def solution(babbling):
    test = ["ye", "ma", "woo", "aya"]
    for x in babbling:
        for y in test:
            if len(y) > len(x):
                pass
            print(x[0:len(y)])
            if x[0:len(y)] == y:
                print("yay")
    answer = 0
    return answer

solution(babbling)