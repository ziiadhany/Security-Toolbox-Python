import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    if len(password) < 8:
        return "ضعيفة جداً"
    has_digit = False
    has_upper = False
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
    if has_digit and has_upper:
        return "قوية"
    elif has_digit or has_upper:
        return "متوسطة"
    else:
        return "ضعيفة"

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def handle_strength():
    pwd = entry_pwd.get()
    if not pwd:
        messagebox.showwarning("تنبيه", "برجاء إدخال كلمة سر!")
        return
    res = check_password_strength(pwd)
    lbl_res_pwd.config(text=f"النتيجة: {res}", fg="blue")

def handle_cipher():
    try:
        text = entry_text.get()
        shift = int(entry_shift.get())
        encrypted = caesar_cipher(text, shift)
        lbl_res_cipher.config(text=f"النص المشفر: {encrypted}")
    except ValueError:
        messagebox.showerror("خطأ", "برجاء إدخال رقم صحيح في خانة الإزاحة!")

root = tk.Tk()
root.title("Suez National University - Security Toolbox")
root.geometry("400x500")

tk.Label(root, text="Suez National University", font=("Arial", 10, "italic"), fg="gray").pack()
tk.Label(root, text="أداة الحماية البرمجية", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="فاحص قوة كلمة السر:").pack()
entry_pwd = tk.Entry(root, show="*")
entry_pwd.pack(pady=5)
tk.Button(root, text="افحص الآن", command=handle_strength).pack()
lbl_res_pwd = tk.Label(root, text="")
lbl_res_pwd.pack(pady=5)

tk.Canvas(root, height=1, bg="lightgray").pack(fill="x", pady=10, padx=20)

tk.Label(root, text="مشفر النصوص (Caesar Cipher):").pack()
entry_text = tk.Entry(root)
entry_text.pack(pady=5)
tk.Label(root, text="مقدار الإزاحة (رقم):").pack()
entry_shift = tk.Entry(root, width=5)
entry_shift.pack()
tk.Button(root, text="تشفير النص", command=handle_cipher).pack(pady=10)
lbl_res_cipher = tk.Label(root, text="")
lbl_res_cipher.pack()

root.mainloop()