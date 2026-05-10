from parser import parselinks
from browser import getpage, createdriver
from downloader import download, choosetype
import time

def main():
    url = input("Input AO3 link\n")
    driver = createdriver()
    print("Driver was created")
    html = getpage(driver, url)
    print("Page loaded successfully")
    links = parselinks(html)
    filetype = choosetype()
           
    for link in links:
        download(driver, link, filetype)
        print("Download has started")
        time.sleep(2)
        print('Download in progress...')
        

    print("Download completed! Thank you for using AO3 downloader:)")

if __name__ == "__main__":
    main()