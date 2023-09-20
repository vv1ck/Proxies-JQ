try:
	from requests import get
	from random import choice
	from time import sleep
	from threading import Thread,Lock
	import requests,sys,os;Lists='V4^c_Yf4TEw'
	from user_agent import generate_user_agent;Lis='V4^c_Yf4TEw'
except Exception as Joker:exit(Joker)
def vv1ck(*a, **b):
	with Lock():
		print(*a, **b)
def MOVES(M):
	for c in M + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		sleep(1. / 10)
class Check_Proxy:
	def __init__(self,modes):
		self.listProxys,self.theards=[],[]
		self.START=True;self.modes=modes
		self.BAD,self.successful,self.cont=0,0,0
		self.TRT=150
		self.URLS='https://vv1ck.github.io/home'
		self.FEILS()
	
	def CLOESD_CHECK(self):
		self.START=False
		vv1ck('\n The examination is over ..\n')
		sleep(10)
		sys.exit()
	
	def CheckProxys(self):
		while self.START:
			if ( self.cont == len(self.listProxys)):
				self.CLOESD_CHECK()
			else:
				try:
					IPS=self.listProxys[self.cont]
					CK=get(self.URLS,headers={"Connection" : "keep-alive","Accept-Encoding" : "gzip, deflate, br","Accept-Language" : "en","User-Agent" : generate_user_agent(),"Accept" : "*/*"},proxies= {"http": f"http://{IPS}","https": f"http://{IPS}"},timeout=10)
					if CK.status_code==429:
						self.BAD+=1
					else:
						self.successful+=1
						with open('PROXYS_Checked.txt', 'a') as J:J.write(f'{IPS}\n')
				except IndexError:
					self.CLOESD_CHECK()
				except KeyboardInterrupt:
					self.CLOESD_CHECK()
				except requests.exceptions.ConnectionError:
					self.BAD+=1
				except requests.exceptions.ReadTimeout:
					self.BAD+=1
				except requests.exceptions.ChunkedEncodingError: self.BAD+=1
				vv1ck(f'\r₿:~ Good proxy: {self.successful} | Bad Proxy: {self.BAD}\r',end="")
				self.cont+=1				
	
	def Threads(self):
		self.URLS=input('₿:~ Enter the website link: ')
		if ('http'in self.URLS):pass
		elif ('https'in self.URLS):pass
		else:
			vv1ck('\n[!] Please enter a valid link\n');return self.Threads()
		vv1ck('\n')
		for i in range(self.TRT):
			trts=Thread(target=self.CheckProxys)
			trts.start()
			self.theards.append(trts)
		for trts2 in self.theards:
			trts2.join()
		input('Done')
	def FEILS(self):
		if (self.modes=='QTR'):
			try:
				for PRX in open('NewProxy.txt','r').read().splitlines():
					self.listProxys.append(PRX)
			except FileNotFoundError:
				try:
					for PRX in open(input('₿:~ Enter Proxy File: '),'r').read().splitlines():
						self.listProxys.append(PRX)
				except FileNotFoundError:
					vv1ck('[!] Invalid file name, try again');return self.FEILS()
		else:
			try:
				for PRX in open(input('₿:~ Enter Proxy File: '),'r').read().splitlines():
					self.listProxys.append(PRX)
			except FileNotFoundError:
				vv1ck('[!] Invalid file name, try again');return self.FEILS()
		if (len(self.listProxys)>=500):self.TRT= 250
		else:self.TRT=150
		self.Threads()
def PROXYSFILAS():
	if Lis in Lists:pass
	else:exit('Okay..')
	JOlist=[]
	for JJNN1 in Lists:
		posi=ord(JJNN1)
		NW=chr(posi-20)
		JOlist.append(NW)
	DN=''.join(JOlist)
	return DN
class PROXYS_API:
	def __init__(self):
		self.listProxys=[]
		self.theards=[]
		try:os.remove('NewProxy.txt')
		except FileNotFoundError:pass
		self.ProxyScrapeAPI()
	def SAVE_FAILS(self):
		vv1ck('\r[+] Proxies are saved >#1\r',end='')
		con=1
		for ip in self.listProxys:
			with open('NewProxy.txt', 'a') as J:J.write(f'{ip}\n')
			print(f'\r[+] Proxies are saved >#{str(con)}\r',end='')
			con+=1
		vv1ck(f'\n[+] proxies : {len(self.listProxys)}\n[+] File Name : NewProxy.txt\n[+] The proxies have been saved successfully ..\n[!] Want to check proxies? : ');J=input('\t-1) Yes, check proxies please\n\t2-) Exit ..')
		if (J=='1'):Check_Proxy('QTR')
		else:sys.exit()
	def OpenProxyAPI(self):
		try:
			prx3 = get('https://openproxy.space/list/http').text
			try:
				for PRXS0 in prx3.split('code:"CN"')[1].split('items:[')[1].split('],active')[0].split(','):
					vv1ck('\r[+] Extracting in progress >>>>>>>\r',end='')
					s = PRXS0.split('"')[1].split('"')[0]
					if str(s) in self.listProxys:pass
					else:self.listProxys.append(s)
					try:self.listProxys.remove('')
					except ValueError:pass
			except IndexError:pass
			try:
				for PRXS1 in prx3.split('code:"US"')[1].split('items:[')[1].split('],active')[0].split(','):
					vv1ck('\r[+] Extracting in progress >>>>>>>>\r',end='')
					j = PRXS1.split('"')[1].split('"')[0]
					if str(j) in self.listProxys:pass
					else:self.listProxys.append(j)
					try:self.listProxys.remove('')
					except ValueError:pass
			except IndexError:pass
			try:
				for PRXS2 in prx3.split('code:"ID"')[1].split('items:[')[1].split('],active')[0].split(','):
					vv1ck('\r[+] Extracting in progress >>>>>>>>>\r',end='')
					n = PRXS2.split('"')[1].split('"')[0]
					if str(n) in self.listProxys:pass
					else:self.listProxys.append(n)
					try:self.listProxys.remove('')
					except ValueError:pass
			except IndexError:pass
			try:
				for PRXS3 in prx3.split('code:"CA"')[1].split('items:[')[1].split('],active')[0].split(','):
					vv1ck('\r[+] Extracting in progress >>>>>>>>>>\r',end='')
					p = PRXS3.split('"')[1].split('"')[0]
					if str(p) in self.listProxys:pass
					else:self.listProxys.append(p)
					try:self.listProxys.remove('')
					except ValueError:pass
			except IndexError:pass
			try:
				for PRXS4 in prx3.split('code:"RU"')[1].split('items:[')[1].split('],active')[0].split(','):
					vv1ck('\r[+] Extracting in progress >>>>>>>>>>>\r',end='')
					v = PRXS4.split('"')[1].split('"')[0]
					if str(v) in self.listProxys:pass
					else:self.listProxys.append(v)
					try:self.listProxys.remove('')
					except ValueError:pass
			except IndexError:pass
		except requests.exceptions.ConnectTimeout:pass
		except :pass
		vv1ck('\n');self.SAVE_FAILS()
	
	def GeonodeProxyAPI(self):
		try:
			prx6 = get('https://proxylist.geonode.com/api/proxy-list?limit=350&page=1&sort_by=lastChecked&sort_type=desc',headers={"Origin" : "https://geonode.com","Host" : "proxylist.geonode.com","User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Connection" : "keep-alive","Referer" : "https://geonode.com/free-proxy-list","Accept-Language" : "ar","Accept" : "application/json, text/plain, */*"})
			cont=1
			if ('ip' in prx6.text):
				for _ in range(300):
					print('\r[+] Extracting in progress >>>>>>\r',end='')
					ip = prx6.json()['data'][cont]['ip']+':'+prx6.json()['data'][cont]['port']
					if str(ip) in self.listProxys:pass
					else:self.listProxys.append(ip)
					try:self.listProxys.remove('')
					except ValueError:pass
					cont+=1
					vv1ck('\r[+] Extracting in progress >>>>*\r',end='')
					vv1ck('\r[+] Extracting in progress >>>>>>\r',end='')
		except requests.exceptions.ConnectTimeout:pass
		except :pass
		self.OpenProxyAPI()
	def GithubProxyAPI(self):
		try:
			for prx5 in get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt').text.split('\n'):
				vv1ck('\r[+] Extracting in progress >>>>\r',end='')
				if str(prx5) in self.listProxys:pass
				else:self.listProxys.append(prx5)
				try:self.listProxys.remove('')
				except ValueError:pass
		except requests.exceptions.ConnectTimeout:pass
		except :pass
		try:
			for prx2 in get('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt').text.split("\n"):
				vv1ck('\r[+] Extracting in progress >>>>>\r',end='')
				if str(prx2) in self.listProxys:pass
				else:self.listProxys.append(prx2)
				try:self.listProxys.remove('')
				except ValueError:pass
		except requests.exceptions.ConnectTimeout:pass
		except :pass
		self.GeonodeProxyAPI()
		
	def ProxyScrapeAPI(self):
		try:
			for prx in get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={choice(['5','2','3','4','6'])}0000&country=all&ssl=all&anonymity=all&simplified=true").text.split("\r\n"):
				vv1ck('\r[+] Extracting in progress >>\r',end='')
				self.listProxys.append(prx)
				try:self.listProxys.remove('')
				except ValueError:pass
		except requests.exceptions.ConnectTimeout:pass
		except :pass
		try:
			for PRXS in get('https://free-proxy-list.net/').text.split('onclick="select(this)">Free proxies from free-proxy-list.net')[1].split('UTC.')[1].split('</textarea>')[0].split('\n'):
				vv1ck('\r[+] Extracting in progress >>>\r',end='')
				if str(PRXS) in self.listProxys:pass
				else:self.listProxys.append(PRXS)
				try:self.listProxys.remove('')
				except ValueError:pass
		except requests.exceptions.ConnectTimeout:pass
		except :pass
		self.GithubProxyAPI()

if __name__ == '__main__':
	print("""
  ____                _ """+PROXYSFILAS()+""" _  ___  
 |  _ \ _ __ _____  _(_) ___  ___      | |/ _ \ 
 | |_) | '__/ _ \ \/ / |/ _ \/ __|  _  | | | | |
 |  __/| | | (_) >  <| |  __/\__ \ | |_| | |_| |
 |_|   |_|  \___/_/\_\_|\___||___/  \___/ \__\_\
      
       GitHub : https://github.com/vv1ck
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
	MOVES("""
	-1) proxies checker
	-2) proxies extractor 
	-99) Exit ...""")
	MODES=input('[+] Enter : ')
	if(MODES=='1'):Check_Proxy('Joker')
	elif(MODES=='2'):PROXYS_API()
	else:pass
