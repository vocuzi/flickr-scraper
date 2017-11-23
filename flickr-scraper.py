def link_download(keyword):
    from selenium import webdriver
    from time import sleep, time
    from urllib import urlretrieve
    from bs4 import BeautifulSoup
    print "[!!] I START :P"
    driver = webdriver.PhantomJS()
    fp = open(keyword+"-flickr-links.txt")
    links = fp.read().split("\n")
    for link in links:
        driver.get("https://www.flickr.com"+link+"sizes/l/")
        print "[+] Waiting for 5 Seconds"
        sleep(5)
        pagesource = driver.page_source
        soup = BeautifulSoup(pagesource, 'html.parser')
        soup = soup.findAll("div",{"id":"allsizes-photo"})
        for image in soup:
            linkurl = image.findAll("img")[0]["src"]
            urlretrieve(linkurl, keyword+str(time())+".jpg")
            print "[+] Downloaded "+str(linkurl)
def link_extract(keyword):
    from selenium import webdriver
    import os
    from time import sleep
    from bs4 import BeautifulSoup
    driver = webdriver.PhantomJS()
    driver.get("https://www.flickr.com/search/?q="+str(keyword))
    print "[+] Page Loading"
    sleep(5)
    print "[+] Page Receieved"
    pagesource = driver.page_source
    print "[+] Page Source Obtained"
    soup = BeautifulSoup(pagesource, 'html.parser')
    print "[+] Delicious Soup is Here"
    soup = soup.findAll("main",{"id":"search-unified-content"})
    print "[+] Page search-unified-content"
    soup = soup[0].findAll("div",{"class":"photo-list-photo-interaction"})
    print "[+] Page photo-list-photo-interaction"
    os.mkdir(keyword)
    os.chdir(keyword)
    for item in soup:
        link = item.findAll("a")[0]["href"]
        fp = open(keyword+"-flickr-links.txt","a")
        fp.write(str(link)+"\n")
        fp.close()
        print "[+] Processed "+str(link)
    print "[-] I QUIT !!!"
    link_download(keyword)
link_extract(raw_input("[!!] Enter Search Keyword : "))
