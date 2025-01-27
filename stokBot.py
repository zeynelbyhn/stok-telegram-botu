import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from telegram import Bot

# Telegram bot token'ınızı buraya yazın
TOKEN = ''
CHAT_ID = ''  # Botu başlattığınızda kendinize mesaj göndermek için chat_id'yi buraya yazın

# Ürünün sayfasının URL'si
url = ""

# WebDriver'ı başlat
driver = webdriver.Chrome()

# Telegram botuna mesaj göndermek için asenkron fonksiyon
async def send_message(message):
    bot = Bot(token=TOKEN)
    # 'await' ile bot mesajını gönderiyoruz
    await bot.send_message(chat_id=CHAT_ID, text=message)

# Stok kontrolünü yapan asenkron fonksiyon
async def check_stock():
    driver.get(url)
    
    try:
        # Stok durumu ile ilgili bir element arıyoruz (Bu kısmı sayfanın yapısına göre değiştirebilirsiniz)
        stock_element = driver.find_element(By.XPATH, '//*[@id="main"]/article/div[2]/div[1]/div[2]/div/div[3]/button/div/span[2]')
        
        # Eğer element mevcutsa, ürün stokta mevcut demektir
        if stock_element.is_displayed():
            await send_message("Ürün stokta mevcut değil!")
        else:
            await send_message("Ürün stokta mevcut.")
    except Exception as e:
        await send_message(f"Stok durumu kontrol edilirken bir hata oluştu: {e}")

# 2 dakika (120 saniye) aralıklarla stok kontrolü yap
async def main():
    while True:
        await check_stock()
        await asyncio.sleep(2)  # 2 dakika

# Asenkron kodu başlat
asyncio.run(main())

# WebDriver'ı kapatma (Bu satırı asenkron blok bitmeden önce koymamalısınız)
driver.quit()
