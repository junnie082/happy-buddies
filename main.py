from members import Members
from dates import Dates
from counting_table import CountingTable

mem = Members()
dates = Dates()
months = list(map(int, input().split()))

dates.set_month(months)
dates.days_in_first_month()
dates.days_in_second_month()

cnt_table = CountingTable(months)

while(1):
    name = input()
    if name == "회원끝":
        break

    while(1):
        date = input()
        if date == "날짜끝":
            break
        month, day = map(int, date.split('.'))

        mem.addPossibleDateInMember(name, date)

        if month == dates.months[0]:
            dates.firstMonth[day-1].append(name)
            if mem.members[name][0] <= 2:
                cnt_table.firstMonth[day-1][0] += 1
            else:
                cnt_table.firstMonth[day-1][1] += 1
        else:
            dates.secondMonth[day-1].append(name)
            if mem.members[name][0] <= 2:
                cnt_table.secondMonth[day-1][0] += 1
            else:
                cnt_table.secondMonth[day-1][1] += 1

        mem.members[name][1].append(date)


for i in cnt_table.firstMonth:
    print(i, end=" ")

print()

for i in cnt_table.secondMonth:
    print(i, end=" ")

# for name, values in members.items():
#     print("name: " + name + " ")
#     for i in range(len(values[1])):
#         print(members[name][1][i] , end = " ")
#     print()
