from members import Members
from dates import Dates
from counting_table import CountingTable
from pair_buddies import PairBuddies
from tkinter import *
from tkinter import Tk,Button,ttk,messagebox
from tkcalendar import DateEntry

# # # # # UI # # # # # # 

datesAndMembersList = []
months = []

def get_date():
    selected_date = cal.get()
    month = selected_date.split('-')[1]
    # 훈련 당월 (최대 두 개) 계산하기
    if all(month not in mon for mon in months):
        months.append(month)
    members = names.get()
    # 겹치는 날짜가 하나도 없다면, datesAndMembers에 append
    if all(selected_date not in date for date in datesAndMembersList):
        datesAndMembersList.append([selected_date, members])
    putMemBtn['text'] = f"date: {selected_date} name: {members}"

root = Tk()
root.title("Happy Buddies")
root.geometry("600x500")
cal = DateEntry(root, date_pattern="yyyy-mm-dd")
cal.pack()

names = StringVar()

textbox = ttk.Entry(root, width = 30, textvariable=names)
textbox.pack()

# 해당 날짜에 멤버 이름 기입.
putMemBtn = Button(root, text="Next Date", command=get_date)
putMemBtn.pack()

# '마침' 버튼, 멤버들을 모두 기입한 후.
# # # # # # # # # LOGIC # # # # # # # # # # # # 

mem = Members()
dates = Dates()

pair_buddies = PairBuddies()
cnt_table = CountingTable()

def done(): 
    for i,m in enumerate(months):
        months[i] = int(m)
    
    print("months: ", months)
    dates.set_month(months)
    print(months)

    
    dates.iniNamesInFirstMonth()
    if len(months) == 2: 
        dates.iniNamesInSecondMonth()

    cnt_table.initMonths(months)

    while len(datesAndMembersList) != 0:
        datesAndMemebers = datesAndMembersList.pop()
        date = datesAndMemebers[0]
        _, month, day = map(int, date.split('-'))
        members = datesAndMemebers[1]
        names = members.split(',')

        priorities = []

        for name in names:
            if name == '': continue
            priorities.append([mem.members[name][0], name])

        if len(priorities) == 0: continue 

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

# 파일로 열기.
# print("훈련 당월을 입력하세요: (1부터 12까지 최대 2개의 정수를 띄어 작성하세요. 예시: 11 12) ")
# months = list(map(int, input().split()))
# if months[0] > months[1]:
#     months[0], months[1] = months[1], months[0]

# f = open("memberList.txt", "r")
# while True:
#     line = f.readline()
#     if not line: break
#     date = line.split()[0]
#     month, day = map(int, line.split()[0].split('.'))
#     names = line.split()[1].split(',')

#     priorities = []

#     for name in names:
#         priorities.append([mem.members[name][0], name])
#     priorities.sort(reverse=True)


#     for name in priorities:
#         name = name[1]
#         mem.addPossibleDateInMember(name, date)

#         if month == dates.months[0]:
#             dates.names_in_first_month[day - 1].append(name)
#             if mem.members[name][0] <= 2:
#                 cnt_table.firstMonth[day - 1][0] += 1
#             else:
#                 cnt_table.firstMonth[day - 1][1] += 1
#         else:
#             dates.names_in_second_month[day - 1].append(name)
#             if mem.members[name][0] <= 2:
#                 cnt_table.secondMonth[day - 1][0] += 1
#             else:
#                 cnt_table.secondMonth[day - 1][1] += 1
    pair_buddies.setMembers(mem)
    pair_buddies.setMonths(months)
    pair_buddies.setNamesInFirstMonth(dates.names_in_first_month)
    pair_buddies.setNamesInSecondMonth(dates.names_in_second_month)
    pair_buddies.setCntTable(cnt_table)

    pair_buddies.pairUpBuddies(cnt_table.firstMonth, dates.names_in_first_month, 0)
    pair_buddies.pairUpBuddies(cnt_table.secondMonth, dates.names_in_second_month, 1)

    pair_buddies.pairTheRest(cnt_table.firstMonth, dates.names_in_first_month, 0)
    pair_buddies.pairTheRest(cnt_table.secondMonth, dates.names_in_second_month, 1)

    printBuddies()
    printTraingDays()



donePutBtn = Button(root, text="Done", command=done)
donePutBtn.pack()

def printBuddies(): 
    # 매치된 버디 출력
    text_container = Text(
        root,
        width = 60,
        height = 30
    )

    items = pair_buddies.getBuddies().items()

    for key, values in items:
        text_container.insert('end', key+"\n")
        for value in values: 
            text_container.insert('end', value)
            text_container.insert('end', " ")
        text_container.insert('end', '\n\n')
    
    text_container.pack(expand=True)

def printTraingDays(): 
    # 각 회원 별 훈련 날짜 수
    print("\n")
    for i, m in enumerate(months): 
        print('각 회원이 ' + str(months[i]) + '월, ')
        
    print('에 훈련을 받는 횟수: ')
    for member, values in cnt_table.membersInCntTable.items():
        print(member, values, end = " ")


root.mainloop()
# calendar: https://www.tutorialspoint.com/how-to-handle-a-button-click-event-in-tkinter
# dynamic button: https://pythonexamples.org/python-tkinter-change-button-text-dynamically/
# StringVar() 을 담은 변수의 이름은 반드시 str 이어야 하나보다. 
# 2차원 배열의 포함여부 검사하기: https://velog.io/@woo0_hooo/python-2차원-리스트에서-원소의-포함여부-검사하기