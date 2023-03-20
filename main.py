from pytube import YouTube
import customtkinter as tk

def GUI():
    tk.set_appearance_mode('dark')
    tk.set_default_color_theme('dark-blue')

    root = tk.CTk()
    root.title('YouTube downloader')
    root.geometry('600x710')

    frame = tk.CTkFrame(master=root)
    frame.pack(pady=150, padx= 50, fill='both', expand=True)

    label = tk.CTkLabel(master=root, text='Paste link to video and enjoy it later offline!', font=('CTkFont', 20))
    label.pack(padx = 100, pady = 35)

    global entry
    entry = tk.CTkEntry(master=frame, placeholder_text='https://www.youtube.com/...', height=30, width=350)
    entry.pack(padx = 100, pady = 20)

    button = tk.CTkButton(master=root, text='Download', command=ytdown, height=60, width=150, fg_color='darkgreen', hover_color='lightgreen', font=('CTkFont', 18))
    button.pack(padx = 100, pady = 50)

    global pathentry
    pathentry = tk.CTkEntry(master=frame, placeholder_text='Path', height=30, width=350)
    pathentry.pack(padx=100, pady=30)

    root.mainloop()

def ytdown():
    link = entry.get()
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download(pathentry.get())

if __name__=='__main__':
    GUI()

# pyinstaller -F -w -n YouTubeDownloader -i favicon.ico --add-data "c:\users\szymo\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages/customtkinter;customtkinter" main.py