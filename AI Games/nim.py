import tkinter as tk
from tkinter import messagebox
import math

# ---------------- Minimax algorithm ----------------
def minimax(stones, max_take, is_ai_turn):
    if stones == 0:
        return -1 if is_ai_turn else 1

    if is_ai_turn:
        max_eval = -math.inf
        for take in range(1, min(max_take, stones) + 1):
            score = minimax(stones - take, max_take, False)
            max_eval = max(max_eval, score)
        return max_eval
    else:
        min_eval = math.inf
        for take in range(1, min(max_take, stones) + 1):
            score = minimax(stones - take, max_take, True)
            min_eval = min(min_eval, score)
        return min_eval

# ---------------- AI move ----------------
def ai_turn(stones, max_take):
    best_score = -math.inf
    best_take = 1
    for take in range(1, min(max_take, stones) + 1):
        score = minimax(stones - take, max_take, False)
        if score > best_score:
            best_score = score
            best_take = take
    return best_take

# ---------------- GUI Game Class ----------------
class NimGameGUI:
    def __init__(self, root, total_stones=15, max_take=3):
        self.root = root
        self.root.title("Nim Game (Minimax AI)")
        self.root.geometry("400x450")
        self.root.config(bg="#d9e4f5")

        self.total_stones = total_stones
        self.max_take = max_take
        self.stones = total_stones
        self.human_turn = True

        # Title label
        self.title_label = tk.Label(root, text="🎮 Nim Game (You vs AI)", font=("Arial", 16, "bold"), bg="#d9e4f5")
        self.title_label.pack(pady=10)

        # Stones display
        self.stone_label = tk.Label(root, text="", font=("Arial", 20), bg="#d9e4f5")
        self.stone_label.pack(pady=10)
        self.update_stones_display()

        # Button frame
        self.button_frame = tk.Frame(root, bg="#d9e4f5")
        self.button_frame.pack(pady=20)

        # Create take buttons
        for i in range(1, max_take + 1):
            btn = tk.Button(self.button_frame, text=f"Take {i}", width=10, font=("Arial", 12),
                            command=lambda x=i: self.human_move(x))
            btn.grid(row=0, column=i - 1, padx=5)

        # Restart button
        self.restart_btn = tk.Button(root, text="Restart Game", font=("Arial", 12, "bold"),
                                     command=self.restart_game, bg="#9eb7e5")
        self.restart_btn.pack(pady=10)

        # Info label
        self.info_label = tk.Label(root, text="Your turn!", font=("Arial", 13, "italic"), bg="#d9e4f5", fg="green")
        self.info_label.pack(pady=5)

    # Update stone display
    def update_stones_display(self):
        stones_str = " ".join(["🪨" for _ in range(self.stones)])
        self.stone_label.config(text=f"Stones left: {self.stones}\n{stones_str}")

    # Human move
    def human_move(self, take):
        if not self.human_turn:
            return

        if take > self.stones:
            messagebox.showinfo("Invalid", f"You can only take up to {self.stones} stones.")
            return

        self.stones -= take
        self.update_stones_display()

        if self.stones == 0:
            messagebox.showinfo("Game Over", "You took the last stone. You lose! 😢\nAI wins!")
            self.disable_buttons()
            return

        self.human_turn = False
        self.info_label.config(text="AI is thinking...", fg="red")
        self.root.after(1000, self.ai_move)

    # AI move
    def ai_move(self):
        take = ai_turn(self.stones, self.max_take)
        self.stones -= take
        self.update_stones_display()

        messagebox.showinfo("AI Move", f"AI took {take} stone(s).")

        if self.stones == 0:
            messagebox.showinfo("Game Over", "AI took the last stone. AI loses! 🎉\nYou win!")
            self.disable_buttons()
            return

        self.human_turn = True
        self.info_label.config(text="Your turn!", fg="green")

    # Disable all buttons
    def disable_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.config(state="disabled")

    # Restart game
    def restart_game(self):
        self.stones = self.total_stones
        self.human_turn = True
        for widget in self.button_frame.winfo_children():
            widget.config(state="normal")
        self.update_stones_display()
        self.info_label.config(text="Your turn!", fg="green")


# ---------------- Run Game ----------------
if __name__ == "__main__":
    root = tk.Tk()
    game = NimGameGUI(root)
    root.mainloop()
