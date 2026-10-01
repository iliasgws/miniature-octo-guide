import tkinter as app

notes = app.Tk()
notes.title("Mes Notes")
notes.geometry("700x500")
notes.config(bg="green")

cadre = app.Frame(notes, bg="green")
cadre.place(relx=0.5, rely=0.1, anchor="center")

app.Label(cadre, text="Nom d'utilisateur", bg="green", fg="white").grid(row=0, column=0, sticky="e", padx=10, pady=8)
champ_nom = app.Entry(cadre)
champ_nom.grid(row=0, column=1, padx=10, pady=8)

notes.mainloop()
