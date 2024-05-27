import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import pygame

class ImageWordGuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("GUESS ME")

        pygame.mixer.init()
        pygame.mixer.music.load('song.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        
        # Menambahkan gambar latar belakang
        background_image = Image.open("BGPANJANG.png")
        self.background_image = ImageTk.PhotoImage(background_image)
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.logo_image = Image.open("LGAP.png")
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(root, image=self.logo_image)
        self.logo_label.pack(pady=50)

        self.start_button = tk.Button(root, text="START GAME", font=("Comic Sans MS", 20, "bold"), command=self.start_game, width=20, height=2, fg= "black", bg= "#FDD67E")
        self.start_button.pack(pady=5)

        # List of images and words to guess
        self.game_data = [
            {"image": "11.png", "word": "penjumlahan"},
            {"image": "7.png", "word": "pengurangan"},
            {"image": "1.png", "word": "perkalian"},
            {"image": "3.png", "word": "pembagian"},
            {"image": "15.png", "word": "kurawal"},
            {"image": "17.png", "word": "kuadrat"},
            {"image": "19.png", "word": "akar"},
            {"image": "21.png", "word": "persentase"},
            {"image": "31.png", "word": "pangkat"},
            {"image": "35.png", "word": "logaritma"},
            {"image": "9.png", "word": "turunan"},
            {"image": "5.png", "word": "faktorial"},
            {"image": "13.png", "word": "subset"},
            {"image": "23.png", "word": "intersection"},
            {"image": "33.png", "word": "epsilon"},
            {"image": "25.png", "word": "pi"},
            {"image": "27.png", "word": "integral"},
            {"image": "29.png", "word": "euler"},
            {"image": "37.png", "word": "union"},
            {"image": "39.png", "word": "elemen"},
            {"image": "41.png", "word": "mutlak"},
            {"image": "43.png", "word": "trigonometri"},
            {"image": "44.png", "word": "sigma"},
            {"image": "46.png", "word": "teta"},
            {"image": "45.png", "word": "lamda"},
            # Add more image-word pairs as needed
        ]

        self.current_index = 0
        self.score = 0  # Inisialisasi skor

        self.image_label = tk.Label(root, image=None)
        self.image_label.pack(pady=50)

        self.entry = tk.Entry(root, font=("Comic Sans MS", 20), justify = "center")
        self.entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Answer", font=("Comic Sans MS", 20), command=self.check_answer, width=20, height=1, fg= "black", bg= "#E4DB8B")
        self.check_button.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: {}".format(self.score), font=("Comic Sans MS", 20),width=20, height=1)
        self.score_label.pack(pady=10)
        
        self.restart_button = tk.Button(root, text="Restart", font=("Comic Sans MS", 14), command=self.restart_game, width=10, height=1, fg="black", bg="#FDD67E")
        self.restart_button.pack(side=tk.LEFT, padx=10)
        
        self.attempts_left = 5
        
        self.exit_button = tk.Button(root, text="Exit", font=("Comic Sans MS", 14), command=root.destroy, width=10, height=1, fg="black", bg="#FDD67E")
        self.exit_button.pack(side=tk.RIGHT, padx=10)


        # Sembunyikan elemen-elemen pada awal
        self.hide_elements()

    def start_game(self):
        self.show_elements()
        self.next_item()

    def restart_game(self):
        # Mengulang permainan dari awal
        self.current_index = 0
        self.score = 0
        self.hide_elements()
        self.logo_label.pack(pady=20)
        self.start_button.pack(pady=10)
    
    def show_elements(self):
        # Menampilkan elemen-elemen yang diperlukan
        self.image_label.pack(pady=45)
        self.entry.pack(pady=12)
        self.check_button.pack(pady=12)
        self.score_label.pack(pady=12)

        # Sembunyikan logo dan tombol "Start Game"
        self.logo_label.pack_forget()
        self.start_button.pack_forget()

    def hide_elements(self):
        # Sembunyikan elemen-elemen yang tidak diperlukan
        self.image_label.pack_forget()
        self.entry.pack_forget()
        self.check_button.pack_forget()
        self.score_label.pack_forget()

        # Tampilkan kembali logo dan tombol "Start Game"
        self.logo_label.pack()
        self.start_button.pack()

    def next_item(self):
        # Check if there are more items to display
        if self.current_index < len(self.game_data):
            # Display the next item
            current_data = self.game_data[self.current_index]
            current_image_path = current_data["image"]
            current_word = current_data["word"]

            img = Image.open(current_image_path)
            img = img.resize((300, 300), resample=Image.BICUBIC)
            img = ImageTk.PhotoImage(img)

            self.image_label.config(image=img)
            self.image_label.image = img
            
            self.entry.delete(0, tk.END)
            
            self.attempts_left = 5
            
            self.current_index += 1
        else:
            # Game Over: Show total score
            tk.messagebox.showinfo("Game Over", "You have guessed all the items!\nTotal Score: {}".format(self.score))

            # Reset the game
            self.current_index = 0
            self.score = 0
            self.hide_elements()
            self.logo_label.pack(pady=20)
            self.start_button.pack(pady=10)

    def check_answer(self):
        user_input = self.entry.get().lower()
        correct_answer = self.game_data[self.current_index - 1]["word"]

        if user_input == correct_answer:
            tk.messagebox.showinfo("CORRECT", "Awesome, you've guessed correctly!")
            self.score += 1  # Score = +1 untuk setiap jawaban benar
            self.score_label.config(text="Score: {}".format(self.score))
            self.next_item()
        else:
            self.attempts_left -= 1  # Kurangi attempts_left
            if self.attempts_left == 0:
                tk.messagebox.showinfo("Correct Answer", "The correct answer is: {}".format(correct_answer))
                self.next_item()
            else:
                tk.messagebox.showerror("TRY AGAIN", "The word has not been arranged correctly yet. {} attempts left.".format(self.attempts_left))

if __name__ == "__main__":
    root = tk.Tk()
    game = ImageWordGuessGame(root)
    root.mainloop()
