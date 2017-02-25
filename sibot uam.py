import urllib, urllib2, cookielib, re
#from pyquery import PyQuery
from bs4 import BeautifulSoup
"""
codigo encontrado:
http://stackoverflow.com/questions/189555/how-to-use-python-to-login-to-a-webpage-and-retrieve-cookies-for-later-usage
"""
def idsFromPage(html):
    re_id = r'<tr><td><div align="center"><font color="#[0-9]+">[0-9]+</font>'
    m = re.findall(re_id, html)
    ids = [re.search(">([0-9]+)<",x).groups()[0] for x in m]
    return ids

def vacFromPage(html):
    soup = BeautifulSoup(html,"html.parser")
    tr = soup.findAll("tr")
    vac = {}
    for row in tr:
        cols = row.findAll('td')
        if(len(cols)>1):
            key =  cols[0].text.replace(':','').strip(' \t\n\r')
            value = row.findAll('td')[1].text.strip(' \t\n\r')
            vac[key] = value
    return vac
def vacFromIds(ids):
    pages={}
    vac_param = {'txtClave':'Oswaldo948',
             'txtUsuario':'2123065423',
             'txtPos':'0',
             'bolTipoQ':'0',
             'txtBuscaEmp':'',
             'btnEnviar':'Ver'}
    for id in ids:
        vac_param['txtVacID'] = id
        resp3 = opener.open("https://www.bolsadetrabajo.uam.mx/srcMueResEmp.php",urllib.urlencode(vac_param));
        pages[id] = resp3.read();
    return pages
login_param = {'txtUsuario':'2123065423',
         'txtContrasena':'Oswaldo948',
         'btnAccesar':'Ingresar'}
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode(login_param)
resp1 = opener.open('https://www.bolsadetrabajo.uam.mx/sesion.php', login_data)
page_param = {'txtClave':'Oswaldo948',
             'txtUsuario':'2123065423',
             'x':'79',
             'y':'24'}
page_data = urllib.urlencode(page_param)
resp2 = opener.open('https://www.bolsadetrabajo.uam.mx/srcBuscaEmp.php',page_data)

html_text = resp2.read()
ids = idsFromPage(html_text)

pages = vacFromIds(ids)

html_text3 = pages[ids[0]].replace("\r","")
print  vacFromPage(html_text3)





