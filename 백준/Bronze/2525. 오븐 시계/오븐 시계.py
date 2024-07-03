# 현재 시각 A 시 B 분을 입력받습니다.
A, B = map(int, input().split())

# 요리하는 데 필요한 시간 C 분을 입력받습니다.
C = int(input())

# 현재 시각에 요리하는 데 필요한 시간을 더합니다.
total_minutes = A * 60 + B + C

# 시와 분을 계산합니다.
end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

# 결과를 출력합니다.
print(end_hour, end_minute)
