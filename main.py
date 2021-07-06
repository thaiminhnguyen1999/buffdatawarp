import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
script_version = '1.2'
window_title   = f"Buff dung lượng Cloudflare WARP+ by Nguyễn Ngọc Thiện - Phiên bản script: {script_version}"
os.system('title ' + window_title if os.name == 'nt' else 'PS1="\[\e]0;' + window_title + '\a\]"; echo $PS1')
os.system('cls' if os.name == 'nt' else 'clear')
print ("----------------------------------------------------------------")
print ("|    BUFF DUNG LƯỢNG CLOUDFLARE WARP+ BY NGUYỄN NGỌC THIỆN     |")
print ("----------------------------------------------------------------")
print (f"| [-]Phiên bản script: {script_version}				       |")
print ("----------------------------------------------------------------")
print ("| [-] Mọi lỗi về script xin được báo lỗi qua GitHub 	       |") 
print ("| [-] GitHub: github.com/kakangocthien109 		       |")
print ("----------------------------------------------------------------")
referrer  = input("Nhập WARP+ ID của bạn vào đây:")
def progressBar():
	animation     = ["[□□□□□□□□□□]","[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]"]
	progress_anim = 0
	save_anim     = animation[progress_anim % len(animation)]
	percent       = 0
	while True:
		for i in range(10):
			percent += 1
			sys.stdout.write(f"\r[+] Chờ phản hồi từ máy chủ...  " + save_anim + f" {percent}%")
			sys.stdout.flush()
			time.sleep(0.075)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 100:
			sys.stdout.write("\r[+] Lệnh đã được hoàn thành! ")
			break

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print("")
		print(error)	

g = 0
b = 0
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("")
	print("                  Buff dung lượng Cloudflare WARP+" + " by Nguyễn Ngọc Thiện")
	print("")
	sys.stdout.write("\r[+] Đang thực thi lệnh...   [□□□□□□□□□□] 0%")
	sys.stdout.flush()
	result = run()
	if result == 200:
		g += 1
		progressBar()
		print(f"\n[*] WARP+ ID của bạn: {referrer}")    
		print(f"[+] Đã thêm {g} GB vào tài khoản WARP+ của bạn.")
		print(f"[#] Tổng cộng: {g} lần thành công; {b} lần thất bại")
		for i in range(15,0,-1):
			sys.stdout.write(f"\r[*] Sau {i} giây, lệnh mới sẽ được thực thi.")
			sys.stdout.flush()
			time.sleep(1)
	else:
		b += 1
		print("[-] Không thể kết nối đến server, có thể do server đang quá tải.")
		print(f"[#] Tổng cộng: {g} lần thành công; {b} lần thất bại")
		for i in range(10,0,-1):
			sys.stdout.write(f"\r[*] Thực thi lại lệnh sau {i} giây...")
			sys.stdout.flush()
			time.sleep(1)
