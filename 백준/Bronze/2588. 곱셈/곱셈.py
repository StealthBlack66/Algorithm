# 첫 번째 세 자리 자연수를 입력받습니다.
num1 = int(input())

# 두 번째 세 자리 자연수를 입력받습니다.
num2 = int(input())

# 각 자리의 수를 구합니다.
num2_units = num2 % 10
num2_tens = (num2 // 10) % 10
num2_hundreds = num2 // 100

# 각 자리 수와 num1의 곱셈 결과를 구합니다.
result1 = num1 * num2_units
result2 = num1 * num2_tens
result3 = num1 * num2_hundreds

# 최종 결과를 구합니다.
final_result = num1 * num2

# 결과를 출력합니다.
print(result1)
print(result2)
print(result3)
print(final_result)
