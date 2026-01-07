import subprocess
import time
from datetime import datetime
from email.message import EmailMessage
import smtplib

EMAIL = "chandana.r@sigmoidanalytics.com"  
REPORT = "/home/sigmoid/report.html"

html = """
<html>
<body>
<h3>CPU & Memory Alert Report</h3>
<table border="1" cellpadding="5">
<tr>
<th>Time</th><th>Command</th><th>Metric</th><th>Usage</th><th>Status</th>
</tr>
"""

for _ in range(60):
    timestamp = datetime.now().strftime("%H:%M:%S")

    result = subprocess.check_output(
        ["ps", "-eo", "comm,%cpu,%mem", "--no-headers"],
        text=True
    )

    for line in result.splitlines():
        cmd, cpu, mem = line.split(None, 2)
        cpu = float(cpu)
        mem = float(mem)

        if cpu > 10:
            html += f"<tr style='background-color:red;color:white'>\
            <td>{timestamp}</td><td>{cmd}</td><td>CPU</td><td>{cpu}%</td><td>CRITICAL</td></tr>"
        elif cpu > 5:
            html += f"<tr style='background-color:yellow'>\
            <td>{timestamp}</td><td>{cmd}</td><td>CPU</td><td>{cpu}%</td><td>WARNING</td></tr>"

        if mem > 10:
            html += f"<tr style='background-color:red;color:white'>\
            <td>{timestamp}</td><td>{cmd}</td><td>MEM</td><td>{mem}%</td><td>CRITICAL</td></tr>"
        elif mem > 5:
            html += f"<tr style='background-color:yellow'>\
            <td>{timestamp}</td><td>{cmd}</td><td>MEM</td><td>{mem}%</td><td>WARNING</td></tr>"

    time.sleep(10)

html += "</table></body></html>"

with open(REPORT, "w") as f:
    f.write(html)

msg = EmailMessage()
msg["Subject"] = "CPU & Memory Alert Report"
msg["From"] = EMAIL
msg["To"] = EMAIL
msg.set_content("HTML report attached")
msg.add_alternative(html, subtype="html")

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(EMAIL, "zwqj pkaz vbxh ckev")   
    server.send_message(msg)

print("Mail sent successfully")

