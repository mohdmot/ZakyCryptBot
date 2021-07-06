from random import choice
import requests,sys,time,pyperclip,threading
from tkinter import *
from tkinter import ttk
from tkinter import filedialog,messagebox


def Hex(Tybe,string):
    if Tybe == 'decode':
        HexDecodeHeader={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '24',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_lfa=LF1.1.168521d0946d393c.1622380139777; _hjid=2cd3a1f8-d168-4ded-9600-0edf56e77b32; __gads=ID=04a3600e98a2b4c5-22c362c058c800be:T=1622380140:RT=1622380140:S=ALNI_MZMNxBxY4httSYrCIkc6t_sELX__A; PHPSESSID=fcaffop44l03gaessc5debcgn2; _gid=GA1.2.1038518682.1625340202; _ga_JY9C3TP5R4=GS1.1.1625340160.2.1.1625340661.0; _ga=GA1.2.1046006246.1622380140',
            'Host': 'online-toolz.com',
            'Origin': 'https://online-toolz.com',
            'Referer': 'https://online-toolz.com/tools/text-hex-convertor.php',
            'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'}
        HexDecodeData={'input': string}
        HexDecodeReq=requests.post('https://online-toolz.com/functions/HEX-TEXT.php',headers=HexDecodeHeader,data=HexDecodeData).text
        return HexDecodeReq
    if Tybe == 'encode':
        HexEncodeHeader={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '15',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_lfa=LF1.1.168521d0946d393c.1622380139777; _hjid=2cd3a1f8-d168-4ded-9600-0edf56e77b32; __gads=ID=04a3600e98a2b4c5-22c362c058c800be:T=1622380140:RT=1622380140:S=ALNI_MZMNxBxY4httSYrCIkc6t_sELX__A; PHPSESSID=fcaffop44l03gaessc5debcgn2; _gid=GA1.2.1038518682.1625340202; _ga_JY9C3TP5R4=GS1.1.1625340160.2.1.1625340661.0; _ga=GA1.2.1046006246.1622380140',
            'Host': 'online-toolz.com',
            'Origin': 'https://online-toolz.com',
            'Referer': 'https://online-toolz.com/tools/text-hex-convertor.php',
            'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'}
        HexEncodeData={'input': string}
        HexEncodeReq=requests.post('https://online-toolz.com/functions/TEXT-HEX.php',headers=HexEncodeHeader,data=HexEncodeData).text
        return HexEncodeReq
    else:return 'error'

def Text(Tybe,string):
    if Tybe=='encode':
        TextEncodeHeaders={'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '11',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_lfa=LF1.1.168521d0946d393c.1622380139777; _hjid=2cd3a1f8-d168-4ded-9600-0edf56e77b32; __gads=ID=04a3600e98a2b4c5-22c362c058c800be:T=1622380140:RT=1622380140:S=ALNI_MZMNxBxY4httSYrCIkc6t_sELX__A; _gid=GA1.2.1038518682.1625340202; PHPSESSID=1fpcn4ihr8s8jg9n8459ki7ind; _ga_JY9C3TP5R4=GS1.1.1625399741.4.1.1625399748.0; _ga=GA1.2.1046006246.1622380140'
            ,'Host': 'www.online-toolz.com',
            'Origin': 'https://www.online-toolz.com',
            'Referer': 'https://www.online-toolz.com/tools/text-encryption-decryption.php',
            'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'}
        TextEncodeData={'input': string}
        TextEncodeReq=requests.post('https://www.online-toolz.com/functions/ENCRYPT.php',headers=TextEncodeHeaders,data=TextEncodeData).text
        return TextEncodeReq
    if Tybe=='decode':
        TextDecodeHeaders={'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '11',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_lfa=LF1.1.168521d0946d393c.1622380139777; _hjid=2cd3a1f8-d168-4ded-9600-0edf56e77b32; __gads=ID=04a3600e98a2b4c5-22c362c058c800be:T=1622380140:RT=1622380140:S=ALNI_MZMNxBxY4httSYrCIkc6t_sELX__A; _gid=GA1.2.1038518682.1625340202; PHPSESSID=1fpcn4ihr8s8jg9n8459ki7ind; _ga_JY9C3TP5R4=GS1.1.1625399741.4.1.1625399748.0; _ga=GA1.2.1046006246.1622380140'
            ,'Host': 'www.online-toolz.com',
            'Origin': 'https://www.online-toolz.com',
            'Referer': 'https://www.online-toolz.com/tools/text-encryption-decryption.php',
            'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'}
        TextDecodeData={'input': string}
        TextDecodeReq=requests.post('https://www.online-toolz.com/functions/DECRYPT.php',headers=TextDecodeHeaders,data=TextDecodeData).text
        return TextDecodeReq
    else:return 'error'

def Base64(Tybe,string):
    Base64Headers={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '11',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_lfa=LF1.1.168521d0946d393c.1622380139777; _hjid=2cd3a1f8-d168-4ded-9600-0edf56e77b32; __gads=ID=04a3600e98a2b4c5-22c362c058c800be:T=1622380140:RT=1622380140:S=ALNI_MZMNxBxY4httSYrCIkc6t_sELX__A; _gid=GA1.2.1038518682.1625340202; PHPSESSID=1fpcn4ihr8s8jg9n8459ki7ind; _ga=GA1.2.1046006246.1622380140; _ga_JY9C3TP5R4=GS1.1.1625399741.4.1.1625400528.0'
        ,'Host': 'www.online-toolz.com',
        'Origin': 'https://www.online-toolz.com',
        'Referer': 'https://www.online-toolz.com/tools/base64-decode-encode-online.php',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'}
    Base64Data={'input':string}
    if Tybe == 'encode':
        Base64EncodeReq=requests.post('https://www.online-toolz.com/functions/BASE64-ENCODE.php',headers=Base64Headers,data=Base64Data).text
        return Base64EncodeReq
    if Tybe == 'decode':
        Base64DecodeReq=requests.post('https://www.online-toolz.com/functions/BASE64-DECODE.php',headers=Base64Headers,data=Base64Data).text
        return Base64DecodeReq
    else:return 'error'

def Binary(Tybe,string):
    BinaryHeaders={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '11',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_lfa=LF1.1.168521d0946d393c.1622380139777; _hjid=2cd3a1f8-d168-4ded-9600-0edf56e77b32; __gads=ID=04a3600e98a2b4c5-22c362c058c800be:T=1622380140:RT=1622380140:S=ALNI_MZMNxBxY4httSYrCIkc6t_sELX__A; _gid=GA1.2.1038518682.1625340202; PHPSESSID=4ehohb3vote43bor178ld5fgs8; _ga=GA1.2.1046006246.1622380140; _ga_JY9C3TP5R4=GS1.1.1625415126.5.1.1625415225.0'
        ,'Host': 'www.online-toolz.com',
        'Origin': 'https://www.online-toolz.com',
        'Referer': 'https://www.online-toolz.com/tools/text-binary-convertor.php',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'}
    BinaryData={'input':string}
    if Tybe =='encode':
        BinaryEncodeReq=requests.post('https://www.online-toolz.com/functions/TEXT-BINARY.php',headers=BinaryHeaders,data=BinaryData).text
        return BinaryEncodeReq
    if Tybe =='decode':
        BinaryDecodeReq=requests.post('https://www.online-toolz.com/functions/BINARY-TEXT.php',headers=BinaryHeaders,data=BinaryData).text
        return BinaryDecodeReq
    else:return 'error'


# print (Key.Create('text%hex%base64%base64%hex'))
# print (Key.Read('Zaky%Crypt%Bot:89551253923862398126945760674938760983643091092981231'))
class Key () :
    # KeyV1  :  text%hex%base64%base64%hex
    # KeyV2  :  Zaky%Crypt%Bot:8955125392386239812091092981231
    def Create (KeyV1) :
        EncodedKey=Base64('encode',KeyV1)
        EncodedKey=Hex('encode',EncodedKey)
        EncodedKey='Zaky%Crypt%Bot:'+EncodedKey
        return EncodedKey
    def Read (keyV2) :
        keyV2=keyV2.replace('Zaky%Crypt%Bot:','')
        EncodedKey=Hex('decode',keyV2)
        EncodedKey=Base64('decode',EncodedKey)
        return EncodedKey


# print('File Tybe : ' + ReadFileTybe('C://File/File.txt'))
# Output : File Tybe : txt
def ReadFileTybe (Path) :
    ReadFileTybe_Data={}
    Path=Path.replace('/','@#\n').replace(' \ '.strip(),'@#\n').splitlines()
    for Items in Path :
        if Items.endswith('@#') :
            continue
        else:
            ReadFileTybe_Data['File']=Items
    File_Tybe1=f'{ReadFileTybe_Data["File"]}'.replace('.','\npath=').splitlines()
    for File_Tybe in File_Tybe1:
        if File_Tybe.startswith('path='):
            Ensd=File_Tybe.replace('path=','')
            return Ensd
            break
        else:continue


# if CheckInternet() :
#     print('[ + ] Internet Connected !!')
def CheckInternet () :
    try:
        requests.get('https://www.google.com').text
        return True
    except:return False


# EncryptFile('C://File/File.txt')['src']
# EncryptFile('C://File/File.txt')['key']
def EncryptFile (FilePath,progress,win) :
    FileSrc=open(FilePath,'rb').read()
    NewSrc=''
    KeyV1Created=''
    DownloadNum=0
    for crypt in range(5):
        DownloadNum+=20
        progress['value']=DownloadNum
        win.update_idletasks()
        CryptTybe=choice(['hex','text','base64'])
        if CryptTybe == 'hex':
            FileSrc=Hex('encode',FileSrc)
            KeyV1Created='hex'+'%'+KeyV1Created
        if CryptTybe == 'text':
            FileSrc=Text('encode',FileSrc)
            KeyV1Created='text'+'%'+KeyV1Created
        if CryptTybe == 'base64':
            FileSrc=Base64('encode',FileSrc)
            KeyV1Created='base64'+'%'+KeyV1Created
    OutData={'src':FileSrc,'key':KeyV1Created}
    return OutData


# DecryptFile('C://File/File','Key')
def DecryptFile (FilePath,Key1,progress,win) :
    FileSrc=open(FilePath,'rb').read()
    Key1=Key1.replace('%','\n').splitlines()
    DownloadNum=0
    for CryptTybe in Key1 :
        DownloadNum+=20
        progress['value']=DownloadNum
        win.update_idletasks()
        if CryptTybe == 'hex':
            FileSrc=Hex('decode',FileSrc)
        if CryptTybe == 'text':
            FileSrc=Text('decode',FileSrc)
        if CryptTybe == 'base64':
            FileSrc=Base64('decode',FileSrc)
    OutData={'src':FileSrc}
    return FileSrc


def OutKeyWindow (KeyHere) :
    KeyWindow=Tk()
    KeyWindow.title('Zaky Crypt Bot (Your Decrypt Key)')
    KeyWindow.geometry('350x70')
    KeyWindow.iconbitmap('icon.ico')
    #####################################
    def CopyButton () :
        pyperclip.copy(KeyHere)
    KeyOutEntry=ttk.Entry(KeyWindow,width=40)
    KeyOutEntry.place(x=10,y=25)
    ttk.Button(KeyWindow,text='Copy',command=CopyButton).place(x=260,y=25)
    KeyOutEntry.insert(0,KeyHere)
    #####################################
    KeyWindow.mainloop()




class App () :
    def __init__ (self) :
        win=Tk()
        win.title('Zaky Crypt Bot')
        win.geometry('300x250')
        win.iconbitmap('icon.ico')
        ################################################
        progress = ttk.Progressbar(orient = HORIZONTAL,length = 280, mode = 'determinate')
        progress.place(x=10,y=180)
        #################################
        def StartApp () :
            # TybeVar = Encrypt
            # TybeVar1 = Decrypt
            OpenBtn.config(state=DISABLED)
            StartBtn.config(state=DISABLED)
            if int(TybeVar.get()) == 1 : # Encrypt
                def Encode222 () :
                    EncryptDef=EncryptFile(str(PathVar.get()),progress,win)
                    SaveAsDirectory = filedialog.asksaveasfilename()
                    HHH=EncryptDef['key']
                    EncodeKey=Key.Create(HHH)
                    def HHH1 () :
                        OutKeyWindow(EncodeKey)
                    threading.Thread(target=HHH1).start()
                    open(SaveAsDirectory,'w',encoding="utf-8").write(EncryptDef['src'])
                    OpenBtn.config(state=NORMAL)
                    StartBtn.config(state=NORMAL)
                    return
                threading.Thread(target=Encode222).start()
                return
            if int(TybeVar1.get()) == 1 : # Decrypt
                def decode11 () :
                    Pathy=str(PathVar.get())
                    #####################################################
                    AskKeyWindow=Tk()
                    AskKeyWindow.title('Zaky Crypt Bot (Enter Your Decrypt Key)')
                    AskKeyWindow.geometry('350x70')
                    AskKeyWindow.iconbitmap('icon.ico')
                    MMM=StringVar(AskKeyWindow)
                    ###################
                    def Done ():
                        AskKeyWindow.destroy()
                    AskKeyVar=ttk.Entry(AskKeyWindow,width=40,textvariable=MMM)
                    AskKeyVar.place(x=10,y=25)
                    ttk.Button(AskKeyWindow,text='Decrypt',command=Done).place(x=260,y=25)
                    ###################
                    AskKeyWindow.mainloop()
                    print(str(MMM.get()))
                    #####################################################
                    AskForKeyWin=Key.Read(str(MMM.get()))
                    DecodeEnd=DecryptFile(Pathy,AskForKeyWin,progress,win)
                    print(DecodeEnd)
                    SaveAsDirectory = filedialog.asksaveasfilename()
                    open(SaveAsDirectory,'w',encoding="utf-8").write(str(DecodeEnd))
                    OpenBtn.config(state=NORMAL)
                    StartBtn.config(state=NORMAL)
                threading.Thread(target=decode11).start()
                return
            else:messagebox.showerror('Error !!','Please Choice (Encrypt or Decrypt)')
        ################################################
        ################################################
        StartBtn=ttk.Button(text='Start',width=30,command=StartApp)
        StartBtn.place(x=50,y=210)
        ################################################
        PathVar=StringVar()
        PathEntry=ttk.Entry(width=33,textvariable=PathVar).place(x=10,y=100)
        ########################
        def OpenFile () :
            GetPath=filedialog.askopenfilename(defaultextension = "*.*",filetypes = [("All Files", "*.*")])
            PathVar.set(str(GetPath))
        OpenBtn=ttk.Button(text='Open',width=8,command=OpenFile)
        OpenBtn.place(x=220,y=100)
        ################################################
        def V1 () :
            TybeVar.set(0)
        def V2 () :
            TybeVar1.set(0)
        TybeVar=IntVar()
        TybeVar1=IntVar()
        ttk.Checkbutton(text='Encrypt',variable=TybeVar,command=V2).place(x=180,y=20)
        ttk.Checkbutton(text='Decrypt',variable=TybeVar1,command=V1).place(x=30,y=20)
        ################################################
        win.mainloop()

if __name__ == '__main__':
    while True:
        if CheckInternet() :
            App()
            break
        else:
            Error=Tk()
            Error.title('Zaky Crypt Bot (Internet Error)')
            Error.geometry('350x100')
            Error.iconbitmap('icon.ico')
            Label(Error,text='No Internet Connection !!!',font=('calibri',15)).place(x=60,y=15)#font
            def again () :
                Error.destroy()
            ttk.Button(Error,text='Try Again',width=15,command=again).place(x=35,y=60)
            ttk.Button(Error,text='Exit',width=15,command=lambda:sys.exit()).place(x=220,y=60)
            Error.mainloop()