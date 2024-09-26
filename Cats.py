import os
import time
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def art():
    print("\033[1;91m" + r""" ______  _               _    
 | ___ \| |             | |   
 | |_/ /| |  __ _   ___ | | __
 | ___ \| | / _` | / __|| |/ /
 | |_/ /| || (_| || (__ |   < 
 \____/ |_| \__,_| \___||_|\_\
""" + "\033[0m" + "\033[1;92m" + r""" ______                                   
 |  _  \                                  
 | | | | _ __   __ _   __ _   ___   _ __  
 | | | || '__| / _` | / _` | / _ \ | '_ \ 
 | |/ / | |   | (_| || (_| || (_) || | | |
 |___/  |_|    \__,_| \__, | \___/ |_| |_|
                       __/ |              
                      |___/               
""" + "\033[0m" + "\033[1;93m" + r"""  _   _               _                
 | | | |             | |               
 | |_| |  __ _   ___ | | __  ___  _ __ 
 |  _  | / _` | / __|| |/ / / _ \| '__|
 | | | || (_| || (__ |   < |  __/| |   
 \_| |_/ \__,_| \___||_|\_\ \___||_| 
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mScript created by: Black Dragon Hacker\033[0m\n\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m\n\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m--------------[Cats Bot]---------------\033[0m\n\033[1;96m---------------------------------------\033[0m")

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')

import requests

def fetch_user_data(token, account_number):
    url_1 = "https://cats-backend-cxblew-prod.up.railway.app/user/create?referral_code=6qZk2HSNQ9MkvIYAMF1zI"
    headers = {
        "Accept": "*/*",
        "Authorization": f"tma {token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Origin": "https://cats-frontend.tgapps.store",
        "Referer": "https://cats-frontend.tgapps.store/",
        "Sec-CH-UA": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "Sec-CH-UA-Mobile": "?1",
        "Sec-CH-UA-Platform": '"Android"',
    }
    
    body = {}

    try:
        response_1 = requests.post(url_1, headers=headers, json=body)
        response_1.raise_for_status()
        data_1 = response_1.json()
        massage = data_1.get("name")
        
        if response_1.status_code == 200:
            url_2 = "https://cats-backend-cxblew-prod.up.railway.app/user"
            response_2 = requests.get(url_2, headers=headers)
            response_2.raise_for_status()
            data_2 = response_2.json()
            refer_reward = data_2.get("referrerReward", "N/A")
            name = data_2.get("firstName", "N/A")
            balance = data_2.get("totalRewards", "N/A")
            
            print(f"{Fore.CYAN + Style.BRIGHT}------Account No.{account_number}------")
            print(f"{Fore.MAGENTA + Style.BRIGHT}Name: {name}")
            print(f"{Fore.GREEN + Style.BRIGHT}Balance: {Fore.WHITE + Style.BRIGHT}{balance} | {Fore.CYAN + Style.BRIGHT}Referral Bonus: {Fore.WHITE + Style.BRIGHT}{refer_reward}")
        
        elif massage == "Error":
            url_2 = "https://cats-backend-cxblew-prod.up.railway.app/user"
            response_2 = requests.get(url_2, headers=headers)
            response_2.raise_for_status()
            data_2 = response_2.json()
            refer_reward = data_2.get("referrerReward", "N/A")
            name = data_2.get("firstName", "N/A")
            balance = data_2.get("totalRewards", "N/A")
            
            print(f"{Fore.CYAN + Style.BRIGHT}------Account No.{account_number}------")
            print(f"{Fore.MAGENTA + Style.BRIGHT}Name: {name}")
            print(f"{Fore.GREEN + Style.BRIGHT}Balance: {Fore.WHITE + Style.BRIGHT}{balance} | {Fore.CYAN + Style.BRIGHT}Referral Bonus: {Fore.WHITE + Style.BRIGHT}{refer_reward}")
               
    except requests.RequestException as e:
        url_2 = "https://cats-backend-cxblew-prod.up.railway.app/user"
        response_2 = requests.get(url_2, headers=headers)
        response_2.raise_for_status()
        data_2 = response_2.json()
        refer_reward = data_2.get("referrerReward", "N/A")
        name = data_2.get("firstName", "N/A")
        balance = data_2.get("totalRewards", "N/A")
            
        print(f"{Fore.CYAN + Style.BRIGHT}------Account No.{account_number}------")
        print(f"{Fore.MAGENTA + Style.BRIGHT}Name: {name}")
        print(f"{Fore.GREEN + Style.BRIGHT}Balance: {Fore.WHITE + Style.BRIGHT}{balance} | {Fore.CYAN + Style.BRIGHT}Referral Bonus: {Fore.WHITE + Style.BRIGHT}{refer_reward}")
    except ValueError:
        print(f"Error parsing JSON response for Account No.{account_number}")

def task_list(token):
    url = "https://cats-backend-cxblew-prod.up.railway.app/tasks/user?group=cats"
    headers = {
        "Accept": "*/*",
        "Authorization": f"tma {token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Origin": "https://cats-frontend.tgapps.store",
        "Referer": "https://cats-frontend.tgapps.store/",
        "Sec-CH-UA": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "Sec-CH-UA-Mobile": "?1",
        "Sec-CH-UA-Platform": '"Android"',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        task_ids = [task['id'] for task in data.get('tasks', [])]
        total_tasks = len(task_ids)
        return task_ids, total_tasks
    except requests.RequestException as e:
        print(f"Error fetching tasks: {e}")
        return [], 0
    except ValueError:
        print("Error parsing JSON response for tasks")
        return [], 0

def task_complete(token, task_ids):
    total_tasks = len(task_ids)
    print(f"{Fore.CYAN + Style.BRIGHT}Total Tasks: {total_tasks}")

    for task_id in task_ids:
        url_1 = f"https://cats-backend-cxblew-prod.up.railway.app/tasks/{task_id}/complete"
        url_2 = f"https://cats-backend-cxblew-prod.up.railway.app/tasks/{task_id}/check"
        headers = {
            "Accept": "*/*",
            "Authorization": f"tma {token}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36",
            "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
            "Origin": "https://cats-frontend.tgapps.store",
            "Referer": "https://cats-frontend.tgapps.store/",
            "Sec-CH-UA": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "Sec-CH-UA-Mobile": "?1",
            "Sec-CH-UA-Platform": '"Android"',
        }
        
        body = {}

        try:
            response = requests.post(url_1, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()
            success = data.get("success")
            if success:
                print(f"{Fore.GREEN + Style.BRIGHT}Task No.{task_id} Claimed Successfully")
            else:
                print(f"{Fore.YELLOW + Style.BRIGHT}Task No.{task_id} Already Claimed")
        except requests.RequestException as e:
            try:
                response_check = requests.get(url_2, headers=headers)
                response_check.raise_for_status()
                print(f"Response from {url_2}: {response_check.json()}")
            except requests.RequestException as e_check:
                print(f"{Fore.RED + Style.BRIGHT}Task No.{task_id} Telegram Task Complete Manually")
            except ValueError:
                print(f"Error parsing JSON response for task check {task_id}")
        except ValueError:
            print(f"Error parsing JSON response for task {task_id}")

def process_all_accounts():
    try:
        with open("data.txt", "r") as file:
            tokens = [line.strip() for line in file.readlines()]

        for i, token in enumerate(tokens, start=1):
            fetch_user_data(token, i)
            task_ids, total_tasks = task_list(token)
            if task_ids:
                task_complete(token, task_ids)
    except FileNotFoundError:
        print("Error: data.txt file not found.")

def main():
    clear_terminal()
    art()
    while True:
        process_all_accounts()
        countdown_timer(3 * 60 * 60)  # 3 hours
        clear_terminal()
        art()

if __name__ == "__main__":
    main()
