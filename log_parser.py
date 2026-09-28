# Simple Security Log Parser Example
import re

def parse_log_file(file_path):
    print(f"[*] Analyzing log file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Look for failed login attempts or warnings
                if "Failed" in line or "Error" in line:
                    print(f"[!] Alert Found: {line.strip()}")
    except FileNotFoundError:
        print("[!] Error: Log file not found. Please check the path.")

if __name__ == "__main__":
    # Test with a sample file name
    parse_log_file("system_security.log")
