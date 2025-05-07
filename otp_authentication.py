import imaplib
import email
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Gmail credentials
EMAIL = "lipika.psingh@gmail.com"
APP_PASSWORD = "Eatoncenter@2025"

# Connect to Gmail and read OTP
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, APP_PASSWORD)
mail.select("inbox")

# Search for the latest OTP email
status, messages = mail.search(None, '(FROM "customercare@icicibank.com")')
latest_email_id = messages[0].split()[-1]

# Fetch email content
status, msg_data = mail.fetch(latest_email_id, '(RFC822)')
msg = email.message_from_bytes(msg_data[0][1])

# Extract email body
body = ""
if msg.is_multipart():
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True).decode()
else:
    body = msg.get_payload(decode=True).decode()

# Extract OTP using regex (assuming it's a 6-digit code)
otp = re.search(r"\b\d{6}\b", body).group()
print("Extracted OTP:", otp)

# === Selenium Part ===
driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Simulate login steps...
# After triggering OTP screen:
time.sleep(2)  # Wait for OTP field to appear

otp_input = driver.find_element(By.ID, "otp_input")
otp_input.send_keys(otp)

submit_btn = driver.find_element(By.ID, "submit_btn")
submit_btn.click()
