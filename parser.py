from bs4 import BeautifulSoup as bs

def parselinks(html):

    pars = bs(html, "lxml")

    lim = int(input("Input download limit\n"))
    if (lim == 0):
        works = pars.find("ol", class_="work index group").find_all("h4", class_="heading")
        links = []
        for work in works:
            link = work.find("a")
            links.append('https://archiveofourown.org' + link.get('href'))
        return links
    elif (lim > 0):
        works = pars.find("ol", class_="work index group").find_all("h4", class_="heading", limit=lim)
        links = []
        for work in works:
            link = work.find("a")
            links.append('https://archiveofourown.org' + link.get('href'))
        return links

