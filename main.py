import os  # Mengimpor modul 'os' untuk berinteraksi dengan sistem operasi (seperti membaca variabel lingkungan)
from dotenv import load_dotenv  # Mengimpor fungsi untuk membaca file .env yang berisi token rahasia
from telegram import Update  # Mengimpor kelas 'Update' yang membawa data dari Telegram (seperti chat baru)
from telegram.ext import Application, CommandHandler, ContextTypes  # Mengimpor alat pembuat bot dan pengatur perintah

# Memuat isi file .env ke dalam sistem agar program bisa membaca variabel di dalamnya
load_dotenv()

# Mengambil kode unik (token) bot Anda dari file .env agar bot bisa terhubung ke Telegram
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Fungsi 'start' ini adalah instruksi apa yang dilakukan bot saat user mengetik /start
# 'update' berisi data pesan user, 'context' adalah alat bantu tambahan dari library Telegram
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Memerintahkan bot untuk membalas pesan user dengan teks "New Bot"
    await update.message.reply_text("New Bot")

# Fungsi utama tempat semua persiapan bot dilakukan
def main():
    # Pengecekan keamanan: apakah token sudah ada? Jika tidak, beri tahu pengguna
    if not TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN not found. Please set it in the .env file.")
        return
    
    # Membangun aplikasi bot menggunakan token yang sudah didapatkan
    application = Application.builder().token(TOKEN).build()

    # Memberitahu bot: "Jika ada orang mengetik /start, jalankan fungsi 'start' yang kita buat di atas"
    application.add_handler(CommandHandler("start", start))
    
    # Memberi informasi ke layar bahwa bot telah aktif
    print("Bot Started (Polling)...")

    # Menjalankan bot dalam mode 'polling' (bot akan terus mengecek pesan baru dari Telegram secara otomatis)
    application.run_polling()

# Ini adalah bagian yang memberitahu Python untuk menjalankan fungsi 'main' saat file ini dimulai
if __name__ == "__main__":
    main()