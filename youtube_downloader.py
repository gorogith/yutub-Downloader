import yt_dlp
import tkinter as tk
from tkinter import simpledialog, messagebox

def download_playlist_videos(url, output_path='.'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def start_download():
    url = simpledialog.askstring("Input", "Masukkan URL playlist YouTube:")
    if not url:
        messagebox.showerror("Error", "URL tidak boleh kosong!")
        return
    
    output_directory = simpledialog.askstring("Input", "Masukkan path folder untuk menyimpan video:")
    if not output_directory:
        output_directory = '.'

    try:
        download_playlist_videos(url, output_directory)
        messagebox.showinfo("Success", "Semua video dalam playlist berhasil diunduh!")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal mengunduh video: {str(e)}")

# Membuat GUI dengan tkinter
root = tk.Tk()
root.withdraw()  # Menyembunyikan jendela utama

messagebox.showinfo("Welcome", "Selamat datang di YouTube Playlist Downloader")

start_download()
