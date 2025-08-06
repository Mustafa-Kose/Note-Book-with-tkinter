import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

saveonloadpath=None
#save/load
def save():#kayıt lanı
    global saveonloadpath
    if saveonloadpath is None:
        thepath=filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt")])
        if not thepath:#iptal ederse patlamayalım diye
            return
        saveonloadpath=thepath
    text=txtplace.get("1.0",tk.END).strip()
    messege_in_label=tk.Label(window,text="",fg="green")
    messege_in_label.pack(side="bottom",pady=2)
    try:
            
        with open(saveonloadpath,"w",encoding="utf-8") as file:
            file.write(text)
        messagebox.showinfo("Saved!","The note has saved.")
        
    except Exception as eror:
        messagebox.showerror("Eror",eror)        

def load():#yükleme alanı
    global saveonloadpath
    thepath=filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not thepath:
        return
    try:
        with open(thepath, "r", encoding="utf-8") as text:
            insidetxt=text.read()
            txtplace.delete("1.0",tk.END)
            txtplace.insert("1.0",insidetxt)
        saveonloadpath=thepath
    except Exception as eror:
        print("Eror", eror)

#Başlık çubuğu defleri
def close():
    window.destroy()

def start_move_araund(e):
    window.x=e.x
    window.y=e.y

def stop_move_araund(e):
    window.x=None
    window.y=None

def move_araund(e):
    x=e.x_root - window.x
    y=e.y_root - window.y
    window.geometry(f"+{x}+{y}")

#GUI açıyoruz/ayarlıyoruz
window=tk.Tk()
window.title("NoteBook")
window.geometry("500x600")
window.configure(bg="#2e2e2e")

#Titlebar özelleştirme
window.overrideredirect(True)
titlebar=tk.Frame(window, bg="#1f1f1f", relief="raised", bd=0, height=30)
titlebar.pack(fill="x", side="top")

label_title=tk.Label(titlebar, text="NoteBook", bg="#1f1f1f",
                     fg="white", font=("segoe UI", 10))
label_title.pack(side="left", padx=10)

close_button=tk.Button(titlebar,text="✕", command=close, bg="#1f1f1f",
                       fg="white", bd=10, activebackground="#ff5555",
                       activeforeground="white")
close_button.pack(side="right", padx=0, pady=0)

titlebar.bind("<ButtonPress-1>", start_move_araund)
titlebar.bind("<B1-Motion>", move_araund)
#Shortcuts
window.bind("<Control-s>", lambda shortcut: save())
window.bind("<Control-l>", lambda shortcut: load())

#sbitleme
frame_button=tk.Frame(window, bg="#2e2e2e")
frame_button.pack(side="bottom",fill="x")

#Sıra tuşlarda
save_button=tk.Button(frame_button, text="Save", command=save,
                      width=5, height=2, bg="gray20", fg="white",
                      activebackground="gray40", 
                      highlightbackground="white", highlightthickness=1) 
save_button.pack(side=tk.LEFT, padx=5, pady=5)

load_button=tk.Button(frame_button, text="Load", command=load,
                      width=5, height=2,
                      bg="gray20", fg="white",
                      activebackground="gray40", 
                      highlightbackground="white", highlightthickness=1)
load_button.pack(side=tk.RIGHT, padx=5, pady=5)

#txt alanı
frame_txt=tk.Frame(window,bg="#2e2e2e")
frame_txt.pack(fill="both", expand=True)

txtplace=tk.Text(frame_txt, wrap=tk.WORD,bg="#292626",fg="white",
                 insertbackground="white",
                 relief="flat", bd=0)

#scroolbar
scrollbar = tk.Scrollbar(frame_txt,
                         orient="vertical", command=txtplace.yview, width=0,
                         troughcolor="#000000", bg="#000000",
                         activebackground="#000000",
                         highlightthickness=0, bd=0)

scrollbar.pack(side="right",fill="x")
txtplace.config(yscrollcommand=scrollbar.set)
txtplace.pack(fill="both", expand=True)

#Başlatttt
window.mainloop()
