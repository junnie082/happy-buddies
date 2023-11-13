from members import Members
from dates import Dates
from counting_table import CountingTable
from pair_buddies import PairBuddies


mem = Members()
dates = Dates()
months = list(map(int, input().split()))
if (months[0] == 12 and months[1] == 1):
    months[0], months[1] = months[1], months[0]
pair_buddies = PairBuddies()

dates.set_month(months)
dates.iniNamesInFirstMonth()
dates.iniNamesInSecondMonth()

cnt_table = CountingTable()
cnt_table.initMonths(months)


f = open("memberList.txt", "r")
while True:
    line = f.readline()
    if not line: break
    date = line.split()[0]
    month, day = map(int, line.split()[0].split('.'))
    names = line.split()[1].split(',')

    priorities = []

    for name in names:
        priorities.append([mem.members[name][0], name])
    priorities.sort(reverse=True)


    for name in priorities:
        name = name[1]
        mem.addPossibleDateInMember(name, date)

        if month == dates.months[0]:
            dates.names_in_first_month[day - 1].append(name)
            if mem.members[name][0] <= 2:
                cnt_table.firstMonth[day - 1][0] += 1
            else:
                cnt_table.firstMonth[day - 1][1] += 1
        else:
            dates.names_in_second_month[day - 1].append(name)
            if mem.members[name][0] <= 2:
                cnt_table.secondMonth[day - 1][0] += 1
            else:
                cnt_table.secondMonth[day - 1][1] += 1


# while(1):
#     name = input()
#     if name == "회원끝":
#         break
#
#     while(1):
#         date = input()
#         if date == "날짜끝":
#             break
#         month, day = map(int, date.split('.'))
#
#         mem.addPossibleDateInMember(name, date)
#
#         if month == dates.months[0]:
#             dates.names_in_first_month[day-1].append(name)
#             if mem.members[name][0] <= 2:
#                 cnt_table.firstMonth[day-1][0] += 1
#             else:
#                 cnt_table.firstMonth[day-1][1] += 1
#         else:
#             dates.names_in_second_month[day-1].append(name)
#             if mem.members[name][0] <= 2:
#                 cnt_table.secondMonth[day-1][0] += 1
#             else:
#                 cnt_table.secondMonth[day-1][1] += 1
#
#         mem.members[name][1].append(date)
pair_buddies.setMembers(mem)
pair_buddies.setMonths(months)
pair_buddies.setNamesInFirstMonth(dates.names_in_first_month)
pair_buddies.setNamesInSecondMonth(dates.names_in_second_month)
pair_buddies.setCntTable(cnt_table)

pair_buddies.pairUpBuddies(cnt_table.firstMonth, dates.names_in_first_month, 0)
pair_buddies.pairUpBuddies(cnt_table.secondMonth, dates.names_in_second_month, 1)

for i in dates.names_in_first_month:
    print(i)

pair_buddies.pairTheRest(cnt_table.firstMonth, dates.names_in_first_month, 0)
pair_buddies.pairTheRest(cnt_table.secondMonth, dates.names_in_second_month, 1)

#
print("buddies: ")
print(pair_buddies.getBuddies())


# 각 회원 별 가능 날짜
# for member, values in mem.members.items():
#     print(member, values)
#
# 각 회원 별 훈련 날짜 수
print("\n")
print("각 회원이 " + str(months[0]) + "월과 " + str(months[1]) + "월에 훈련을 받는 횟수: ")
for member, values in cnt_table.membersInCntTable.items():
    print(member, values, end = " ")

#
# for i in cnt_table.firstMonth:
#     print(i)
