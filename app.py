import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Generate QR Function
def generate_qr():
    data = text_input.get()

    if data == "":
        messagebox.showerror("Error", "Please enter text or URL")
    else:
        qr = qrcode.make(data)
        qr.save("my_qr.png")
        messagebox.showinfo("Success", "QR Code Generated Successfully!")

# Main Window
root = Tk()

# Window Title
root.title("QRJay - QR Code Generator")

# Window Size
root.geometry("450x500")


# Background Color
root.configure(bg="white")

# ===== LOGO =====
img = Image.open("logo.png")
img = img.resize((175, 175 ), Image.ANTIALIAS)

logo = ImageTk.PhotoImage(img)

logo_label = Label(root, image=logo, bg="white")
logo_label.pack(pady=10)

# ===== HEADING =====
heading = Label(
    root,
    text="QR Code Generator",
    font=("Arial", 22, "bold"),
    fg="#6A0DAD",
    bg="white"
)

heading.pack(pady=5)

# ===== INPUT BOX =====
text_input = Entry(
    root,
    width=35,
    font=("Arial", 14),
    bd=3
)

text_input.pack(pady=25)

# ===== BUTTON =====
generate_btn = Button(
    root,
    text="Generate QR",
    command=generate_qr,
    font=("Arial", 14, "bold"),
    bg="#6A0DAD",
    fg="white",
    padx=20,
    pady=8,
    cursor="hand2"
)

generate_btn.pack()

# ===== FOOTER =====
footer = Label(
    root,
    text="Developed by QRJay",
    font=("Arial", 10),
    bg="white",
    fg="gray"
)

footer.pack(side=BOTTOM, pady=15)

# Run App
root.mainloop()