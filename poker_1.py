import tkinter as tk

from tkinter import messagebox as msg

import random



class Card():
    def __init__(self, master, card_name, card_num, n):

        self.card_name = card_name
        self.card_num = card_num
        self.check_hold = n

        self.card_frame = tk.Frame(master)
        self.card_frame.pack(side=tk.LEFT, expand=1)

        self.card_name_label = tk.Label(self.card_frame, text=self.card_name, anchor="center")
        self.card_name_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.card_num_label = tk.Label(self.card_frame, text=self.card_num, anchor="center")
        self.card_num_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.lock_hold = 0
        self.hold_btn = tk.Button(self.card_frame, text='Hold', command=lambda:self.click_hold(self.check_hold))
        self.hold_btn.pack(side=tk.BOTTOM, fill=tk.X)

    def click_hold(self, n):
        if self.lock_hold == 0:
            self.lock_hold = 1
            self.hold_btn.configure(bg='grey')
            win.random_card[2][n] = 1

        else:
            self.lock_hold = 0
            self.hold_btn.configure(bg='lightgrey')
            win.random_card[2][n] = 0


class display_Card():
    def __init__(self, master, card_name, card_num):

        self.card_name = card_name
        self.card_num = card_num

        self.card_frame = tk.Frame(master)
        self.card_frame.pack(side=tk.LEFT, expand=1)

        self.card_name_label = tk.Label(self.card_frame, text=self.card_name, anchor="center")
        self.card_name_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.card_num_label = tk.Label(self.card_frame, text=self.card_num, anchor="center")
        self.card_num_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)



class Win(tk.Tk):
    def __init__(self):
        super().__init__()
#general set
        self.title("poker")
        self.geometry("500x300")
        self.resizable(False, False)

        self.main_frame = tk.Frame(self, height=200)
        self.main_frame.pack(side=tk.TOP, fill=tk.X)

        self.btn_start = tk.Button(self, text="start" ,padx=20, command=self.game_start)
        self.btn_start.pack(side=tk.LEFT ,anchor="s")

        self.btn_ok = tk.Button(self, text="ok", padx=20, command=self.game_ok)
        self.btn_ok.pack(side=tk.LEFT ,anchor="s")

        self.btn_exit = tk.Button(self, text="exit", padx=20, command=quit)
        self.btn_exit.pack(side=tk.RIGHT, anchor="s")

        self.card_name = ['spade', 'heart', 'diamond', 'club']
        self.card_number = ['A', 'J', 'Q', 'K']
        for n in range(2,11):
            self.card_number.append(n)

        self.start_on = 0

        self.game_start_scene()

    def game_start_scene(self):
        self.game_frame = tk.Canvas(self.main_frame, height=200, bg='white')
        self.game_frame.pack_propagate(0)
        self.game_frame.pack(side=tk.TOP, fill=tk.X, anchor='center')

    def game_start(self):
        if self.start_on == 0:
            self.game_frame.destroy()
            self.game_start_scene()

            self.random_card = {}

            self.random_card = [[0 for x in range(5)] for y in range(3)]

            for n in range(0,5):
                self.random_card[0][n] = random.choice(self.card_name)
                self.random_card[1][n] = random.choice(self.card_number)

            repeat_on = 1
            while repeat_on == 1:
                repeat_on=0
                for n in range(0,4):
                    for j in range((n+1),5):
                        if (self.random_card[0][n]==self.random_card[0][j]) & (self.random_card[1][n]==self.random_card[1][j]):
                            self.random_card[0][j] = random.choice(self.card_name)
                            self.random_card[1][j] = random.choice(self.card_number)
                            repeat_on = 1

            for n in range(0,5):
                btn = Card(self.game_frame, self.random_card[0][n], self.random_card[1][n], n)

            self.start_on = 1

    def game_ok(self):
        if self.start_on == 1:

            for n in self.random_card[2]:
                if n == 0:
                    self.random_card[0][n] = random.choice(self.card_name)
                    self.random_card[1][n] = random.choice(self.card_number)

            self.game_frame.destroy()
            self.game_start_scene()

            for n in range(0,5):
                    btn = display_Card(self.game_frame, self.random_card[0][n], self.random_card[1][n])

            self.check_pair = []

            for pt in self.random_card[0]:
                if self.random_card[0].count(pt) != 5:
                    for num in self.random_card[1]:
                        self.check_pair.append(self.random_card[1].count(num))

                    if (2 in self.check_pair)&(3 in self.check_pair):
                        msg.showinfo("Poker Hands", "Full hoouse")
                    elif 4 in self.check_pair:
                        msg.showinfo("Poker Hands", "four of kind")
                    elif 3 in self.check_pair:
                        msg.showinfo("Poker Hands", "Three of kind")
                    elif self.check_pair.count(2) ==4 :
                        msg.showinfo("Poker Hands", "two pair")
                    elif 2 in self.check_pair:
                        msg.showinfo("Poker Hands", "One pair")
                    else:
                        msg.showinfo("Poker Hands", "no pair")

                    self.start_on = 0

                    break


                else:
                    msg.showinfo("Poker Hands", "Flush")
                    break




if __name__ == "__main__":
    win = Win()
    win.mainloop()

