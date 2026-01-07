# CPU & Memory Monitoring with Email Alerts (Python)


This project is a simple Python script that monitors the CPU and memory usage of all running processes on a Linux system. It checks usage every 10 seconds for 10 minutes, highlights processes that exceed certain thresholds with colors, and sends a single email report to you with all the details.

---

## Tools Used

* Python 3
* Linux `ps` command
* SMTP (Gmail)
* HTML formatting for emails

---

## What the Script Does

1. Runs the Linux `ps` command to get:

   * Process name
   * CPU usage (%)
   * Memory usage (%)
2. Adds a timestamp for each record
3. Checks for high usage:

   * Yellow (Warning) → usage > 5%
   * Red (Critical) → usage > 10%
4. Builds an HTML table with colored rows
5. Runs for 10 minutes automatically
6. Sends one consolidated email with all the alerts
7. Saves the report as an HTML file so you can open it and check it manually

---

## Color Rules

| Usage | Status   | Color  |
| ----- | -------- | ------ |
| > 5%  | Warning  | Yellow |
| > 10% | Critical | Red    |

> Note: Colors are applied using HTML, so plain text emails won't show them.

---

## Files in this Project

```
monitor.py       # Main Python script that does the monitoring
report.html      # Generated HTML report (optional for checking)
README.md        # This documentation
```

---

## How to Use

### 1. Prerequisites

* Python 3 installed
* Personal Gmail account
* Gmail App Password (you need to have 2-Step Verification enabled)

### 2. Update Email Info

Edit the script and replace your email and app password:

```python
EMAIL = "your_email@gmail.com"
# Replace APP_PASSWORD with your Gmail App Password
```

### 3. Run the Script

```bash
python3 monitor.py
```

It will:

* Run for about 10 minutes
* Create an HTML report
* Send you a colored email with all the alerts

---

## Checking the Output

You can open the report manually in a browser to see the colored table:

```bash
firefox /home/sigmoid/report.html
```

Or just check your email inbox for the alert email.

---

## What You’ll Learn

By doing this project, you’ll learn:

* How to run Linux commands from Python
* How to monitor system resources
* How to check thresholds and generate alerts
* How to build HTML emails
* How to send emails using Python’s SMTP

---

