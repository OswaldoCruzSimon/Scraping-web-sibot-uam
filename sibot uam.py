import urllib, urllib2, cookielib, re
#from pyquery import PyQuery
from bs4 import BeautifulSoup
import json
import time
import datetime
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
    html = html.replace("\r","")
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
def getNoOfertasVisisbles():
    next_param = {'bolTipoQ':'0',
              'txtClave':'Oswaldo948',
              'txtUsuario':'2123065423',
              'txtBuscaEmp':'',
              'txtPos':'5000',
              'btnRegresar':'Siguientes+10+>'}
   
    resp = opener.open('https://www.bolsadetrabajo.uam.mx/srcBuscaEmp.php',urllib.urlencode(next_param))
    soup = BeautifulSoup(resp.read(),"html.parser")
    return int(soup.findAll('strong')[1].text)

def getVacPag(ini,fin):
    next_param = {'bolTipoQ':'0',
                  'txtClave':'Oswaldo948',
                  'txtUsuario':'2123065423',
                  'txtBuscaEmp':'',
                  'btnRegresar':'Siguientes+10+>'}
    vacantes = {}

    for pos in range(ini,fin,10):
        next_param['txtPos']=str(pos)
        resp4 = opener.open('https://www.bolsadetrabajo.uam.mx/srcBuscaEmp.php',urllib.urlencode(next_param))
        html_text4 = resp4.read();
        ids = idsFromPage(html_text4)
        pages = vacFromIds(ids)
        for id,page in pages.items():
            vacantes[id] =  vacFromPage(page)
        time.sleep(3)
        print pos+10

    return vacantes

def saveDict(filename,dicc):
    #print len(dicc)
    with open(filename, 'w') as f:
        json.dump(dicc, f, indent=4)
    return

def loadDict(filename):
    try:
        with open(filename) as f:
            dicc = json.load(f)
    except:
        dicc={}
    return dicc

def updateVac(filename,newDicc):
    dicc = loadDict(filename)
    dicc.update(newDicc)
    saveDict(filename,dicc)

def getVacPagPersistent(filename,ini,fin):
    next_param = {'bolTipoQ':'0',
                  'txtClave':'Oswaldo948',
                  'txtUsuario':'2123065423',
                  'txtBuscaEmp':'',
                  'btnRegresar':'Siguientes+10+>'}
    vacantes = {}

    for pos in range(ini,fin,10):
        next_param['txtPos']=str(pos)
        resp4 = opener.open('https://www.bolsadetrabajo.uam.mx/srcBuscaEmp.php',urllib.urlencode(next_param))
        html_text4 = resp4.read();
        ids = idsFromPage(html_text4)
        pages = vacFromIds(ids)
        for id,page in pages.items():
            vacantes[id] =  vacFromPage(page)
        updateVac(filename,vacantes)
        vacantes = {}
        time.sleep(3)
        print pos+10

login_param = {'txtUsuario':'2123065423',
         'txtContrasena':'Oswaldo948',
         'btnAccesar':'Ingresar'}
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
resp1 = opener.open('https://www.bolsadetrabajo.uam.mx/sesion.php', urllib.urlencode(login_param))


#page_param = {'txtClave':'Oswaldo948',
#             'txtUsuario':'2123065423',
#             'x':'79',
#             'y':'24'}
#resp2 = opener.open('https://www.bolsadetrabajo.uam.mx/srcBuscaEmp.php',urllib.urlencode(page_param))
#html_text = resp2.read()
#ids = idsFromPage(html_text)
#pages = vacFromIds(ids)

#vacMax = getNoOfertasVisisbles()

fecha = datetime.datetime.now()
filename = "%s-%s-%s %s-%s-%s.json" % (fecha.day, fecha.month, fecha.year, fecha.hour, fecha.month, fecha.second)

vac = getVacPagPersistent(filename,450,550)


