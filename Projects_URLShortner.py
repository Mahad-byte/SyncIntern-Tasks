import pyshorteners
import tkinter
from tkinter import font
import threading
from urllib import parse

window = tkinter.Tk()


def ShortenUrl():
    py_short = pyshorteners.Shortener(api_key='dd6f5060fd2b2365aaaf4daf01ef92ca6a260282')
    enter_long_url = enter.get()
    url = parse.urlparse(enter_long_url)
    if not url.scheme and not url.netloc:
        text.insert(tkinter.END, "\nError! That's Not a URL\n")
    else:
        p = py_short.bitly.short(enter_long_url)
        text.insert(tkinter.END, f"\n{p}\n")

    tkinter.Button(window, text='Clear', fg='black', command=lambda :text.delete(1.0, tkinter.END))\
        .grid(row=4, column=0)


def Threading():
    threading.Thread(target=ShortenUrl).start()


if __name__ == '__main__':
    window.geometry('500x300')
    window.title("URL Shortener")
    fontt = font.Font(family="Ariel", size=10, underline=True)
    fonttt = font.Font(family="Ariel", size=10)
    enter = tkinter.Entry(window, width=40)
    enter.grid(row=0, column=0, padx=140, pady=10)
    enterurl = tkinter.Label(window, text='Enter Url:', fg='black', font=fonttt)
    enterurl.grid(row=0, column=0, padx=80, pady=0, sticky='w')
    tkinter.Button(text="Shorten URL", command=Threading).grid(row=1, column=0, padx=0, pady=0)
    tkinter.Label(window, text="Bitly Url's", fg='black', font=fontt).grid(row=2, column=0, padx=0, pady=20)
    text = tkinter.Text(window, height=5, width=30)
    text.grid(row=3, column=0, pady=0, padx=0)
    window.mainloop()
