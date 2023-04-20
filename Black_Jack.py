from tkinter import *
import random


koloda = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'туз'] * 24
for i in range(3):
    random.shuffle(koloda)

file = open('Money.csv', 'r')
for i in file:
    money = i
file.close()


window = Tk()
window.geometry('800x800')
window.resizable(False, False)
window.title('Black Jack')

# Иконка
# icon = PhotoImage(file='black_jack.png')
# window.iconphoto(False, icon)

# Добавление фона
window.configure(bg='#228B22')

# Шапка
lb_1 = Label(text='Black Jack', font=('Terminal', 30, 'bold'), height=2,
             bg='black', fg='white')
lb_1.pack(side=TOP, fill=X)


# Выполнение команд
def deal():
    lb_no_stavka['text'] = ''
    lb_num_player['text'] = 0
    point_player = 0
    lb_result['text'] = ''
    bet = entry_box.get()
    if (bet == '') or (bet == str(0)):
        lb_no_stavka['text'] = 'You didnt bet'
        lb_no_stavka['fg'] = 'red'
        entry_box.delete(0, END)
        return
    karta = koloda.pop()
    if karta == 'туз':
        karta = 11
    point_krup = karta
    lb_num_krup['text'] = point_krup
    for i in range(2):
        karta = koloda.pop()
        if karta == 'туз':
            karta = 11
            if (point_player + karta) > 21:
                karta = 1
        point_player += karta
        lb_num_player['text'] = point_player



def more():
    point_player = lb_num_player['text']
    karta = koloda.pop()
    if karta == 'туз':
        karta = 11
        if (point_player + karta) > 21:
            karta = 1
    point_player += karta
    lb_num_player['text'] = point_player
    if point_player > 21:
        bet = entry_box.get()
        bet = int(bet)
        lb_result['text'] = 'Lose'
        lb_result['fg'] = 'red'
        file = open('Money.csv', 'r')
        for i in file:
            i = int(i) - bet
            money = i
        file.close()
        file = open('Money.csv', 'w')
        file.write(str(money))
        file.close()
        lb_money['text'] = money
        entry_box.delete(0, END)



def stop():
    point_krup = lb_num_krup['text']
    point_player = lb_num_player['text']
    karta = koloda.pop()
    if karta == 'туз':
        karta = 11
        if (point_krup + karta) > 21:
            karta = 1
    point_krup += karta
    lb_num_krup['text'] = point_krup

    while point_krup < 17:
        karta = koloda.pop()
        if karta == 'туз':
            karta = 11
            if (point_krup + karta) > 21:
                karta = 1
        point_krup += karta
        lb_num_krup['text'] = point_krup

    if (point_krup > point_player) and (point_krup <= 21):
        lb_result['text'] = 'Lose'
        lb_result['fg'] = 'red'
        lb_result.place(x=340, y=365)
        bet = entry_box.get()
        bet = int(bet)
        file = open('Money.csv', 'r')
        for i in file:
            i = int(i) - bet
            money = i
        file.close()

        file = open('Money.csv', 'w')
        file.write(str(money))
        file.close()
        lb_money['text'] = money
        entry_box.delete(0, END)

    elif point_krup == point_player:
        lb_result['text'] = 'Draw'
        lb_result['fg'] = '#A9A9A9'

    elif (point_krup < point_player) or (point_krup > 21):
        lb_result['text'] = 'Winner'
        lb_result['fg'] = 'yellow'
        lb_result.place(x=315, y=365)
        bet = entry_box.get()
        bet = int(bet)
        file = open('Money.csv', 'r')
        for i in file:
            i = int(i) + bet
            money = i
        file.close()

        file = open('Money.csv', 'w')
        file.write(str(money))
        file.close()
        lb_money['text'] = money
        entry_box.delete(0, END)


# Крупье
lb_krup = Label(text='Cropier', font=('Terminal', 30, 'bold'), bg='#228B22')
lb_krup.place(x=330, y=200)

lb_num_krup = Label(text=0, font=('Microsoft Sans Serif', 20,), bg='#A9A9A9')
lb_num_krup.place(x=375, y=260, width=50, height=50)

# Игрок
lb_player = Label(text='Player', font=('Terminal', 30, 'bold'), bg='#228B22')
lb_player.place(x=337, y=500)

lb_num_player = Label(text=0, font=('Microsoft Sans Serif', 20,), bg='#A9A9A9')
lb_num_player.place(x=375, y=560, width=50, height=50)

# Деньги
lb_money = Label(text=money, font=('Terminal', 25,), bg='#228B22')
lb_money.place(x=150, y=100)


# Слово Банк
lb_bank = Label(text='Bank $', font=('Terminal', 25), bg='#228B22')
lb_bank.place(x=20, y=100)

# Надпись результата
lb_result = Label(text='', font=('Terminal', 40, 'bold'), bg='#228B22')
lb_result.place(x=340, y=365)

# Кнопки
bt_start = Button(text='deal', font=('Terminal', 30), bg='#A9A9A9', command=deal)
bt_start.place(x=325, y=650, width=150, height=50)

bt_more = Button(text='more', font=('Terminal', 30), bg='#A9A9A9', command=more)
bt_more.place(x=150, y=650, width=150, height=50)

bt_stop = Button(text='stop', font=('Terminal', 30), bg='#A9A9A9', command=stop)
bt_stop.place(x=500, y=650, width=150, height=50)

# Ставка
entry_box = Entry(text=0, font=('Terminal', 20), bg='#A9A9A9')
entry_box.place(x=300, y=740, height=40)
entry_box.focus()

lb_bet = Label(text='Bet', font=('Terminal', 30), bg='#228B22')
lb_bet.place(x=220, y=736)

lb_dollar = Label(text='$', font=('Terminal', 30), bg='#228B22')
lb_dollar.place(x=520, y=736)

# Надпись того что не сделана ставка
lb_no_stavka = Label(text='', font=('Terminal', 40, 'bold'), bg='#228B22')
lb_no_stavka.place(x=220, y=365)


window.mainloop()