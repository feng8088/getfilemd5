import tkinter as tk
import threading
import hashlib
import pyperclip
from tkinter import filedialog, messagebox

root = tk.Tk()
root.geometry("400x100")


def select_path():
    path = filedialog.askopenfilename()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, path)


def get_md5():
    path = path_entry.get()
    result_entry.delete(0, tk.END)
    result_entry.insert(0, '获取中...')

    t = threading.Thread(target=calc_md5, args=(path, result_entry))
    t.start()


def calc_md5(path, result_entry):
    m = hashlib.md5()
    with open(path, 'rb') as f:
        m.update(f.read())
    md5 = m.hexdigest()
    root.after(100, lambda: result_entry.delete(0, tk.END) or result_entry.insert(0, md5))


def copy_md5():
    pyperclip.copy(result_entry.get())
    messagebox.showinfo('Info', '成功复制到剪切板')


tk.Label(root, text='File Path').grid(row=0, column=0)

path_entry = tk.Entry(root, width=35)
path_entry.grid(row=0, column=1)

tk.Button(root, text='浏览..', command=select_path).grid(row=0, column=2)

tk.Button(root, text='获取MD5', command=get_md5).grid(row=1, column=0)

result_entry = tk.Entry(root, width=35)
result_entry.grid(row=1, column=1)

tk.Button(root, text="复制", command=copy_md5).grid(row=1, column=2)





root.title("文件MD5获取工具 - 爱思考吧")

root.mainloop()