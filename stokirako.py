import tkinter as tk

root = tk.Tk()
root.geometry("400x500")
root.title("Szókirakó")
lable =tk.Label(root, text="szókirakó játék", font=('Calibri',18))
lable.pack(padx=20,pady=20)
textBox= tk.Entry(root,)
textBox.pack()
Button=tk.Button(root,text="Ellenőrzés",font=('Calibri',13))
Button.pack(padx=10,pady=10)


root.mainloop()