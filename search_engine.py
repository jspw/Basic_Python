def first_link(page):
    start_link= page.find('<a href = ')
    if(start_link == -1):
        return None,0
    start_quote = page.find('"',start_link)
    end_quote=page.find('"',start_quote+1)
    url=page[start_quote+1:end_quote]
    return url,end_quote

def print_all_link(page):
    while True :
        url ,end_quote = first_link(page)
        if url :
            print(url)
            page=page[end_quote:]
        else :
            break

page=('......<a href = "www.facebook.com"> FACEBOOK </a>...........<a href = "www.youtube.com">YOUTUBE ......<a href = "www.codeforces.com"> Code.....')
print_all_link(page)
