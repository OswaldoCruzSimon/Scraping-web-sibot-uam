import urllib, urllib2, cookielib, re
"""
codigo encontrado:
http://stackoverflow.com/questions/189555/how-to-use-python-to-login-to-a-webpage-and-retrieve-cookies-for-later-usage
"""

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
print resp2.read()
