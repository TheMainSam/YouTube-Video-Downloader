try:
    from pytube import YouTube
    from pytube import Playlist
    from tkinter import *
    from tkinter import messagebox
    from pathlib import Path
    import time
except Exception as e:
    print("Some Modules are Missing {}".format(e))

root = Tk()
root.title('YouTube Video Downloader')
root.resizable(False, False)
root.iconbitmap('YouTube.ico')
root.geometry('800x600')

def Clear_Text():
    Enter_URL.delete(0, 'end')

def Download():
    if len(Enter_URL.get()) == 0:
        Enter_URL.config(highlightbackground = "#ff272d", highlightcolor= "#ff272d")
        messagebox.showerror("YouTube Video Downloader", "Error: URL not specified.")

    else:
        Enter_URL.config(highlightbackground = "#7ed214", highlightcolor= "#7ed214")

        Video_URL = Enter_URL.get()

        try:
            YT = YouTube(Video_URL)
            Title = YT.title
            Video = YT.streams.first()
            Downloads_Path = str(Path.home() / "Downloads")
            Video.download(Downloads_Path)

            Downloaded = Label(Frame2, text = f"[{time.strftime('%H:%M:%S', time.localtime())}] {Title}", bg = 'black', fg = 'green', font = ('Lucida Console', 10), anchor = 'nw', justify = 'left', bd = 4)
            Downloaded.place(relwidth = 1, relheight = 1)
            Clear_Text()

        except:
            if Enter_URL.get().startswith('https://www.youtube.com/watch?v='):
                Error = Label(Frame2, text = f"[{time.strftime('%H:%M:%S', time.localtime())}] The download link not found.", bg = 'black', fg = 'red', font = ('Lucida Console', 10), anchor = 'nw', justify = 'left', bd = 4)
                Error.place(relwidth = 1, relheight = 1)
                Enter_URL.config(highlightbackground = "#ff272d", highlightcolor= "#ff272d")
                Clear_Text()

            else:
                Error = Label(Frame2, text = f"[{time.strftime('%H:%M:%S', time.localtime())}] Invalid Request.", bg = 'black', fg = 'red', font = ('Lucida Console', 10), anchor = 'nw', justify = 'left', bd = 4)
                Error.place(relwidth = 1, relheight = 1)
                Enter_URL.config(highlightbackground = "#ff272d", highlightcolor= "#ff272d")
                Clear_Text()

Frame1 = Frame(root, bg = '#f9f9f9', bd = 5)
Frame1.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

Enter_URL = Entry(Frame1, font = 40, relief="flat", highlightthickness=4)
Enter_URL.place(relwidth = 0.65, relheight = 1)
Enter_URL.config(highlightbackground = "#7ed214", highlightcolor= "#7ed214")

Download_Button = Button(Frame1, text = 'Download', bg = '#7ed214', fg = 'white', font = 40, relief = 'flat', command = Download)
Download_Button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

Frame2 = Frame(root, bg = 'black', bd = 10)
Frame2.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

root.mainloop()