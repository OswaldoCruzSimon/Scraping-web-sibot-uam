import re
resp = """
<html>
<head>
<title>OpenWebMail - Copyright</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body bgcolor="#ffffff" background="/openwebmail/images/backgrounds/Globe.gif">
<style type="text/css"><!--
body {
background-image: url(/openwebmail/images/backgrounds/Globe.gif);
background-repeat: repeat;
font-family: Arial,Helvetica,sans-serif; font-size: 10pt; font-color: #cccccc
}
A:link    { color: #cccccc; text-decoration: none }
A:visited { color: #cccccc; text-decoration: none }
A:hover   { color: #333333; text-decoration: none }
--></style>
<center><br><br><br>
<a href="/cgi-bin/openwebmail/openwebmail-main.pl?sessionid=2123065423*alumnos.cua.uam.mx-session-0.615765145587833&action=listmessages_afterlogin" title="click to next page" style="text-decoration: none"><font color="#333333"> &nbsp; Cargando, por favor espere ...</font></a>
<br><br><br>

<a href="http://openwebmail.org/" title="click to home of OpenWebMail" target="_blank" style="text-decoration: none">
OpenWebMail 2.53. 20080123<br><br>
Copyright (C) 2001-2008<br>
Thomas Chung, Alex Teslik, Scott Mazur, Joao S Veiga, Marian &#270;urkovi&#269;<br><br>
Copyright (C) 2000<br>
Ernie Miller  (original GPL project: Neomail)<br><br>
Special Thanks to Retired Developers<br>
Chung-Kie Tung, Nai-Jung Kuo, Chao-Chiu Wang, Emir Litric,<br>Dattola Filippo, Bernd Bass<br><br>
</a>

"""
exp = '<a href=".*" title'
exp2 = '/cgi-bin/.*afterlogin'
m = re.search(exp2, resp)

print resp[m.start():m.end()]
