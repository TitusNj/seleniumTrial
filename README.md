ON LINUX


STEP 1 — Install Google Chrome
You downloaded and installed the .deb file directly because apt mirrors were failing.
Commands:
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb

Result:
✔ Chrome is installed
 ✔ Verified by:
google-chrome --version


STEP 2 — Download the correct ChromeDriver
ChromeDriver must match your Chrome version.
You checked your Chrome version: 
google-chrome --version
Google Chrome 144.0.7559.96

So you downloaded the matching driver:
wget https://storage.googleapis.com/chrome-for-testing-public/144.0.7559.96/linux64/chromedriver-linux64.zip


STEP 3 — Extract the ChromeDriver
You didn’t have unzip, so we used Python to extract it.
This failed
muthari@DESKTOP-T6Q43RR:~/selenium/cookieBot/SeleniumTutorial$ unzip chromedriver-linux64.zip
Command 'unzip' not found, but can be installed with:
sudo apt install unzip

So we tried
python3 - <<'PY'
import zipfile
zipfile.ZipFile("chromedriver-linux64.zip").extractall("chromedriver-linux64")
print("unzipped")
PY


STEP 4 — Locate the driver
The file was inside a nested folder:
chromedriver-linux64/chromedriver-linux64/chromedriver


STEP 5 — Make it executable
This makes the driver runnable:
chmod +x chromedriver-linux64/chromedriver-linux64/chromedriver


STEP 6 — Move it to a system PATH
You moved it to /usr/local/bin so the system can access it anywhere.
sudo mv chromedriver-linux64/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver


STEP 7 — Confirm installation
Check the driver version:
chromedriver --version

If it prints a version number, you’re set.

STEP 8 — Write Selenium code using the driver
Use the exact path:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")
time.sleep(10)

BTW

✅ What are APT mirrors?
When you run:
sudo apt install chromium-chromedriver

Ubuntu downloads the software from a server.
That server is called a mirror.
Think of it like:
🌍 A mirror = a copy of Ubuntu’s software store
There are many mirrors around the world.

🔍 Why mirrors exist
Ubuntu keeps many copies of its software in different locations so:
✅ Downloads are faster

Your WSL could not reach that server because of network problems.



driver.quit()
