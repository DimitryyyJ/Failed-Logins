# Failed Login Detector

This project analyzes log files and detects failed login attempts from IP addresses.

It helps identify suspicious activity and potential brute-force attacks.  
The tool is designed as a simple command-line utility and simulates basic SOC analyst tasks.

## Features

- Reads log files
- Detects failed login attempts
- Counts failed logins per IP address
- Identifies suspicious IP addresses based on a threshold
- Finds the most frequent attacker
- Handles invalid input and file errors

## Technologies Used

- Python
- Regular Expressions (re)
- Dictionaries
- File handling
- Command-line interface (CLI)

## Example Output

192.168.1.5 7 failed logins  
10.0.0.8 2 failed logins  

Suspicious IP 192.168.1.5  

Most frequent attacker 192.168.1.5 7 failed logins

## How to Run

Clone the repository:

git clone https://github.com/YOUR_USERNAME/Failed-Login-Detector.git

Run the script:

python main.py

Enter the path to your log file when prompted.

## Why I Built This Project

I am learning cybersecurity and working toward becoming a SOC Analyst.

This project simulates real-world log analysis tasks such as:

- detecting brute-force login attempts
- identifying suspicious IP activity
- analyzing security logs
