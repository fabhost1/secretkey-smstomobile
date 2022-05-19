
import random
import random

import tkinter as tk
from tkinter import *
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
from tracemalloc import stop
import pywhatkit
 
 


root=Tk()
root.geometry('700x500')
img = PhotoImage(file="1.png")
label = Label(
      root,
      image=img)
label.place(x=0,y=0,width=700,height=500)
t=Label(root,text='SECRET KEY GENERATOR',fg='white',bg='black',font=('times',12))
t.place(x=220,y=0)
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
   'abcdefghijklmnopqrstuvwxyz' + \
   '0123456789' + \
   ':.;,?!@#$%&()+=-*/_<> []{}`~^"\'\\'

def generate_key():
    """Generate an key for our cipher"""
    shuffled = sorted(chars, key=lambda k: random.random())
    return dict(zip(chars, shuffled))

def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    return ''.join(key[l] for l in plaintext)

def decrypt(key, ciphertext):

    """Decrypt the string and return the plaintext"""
    flipped = {v: k for k, v in key.items()}
    return ''.join(flipped[l] for l in ciphertext)

MG=Label(root,text='MESSAGE',font=('times'))
MG.place(x=100,y=160)
en=Entry(root)
en.place(x=100,y=200)
NA=Label(root,text='NAME',font=('times'))
NA.place(x=400,y=160)
name=Entry(root)
name.place(x=400,y=200)
def send_mail():
    import smtplib
    from email.message import EmailMessage

    msg = EmailMessage()
    msg['From'] = 'pythonfabhost2021@gmail.com'
    msg['To'] = 'pythonfabhost2021@gmail.com'
    msg['Subject'] = nam
    msg.set_content(enc)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('pythonfabhost2021@gmail.com','skive@123')

        smtp.send_message(msg)
        smtp.quit()

def show_result():
    global key,encrypted,secret1,enc,nam,root1,final1,encryp,dip
    root1=Tk()
    root1.geometry('700x500')
    plaintext=en.get()
    filt=len(plaintext)
    if filt==0:
        from tkinter import messagebox
        messagebox.showwarning("showinfo", "please enter message")
    else:
        n = random.randint(0,3)
        dict={0:'hdfjf0',1:'vcjdwgj',2:'jhcvjh',3:'gvjdfj',4:'gfddfu',5:'hdhfhj'}
        dip=dict.get(n)
        #print(dip)
        key = generate_key()
        keycon=str(key)
        with open('keys.txt', 'w') as f:
            f.write(keycon)
        with open('readme.txt', 'w') as f:
            f.write(dip)
        encrypted = encrypt(key, plaintext)
        enc='%s' % encrypted
        nam="message from"+" "+name.get()
        MG=Label(root1,text='SECRET KEY',font=('times'))
        MG.place(x=100,y=160)
        secret1=Entry(root1)
        secret1.place(x=100,y=200)
        NA=Label(root1,text='ENCRYPTED MESSAGE',font=('times'))
        NA.place(x=400,y=160)
        encryp=Entry(root1)
        encryp.place(x=400,y=200)
        b1=Button(root1,command=decry,text='DECRYPT',font=('times'))
        b1.place(x=250,y=300)
        root1.mainloop
        #print(dip)
        #print(enc)
        send_mail()
        divi()
def divi():
    import requests

    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"FRLiPdUNbjtIylOSgw1C3JHhDAGa4me6Vfo0TXz9uW21503QZKscv79UCGdFZt54yswlxuSLI2Ab6jNXp1H715","sender_id":"FSTSMS","message":dip,"variables_values":"12345|asdaswdx","route":"p","numbers":"6383540837"}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
    # print the send message
    #print(returned_msg['message'])

def decry():
    final1=encryp.get()
    with open('readme.txt') as f:
        lines = f.readlines()
        sec=secret1.get()
    if lines[0]==sec:
        decrypted = decrypt(key,final1)
        #print(type(encrypted),encrypted,"this is main")
        #print('Decrypted: %s' % decrypted)
        out=('Decrypted: %s' % decrypted)
        z=Label(root1,text='TEXT DECRPTED SUCESS',font=('times'))
        z.place(x=210,y=50)
        z=Label(root1,text=out,font=('times'))
        z.place(x=210,y=100)
    else:
        z=Label(root1,text='WRONG KEY',width=30)
        z.place(x=200,y=50)
        z=Label(root1,text="",width=40,font=('times'))
        z.place(x=210,y=100)
        print('wrong key')    
  


    
    



b1=Button(root,command=show_result,text='SEND')
b1.place(x=320,y=300)
root.mainloop()
