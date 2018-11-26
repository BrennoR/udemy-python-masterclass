import webbrowser

# webbrowser.open("https://www.python.org/", new=1)
#
# help(webbrowser)

# for i in range(10):
#     print(1, 2, 3, 4, sep='', end='\t')

# chrome = webbrowser.get('/usr/bin/google-chrome %s').open("https://www.python.org/")    DOESN'T WORK ;(

safari = webbrowser.get(using='safari')
safari.open_new("https://www.python.org/")