import tkinter
import tkinter.filedialog
from tkinter import *
from tkinter.messagebox import *
from first import startSql
class App:
    def __init__(self, root):
        root.title('English to SQL')
        root.bind('<Return>', self.parse)

        self.sentence_frame = LabelFrame(root, text="Input Sentence", padx=0, pady=5)
        self.sentence_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        self.input_sentence_string = StringVar()
        self.input_sentence_string.set("Enter a sentence...")
        self.input_sentence_entry = Entry(self.sentence_frame, textvariable=self.input_sentence_string, width=80)
        self.input_sentence_entry.pack()
        self.input_sentence_entry.bind('<Button-1>', self.clearEntry)


        self.output_frame = LabelFrame(root, text="Output Query", padx=0, pady=5)
        self.output_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        self.output_string = StringVar()
        # self.output_entry = Entry(self.output_frame, textvariable=self.output_string, width=80)
        self.output_entry = Text(self.output_frame, height = 3, width = 60)
        self.output_entry.pack()

        self.go_button = Button(root, text="Go!", command=self.lanch_parsing)
        self.go_button.pack(side="right", fill="both", expand="yes", padx=10, pady=2)

        self.reset_button = Button(root, text="Reset", fg="red", command=self.reset_window)
        self.reset_button.pack(side="right", fill="both", expand="yes", padx=10, pady=2)

    def clearEntry(self, event):
        self.input_sentence_string.set("")

    def parse(self, event):
        self.lanch_parsing()

    def reset_window(self):
        self.input_sentence_string.set("Enter a sentence...")
        return

    def lanch_parsing(self):
        try:
            db = "db.sql"
            query = self.input_sentence_string.get()
            generatedSql = startSql(str(query), str(db))
            # showinfo('Result', generatedSql)
            self.output_entry.insert(END, generatedSql)
            # self.output_string.set(generatedSql)

        except Exception as e:
            showwarning('Error', e)
        return


root = Tk()
App(root)
root.geometry("500x200")
root.resizable(width=TRUE, height=FALSE)
root.mainloop()
