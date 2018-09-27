page="......website contents....."
start_link = (page.find('<a href='))
start_quote=page.find('"',start_link)
end_quote=page.find('"',start_quote+1)
url=(page[start_quote+1:end_quote])
print(url)
