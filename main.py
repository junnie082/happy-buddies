# 멤버이름 : [활동학기수, 가능날짜]
members = {
    "류창수": [10, []], "진성우": [10, []], "유도현": [10, []], "한종한": [10, []],
    "한영숙": [10, []], "김해슬": [10, []],"김우찬": [10, []], "박찬경": [10, []],
    "김선국": [8, []], "최태오": [8, []], "김성민": [8, []], "함민우": [8, []],
    "이용헌": [8, []], "이수연": [8, []], "서연우": [8, []], "안민혁": [8, []],
    "강지수": [6, []], "전효정": [6, []], "최승혜": [6, []], "박수겸": [6, []],
    "오효석": [6, []], "이의린": [4, []], "임채영": [4, []], "윤희정": [4, []],
    "김담우": [4, []], "김찬희": [4, []], "장승호": [4, []], "방재현": [4, []],
    "정기호": [4, []], "조시은": [2, []], "성예진": [2, []], "심혜원": [2, []],
    "이준": [2, []], "문성원": [2, []], "김형준": [2, []]
}

months = list(map(int, input().split()))
calculate_days = lambda x: 30 + (x%2 if  x <= 7  else  (0 if x % 2 else 1))
first_days = calculate_days(months[0])
second_days = calculate_days(months[1])
firstMonth = [[] for _ in range(first_days)]
secondMonth = [[] for _ in range(second_days)]

while(1):
    name = input()
    if name == "회원끝":
        break

    while(1):
        date = input()
        if date == "날짜끝":
            break

        members[name][1].append(date)

        if int(date.split('.')[0]) == months[0]:
            firstMonth[int(date.split('.')[1])].append(name)
        else:
            secondMonth[int(date.split('.')[1])].append(name)

        members[name][1].append(date)

firstMonth.sort(reverse=True)
secondMonth.sort(reverse=True)



for i in firstMonth:
    print(i, end=" ")

print()

for i in secondMonth:
    print(i, end=" ")

# for name, values in members.items():
#     print("name: " + name + " ")
#     for i in range(len(values[1])):
#         print(members[name][1][i] , end = " ")
#     print()
