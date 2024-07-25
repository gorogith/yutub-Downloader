# YouTube Downloader With GUI Python 

YouTube Playlist Downloader adalah aplikasi sederhana berbasis GUI yang memungkinkan Anda mengunduh semua video dari playlist YouTube. Aplikasi ini menggunakan `yt-dlp` untuk mengunduh video dengan kualitas terbaik yang tersedia dan menyimpannya dalam format MP4.

## Fitur
- 📺 Mengunduh semua video dari playlist YouTube
- 🎥 Menggabungkan video dan audio dengan kualitas terbaik
- 🗂️ Menyimpan video dalam folder berdasarkan judul playlist
- 🏷️ Menyimpan video dengan nama file yang berisi indeks video dalam playlist dan judul video

## Persyaratan
- 🐍 Python 3.x
- 🔗 `yt-dlp`
- 🖥️ `tkinter` (biasanya sudah termasuk dalam instalasi Python)

## Instalasi

### Linux
1. **Instal Python:**
   - Gunakan package manager distribusi Linux Anda untuk menginstal Python 3.x. Contoh untuk distribusi berbasis Debian:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **Instal `yt-dlp`:**
   - Jalankan:
     ```bash
     pip3 install yt-dlp
     ```

### Windows
1. **Instal Python:**
   - Unduh dan instal Python dari [python.org](https://www.python.org/downloads/). Pastikan untuk mencentang opsi "Add Python to PATH" selama instalasi.

2. **Instal `yt-dlp`:**
   - Buka Command Prompt dan jalankan:
     ```bash
     pip install yt-dlp
     ```

### macOS
1. **Instal Python:**
   - Instal Python 3.x dari [python.org](https://www.python.org/downloads/) atau menggunakan Homebrew:
     ```bash
     brew install python
     ```

2. **Instal `yt-dlp`:**
   - Buka Terminal dan jalankan:
     ```bash
     pip3 install yt-dlp
     ```

## Penggunaan
1. **Simpan skrip Python berikut ini ke file** (misalnya, `youtube_downloader.py`):

    ```python
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
    ```

2. **Jalankan skrip**:
   - Windows: Buka Command Prompt dan jalankan:
     ```bash
     python youtube_downloader.py
     ```
   - macOS: Buka Terminal dan jalankan:
     ```bash
     python3 youtube_downloader.py
     ```

3. **Ikuti petunjuk pada GUI**:
   - Masukkan URL playlist YouTube dan path folder untuk menyimpan video ketika diminta oleh aplikasi.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](https://opensource.org/licenses/MIT).

---


