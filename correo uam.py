import urllib, urllib2, cookielib, re
"""
codigo encontrado:
http://stackoverflow.com/questions/189555/how-to-use-python-to-login-to-a-webpage-and-retrieve-cookies-for-later-usage
"""

param = {'.cgifields':'httpcompress',
 'cgifields':'autologin',
 'loginname':'2123065423',
 'password':'Oswaldo948',
 'logindomain':'alumnos.cua.uam.mx',
 'loginbutton':'Acceder'}
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode(param)
resp1 = opener.open('https://alumnos.cua.uam.mx/cgi-bin/openwebmail/openwebmail.pl?logindomain=alumnos.cua.uam.mx', login_data)
exp2 = '/cgi-bin/.*afterlogin'
html_text = resp1.read()
m = re.search(exp2, html_text)
url = html_text[m.start():m.end()]
resp2 = opener.open('https://alumnos.cua.uam.mx'+url)
print resp2.read()
