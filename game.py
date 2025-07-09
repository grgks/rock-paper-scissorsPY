import random
import tkinter as tk
from tkinter import font

class RockPaperScissors:
    def __init__(self):
        self.options = ["rock", "paper", "scissors"]
        self.emoji_map = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
        self.player_win = 0
        self.pc_win = 0
        self.draw = 0

    def play(self, player_choice):
        computer_choice = random.choice(self.options)
        if player_choice == computer_choice:
            self.draw += 1
            return "draw", computer_choice
        elif ((player_choice == "rock" and computer_choice == "scissors") or 
             (player_choice == "paper" and computer_choice == "rock") or 
             (player_choice == "scissors" and computer_choice == "paper")):
            self.player_win += 1
            return "player", computer_choice
        else:
            self.pc_win += 1
            return "computer", computer_choice

    def get_score_text(self):
        return (f"🧑‍💻 You: {self.player_win}   "
                f"🤖 Computer: {self.pc_win}   "
                f"🤝 Draws: {self.draw}")

class RockPaperScissorsApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Rock Paper Scissors 🎮")
        self.geometry("450x350")
        self.resizable(False, False)
        self.configure(bg="#222222")

        self.game = RockPaperScissors()

        self.custom_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.result_font = font.Font(family="Helvetica", size=12)

        self.label_info = tk.Label(self, text="Choose your move:", font=self.custom_font, fg="white", bg="#222222")
        self.label_info.pack(pady=15)

        frame_buttons = tk.Frame(self, bg="#222222")
        frame_buttons.pack(pady=10)

        btn_font = ("Helvetica", 12, "bold")

        # Κουμπιά 
        btn_rock = tk.Button(frame_buttons, text="🪨\nRock", width=8, height=3, font=btn_font,
                             command=lambda: self.player_choice("rock"))
        btn_rock.grid(row=0, column=0, padx=8)

        btn_paper = tk.Button(frame_buttons, text="📄\nPaper", width=8, height=3, font=btn_font,
                              command=lambda: self.player_choice("paper"))
        btn_paper.grid(row=0, column=1, padx=8)

        btn_scissors = tk.Button(frame_buttons, text="✂️\nScissors", width=8, height=3, font=btn_font,
                                 command=lambda: self.player_choice("scissors"))
        btn_scissors.grid(row=0, column=2, padx=8)

        self.label_result = tk.Label(self, text="", font=self.result_font, fg="white", bg="#222222", justify="center")
        self.label_result.pack(pady=20)

        self.label_score = tk.Label(self, text=self.game.get_score_text(), font=self.custom_font,
                                    fg="#00FF00", bg="#222222")
        self.label_score.pack(pady=10)

        btn_quit = tk.Button(self, text="Quit", font=self.custom_font, command=self.quit, bg="#880000", fg="white")
        btn_quit.pack(pady=15)

    def player_choice(self, choice):
        winner, computer_choice = self.game.play(choice)
        player_emoji = self.game.emoji_map[choice]
        comp_emoji = self.game.emoji_map[computer_choice]

        if winner == "player":
            msg = f"You chose {player_emoji} {choice.capitalize()}, computer chose {comp_emoji} {computer_choice}.\n🎉 You win! 🎉"
            self.label_result.config(fg="#00FF00")
        elif winner == "computer":
            msg = f"You chose {player_emoji} {choice.capitalize()}, computer chose {comp_emoji} {computer_choice}.\n💥 Computer wins! 💥"
            self.label_result.config(fg="#FF4444")
        else:
            msg = f"You chose {player_emoji} {choice.capitalize()}, computer chose {comp_emoji} {computer_choice}.\n🤝 It's a draw!"
            self.label_result.config(fg="#FFFF00")

            #Ενημέρωση GUI
        self.label_result.config(text=msg)
        #Ενημερώση  σκορ
        self.label_score.config(text=self.game.get_score_text())

if __name__ == "__main__":
    app = RockPaperScissorsApp()
    # aparaithto gia to event loop tou GUI
    app.mainloop()
