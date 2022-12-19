page = 'HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA Alba es muy guapa y me la voy a follar. <a href="https://www.facebook.com/TheXKCD/">FB</a>' #Suponemos que podemos acceder al contenido de una página
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url = page[start_quote + 1 : end_quote]
print(url)