import urllib.request
import urllib.error
from urllib.parse import urljoin

base_url = "http://127.0.0.1:8081/"

paths = [
    "admin",
    "api",
    "robots.txt",
    "login.php",
    "index.php",
    "setup.php",
    "security.php",
    "instructions.php",
    "about.php",
    "phpinfo.php",
    "server-status",
    "uploads/",
    "config/",
    "backup/",
]

print("Local DVWA directory discovery")
print(f"Target: {base_url}")
print("-" * 55)

for path in paths:
    url = urljoin(base_url, path)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Local-DVWA-Discovery/1.0"}
    )

    try:
        with urllib.request.urlopen(request, timeout=3) as response:
            print(f"{response.status:3}  {path}")

    except urllib.error.HTTPError as error:
        print(f"{error.code:3}  {path}")

    except Exception as error:
        print(f"ERR  {path} ({error})")
