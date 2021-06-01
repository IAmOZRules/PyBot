from tkinter import *
from chat import get_response, bot_name

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
    
    def run(self):
        self.window.mainloop()
    
    def _setup_main_window(self):
        self.window.title("PyBot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=700, height=500, bg="#001437")

        # Head Label
        label_header = f"Hello, there! I am {bot_name}! Type 'exit' to stop chatting...!\n"
        head_label = Label(self.window, bg="#001437", fg="#B8FB3C", text=label_header, font="AdHoc 15", pady=0, bd=2)
        head_label.place(relwidth=1)

        # Divider
        line = Label(self.window, width=450, bg="#ABB2B9")
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Text widget
        self.text_widget = Text(self.window, width=20, height=2, bg="#D1D2D0", fg="#000000", font="Constantia 12",
                                padx=10, pady=10, spacing1=2, spacing2=1, spacing3=1)
        self.text_widget.place(relheight=0.75, relwidth=1, rely=0.072)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Bottom Label
        bottom_label = Label(self.window, bg="#B8FB3C", height=3, padx=5, pady=5)
        bottom_label.place(relwidth=1, rely=0.825)

        # Message Entry Box
        self.msg_entry = Entry(bottom_label, font="Constantia 12", bd=3, highlightbackground ="black", highlightcolor="black")
        
        self.msg_entry.place(relwidth=0.74, relheight=0.9, rely=0.012, relx=0.01)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Send Button
        send_button = Button(bottom_label, text="Send", font="Constantia 14 bold", width=20, bg="#ABB2B9", 
                             bd=3, highlightbackground ="white", highlightcolor="white",
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.012, relheight=0.9, relwidth=0.22)
    
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
    
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        if msg == "exit":
            self.window.destroy()
        
        else:
            self.text_widget.tag_config("you", background="#5CE5D5", font=("AdHoc 13"))
            self.text_widget.tag_config("chatbot", background="#7898FB", font=("AdHoc 13"))

            self.msg_entry.delete(0, END)
            msg1_sender = f"{sender}:"
            msg1_msg = f" {msg}\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg1_sender, "you")
            self.text_widget.insert(END, msg1_msg)
            self.text_widget.configure(state=DISABLED)

            msg2_bot = f"{bot_name}:"
            msg2_msg = f" {get_response(msg)}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg2_bot, "chatbot")
            self.text_widget.insert(END, msg2_msg)
            self.text_widget.configure(state=DISABLED)

            self.text_widget.see(END)