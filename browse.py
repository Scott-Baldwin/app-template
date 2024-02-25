import tkinter as tk
from tkinter import filedialog


def file_browse(multiple=False, **args):
    root = tk.Tk()
    root.withdraw()
    if multiple:
        path = filedialog.askopenfilenames(**args)
    else:
        path = filedialog.askopenfilename(**args)
    root.destroy()
    return path if path != "" else None


def folder_browse(**args):
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory(**args)
    root.destroy()
    return path if path != "" else None


if __name__ == "__main__":
    # tests
    filetypes = [("Fit File", "*fit.csv"), ("All Files", "*")]
    # path = file_browse(filetypes=filetypes)
    # path = file_browse(multiple=True, filetypes=filetypes)
    path = folder_browse()
    print("!") if path is None else print(path)
