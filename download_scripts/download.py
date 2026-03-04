import requests
import random
import time


def get_url_for_script_id(script_id):
    return f"https://www.rocky-beach.com/hoerspiel/skript/skript_{script_id:03d}.pdf"


for i in range(1, 226):
    url = get_url_for_script_id(i)
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"scripts/skript_{i:03d}.pdf", "wb") as f:
            f.write(response.content)
        print(f"Downloaded script {i}")
    else:
        print(f"Failed to download script {i}")
    time.sleep(random.uniform(0.5, 1.5))
