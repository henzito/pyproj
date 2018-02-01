
# coding: utf-8

# In[ ]:


import selenium.webdriver as webdriver
import spotilib
import time
from textblob import TextBlob as tb

browser = webdriver.Firefox()
def search_web(tracknamequery,artist):
    url = searchURL+tracknamequery
    browser.get(url)
    link = browser.find_element_by_partial_link_text(artist)
    link.click()
    del url
def get_songname(artist,song):
    a = tb(artist)
    b = tb(song)
    c = a.words
    d = b.words
    e = c + d 
    e.append("genius lyrics")
    tracknamequery = str(e) # adds desired site to query
    search_web(tracknamequery,artist)
    del a,b,c,d,e,artist,song,tracknamequery
    
searchURL="http://www.google.com/?#q=";

#user guide
print('O programa coleta a musica que voce esta ouvindo no spotify e')
print('abre a respectiva pagina da letra no Genius.com através do Firefox.')
print('Pause a música para desligar o programa. Ele fechará todas abas.')
print('~~~Bem vindos ao SpotiGenius fetcher~~~')
print()
info = spotilib.song_info()
if info == "Spotify":
    print('Nada tocando... vou dar play')
    spotilib.play()
    time.sleep(3)
art = spotilib.artist() #returns the artist of the current playing song
son = spotilib.song() #returns the song title of the current playing song
get_songname(art,son)
g = spotilib.song_info()
while g != "Spotify":
    art1 = spotilib.artist()
    son1 = spotilib.song()
    if son1==son:
        time.sleep(1)
    else:
        print('Tocando agora:',son1,'-',art1)
        del art,son
        art = art1
        son = son1
        get_songname(art,son)
    del g
    g = spotilib.song_info()
print('Não tem nada tocando. Vou dormir...')
browser.quit()

        


# In[13]:


print(urls)


# In[92]:


g = spotilib.song_info()
print(g)

