from members import Members
from dates import Dates
from counting_table import CountingTable
from pair_buddies import PairBuddies
from tkinter import *
from tkinter import Tk, Button, ttk
from tkcalendar import DateEntry


mem = Members()
dates = Dates()

pair_buddies = PairBuddies()
cnt_table = CountingTable()

# # # # # UI # # # # # #

datesAndMembersList = []
months = []

root = Tk()
root.title("Happy Buddies")
root.geometry("1000x900")

inputBox = Listbox(
    root,
    selectmode="extended",
    width=50
)

def delete():
    date = inputBox.get(inputBox.curselection()).split()[0]
    for i, datesAndMembers in enumerate(datesAndMembersList):
        if datesAndMembers[0] == date:
            del datesAndMembersList[i]

    inputBox.delete(inputBox.curselection())


def get_date():
    try:
        selected_date = cal.get()
        month = selected_date.split('-')[1]
        # 훈련 당월 (최대 두 개) 계산하기
        if all(month not in str(mon) for mon in months):
            months.append(month)
        members = names.get()
        nameList = list(members.split(','))

        flag = True
        for datesAndMembers in datesAndMembersList:
            if datesAndMembers[0] == str(selected_date):
                cmpList = datesAndMembers[1].split(',')
                if any(name in cmpList for name in nameList):
                    flag = False
                if flag == False:
                    putMemBtn['text'] = "주의! 입력된 회원이 중복으로 추가 되었으므로, 이번에 입력된 동아리원들은 추가되지 않습니다. 다시 입력하세요."
                    print("주의! 입력된 회원이 중복으로 추가 되었으므로, 이번에 입력된 동아리원들은 추가되지 않습니다. 다시 입력하세요.")
                    break

        if flag == True:
            datesAndMembersList.append([selected_date, members])
            putMemBtn['text'] = "Add"
            inputBox.insert('end', selected_date + " " + members + "\n")

    except EXCEPTION as e:
        print(e)

inputBox.pack()

def reset():
    datesAndMembersList.clear()
    mem.resetMembers()
    cnt_table.resetCntTable()
    dates.resetDate()
    pair_buddies.resetBuddies()
    text_container_buddies.delete("1.0", "end")
    text_container.delete("1.0", "end")
    inputBox.delete(0, END)


resetBtn = Button(root, text="RESET", command=reset)
resetBtn.pack()



cal = DateEntry(root, date_pattern="yyyy-mm-dd")
cal.pack()

names = StringVar()


textbox = ttk.Entry(root, width=30, textvariable=names)
textbox.pack()

# 해당 날짜에 멤버 이름 기입.
putMemBtn = Button(root, text="Add", command=get_date)
putMemBtn.pack()

deleteBtn = Button(root, text="Delete", command=delete)
deleteBtn.pack()
# '마침' 버튼, 멤버들을 모두 기입한 후.
# # # # # # # # # LOGIC # # # # # # # # # # # #



def done():
    text_container_buddies.delete("1.0", "end")
    text_container.delete("1.0", "end")
    inputBox.delete(0, END)
    for i, m in enumerate(months):
        months[i] = int(m)

    print("months: ", months)
    dates.set_month(months)
    print(months)

    dates.iniNamesInFirstMonth()
    if len(months) == 2:
        dates.iniNamesInSecondMonth()

    useDatesAndMemberList = datesAndMembersList.copy()

    cnt_table.initMonths(months)
    print("datesAndMemberList: " + str(datesAndMembersList))

    while len(useDatesAndMemberList) != 0:
        datesAndMemebers = useDatesAndMemberList.pop()
        date = datesAndMemebers[0]
        _, month, day = map(int, date.split('-'))
        members = datesAndMemebers[1]
        names = members.split(',')

        priorities = []
        flag = True
        for name in names:
            if name == '': continue
            for _, buddies in pair_buddies.getBuddies().items():
                for buddy in buddies:
                    if buddy == name:
                        flag = False
                        break
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

    # pair_buddies.removeDuplicate()

    printBuddies()
    printTrainingDays()

    pair_buddies.resetAllOfBuddies()
    datesAndMembersList.clear()

doneBtn = Button(root, text="Done", command=done)
doneBtn.pack()


text_container_buddies = Text(
        root,
        width=60,
        height=20
)

def printBuddies():
    # 매치된 버디 출력

    items = sorted(pair_buddies.getBuddies().items())
    print("items: " + str(items))
    for key, values in items:
        text_container_buddies.insert('end', key + "\n")
        for value in values:
            text_container_buddies.insert('end', value)
            text_container_buddies.insert('end', " ")
        text_container_buddies.insert('end', '\n\n')


text_container_buddies.pack(expand=True)


def resetOut():
    text_container_buddies.delete("1.0", "end")

resetOutputBtn = Button(root, text="CLEAR", command=resetOut)
resetOutputBtn.pack()


text_container = Text(
        root,
        width=60,
        height=10
)

def printTrainingDays():
    # 각 회원 별 훈련 날짜 수
    print("\n")

    text_container.tag_config('red', foreground='red')
    text_container.tag_config('green', background='yellow', foreground='green')
    text_container.tag_config('blue', background='blue', foreground='white')
    for i, m in enumerate(months):
        print('각 회원이 ' + str(months[i]) + '월, ')

    items = sorted(cnt_table.membersInCntTable.items())
    print('에 훈련을 받는 횟수: ')
    for member, value in items:
        text_container.insert('end', member + " ")
        if value == 0:
            text_container.insert('end', str(value) + " ", 'red')
        elif value == 1:
            text_container.insert('end', str(value) + " ", 'green')
        else:
            text_container.insert('end', str(value) + " ", 'blue')

        print(member, value, end=" ")

text_container.pack(expand=True)


root.mainloop()
# calendar: https://www.tutorialspoint.com/how-to-handle-a-button-click-event-in-tkinter
# dynamic button: https://pythonexamples.org/python-tkinter-change-button-text-dynamically/
# StringVar() 을 담은 변수의 이름은 반드시 str 이어야 하나보다. => 아님.
# 2차원 배열의 포함여부 검사하기: https://velog.io/@woo0_hooo/python-2차원-리스트에서-원소의-포함여부-검사하기
# textbox 에서 글 색상 바꾸기: https://stackoverflow.com/questions/47591967/changing-the-colour-of-text-automatically-inserted-into-tkinter-widget