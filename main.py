from members import Members
from counting_table import CountingTable
from pair_buddies import PairBuddies
from tkinter import *
from tkinter import Tk, Button, ttk
from tkcalendar import DateEntry

mem = Members()
pair_buddies = PairBuddies()
cnt_table = CountingTable()

# # # # # UI # # # # # #

datesAndMembersList = []

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
        members = getNames.get()
        nameList = list(members.split(','))

        if all(selected_date not in dates for dates in datesAndMembersList):
            # 해당 날짜가 없다면.
            datesAndMembersList.append([selected_date, nameList])
        else:
            # 해당 날짜에 인물이 있는지 확인.
            for name in nameList:
                for index, datesNames in enumerate(datesAndMembersList):
                    # datesNames[0] 은 date, datesNames[1] 은 이
                    if datesNames[0] == selected_date:
                        print("datesNames[1]: " + str(datesNames[1]))
                        if name not in datesNames[1]:
                            if len(datesAndMembersList[index][1]) != 0: datesAndMembersList[index][1].append(name)
                            else:
                                datesAndMembersList[index][1] = [name]

        inputBox.insert('end', selected_date + " " + members + "\n")
    except EXCEPTION as e:
        print(e)


inputBox.pack()


def reset():
    datesAndMembersList.clear()
    mem.resetMembers()
    cnt_table.resetCntTable()
    pair_buddies.resetBuddies()
    text_container_buddies.delete("1.0", "end")
    text_container.delete("1.0", "end")
    inputBox.delete(0, END)


resetBtn = Button(root, text="RESET", command=reset)
resetBtn.pack()

cal = DateEntry(root, date_pattern="yyyy-mm-dd")
cal.pack()

getNames = StringVar()

textbox = ttk.Entry(root, width=30, textvariable=getNames)
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

    pair_buddies.setMembers(mem)
    pair_buddies.setCntTable(cnt_table)
    datesAndMembersList.sort(key = lambda x: len(x[1]))
    pair_buddies.pairUpBuddies(datesAndMembersList)

    printBuddies()
    printTrainingDays()

    pair_buddies.resetBuddies()
    pair_buddies.resetAllOfBuddies()

    cnt_table.resetCntTable()

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
    #cnt_table.countTrainDays(pair_buddies.buddies)
    text_container.tag_config('red', foreground='red')
    text_container.tag_config('green', background='yellow', foreground='green')
    text_container.tag_config('blue', background='blue', foreground='white')

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