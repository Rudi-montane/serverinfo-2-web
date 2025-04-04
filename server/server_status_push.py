import psutil, requests, json, socket, time

url = "https://deinewebsite.tld/serverstatus/receive.php"

while True:
    data = {
        "hostname": socket.gethostname(),
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "uptime": int(time.time() - psutil.boot_time())
    }

    try:
        requests.post(url, json=data, timeout=5)
    except Exception as e:
        print("Fehler beim Senden:", e)

    time.sleep(5)
