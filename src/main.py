import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import json

def get_response(driver, target_url):
    try:
        driver.get(target_url)
        driver.implicitly_wait(4)
        response = driver.requests[-1]

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        with open('response.html', "w", encoding='utf-8') as file:
            file.write(str(soup.prettify()))

    except Exception as e:
        print(f'An error occured: {e}')
        soup = None

    return soup

def main():
    driver = None
    try:
        target_url = "https://www.yell.com/ucs/UcsSearchAction.do?keywords=hotels&location=uk&scrambleSeed=396192646&pageNum=1"
        
        # Opsi WebDriver
        options = uc.ChromeOptions()
        
        # Muat ekstensi Browsec VPN
        options.add_extension('D:\\program\\Browsec-VPNFree-VPN-for-Chrome.crx')
        
        # Buat profil Chrome baru
        options.add_argument("--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
        
        # Tambahkan beberapa opsi tambahan untuk membantu mengatasi masalah koneksi
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        driver = uc.Chrome(options=options)
        
        soup = get_response(driver, target_url)
    except Exception as e:
        print(f'An error occured.... {e}')
    finally:
       if driver is not None:
           driver.quit()

if __name__ == "__main__":
    main()
