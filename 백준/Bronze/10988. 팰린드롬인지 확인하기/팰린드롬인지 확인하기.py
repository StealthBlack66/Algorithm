S=input()
arr_front=[]
arr_back=[]
mid=len(S)//2
for letter in S[:mid]:
      arr_front.append(letter)
if len(S)%2==0:
    for letter in S[mid:]:
      arr_back.append(letter)
else:
    for letter in S[mid+1:]:
      arr_back.append(letter) 
if arr_front==arr_back[::-1]:
    print(1)
else:
    print(0)