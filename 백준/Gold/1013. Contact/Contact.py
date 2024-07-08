import re

def check_patterns(case):
    pattern = re.compile(r"(100+1+|01)+")
    if pattern.fullmatch(case):
        return "YES"
    else:
        return "NO"

T = int(input())
for _ in range(T):
    case = input().strip()
    result = check_patterns(case)
    print(result)