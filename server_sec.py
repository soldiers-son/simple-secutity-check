import os, subprocess
from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def run_command(command):
    try:
        # Added check_=True to catch execution errors better
        result = subprocess.run(command, shell=True, capture_output=True, text=True, input = "sudo")
        return result.stdout.strip()
    except Exception as e:
        return f"Error executing command: {e}"

def firewall_check():
    print("--- Firewall Status ---")
    status = run_command("sudo ufw status verbose")
    print(status)
    if "inactive" in status.lower():
        print("Firewall inactive. Run 'sudo ufw enable' to activate.")

def check_updates():
    print("\n--- System Updates ---")
    print("Checking for updates...")
    run_command("sudo apt update && sudo apt-get update")
    print("Applying upgrades (this may take a moment)...")
    run_command("sudo apt full-upgrade -y")
    print("Updates complete.")

def port_scan():
    print("\n--- LocalHost Port Scan ---")
    print("Scanning all ports...")
    run_command("sudo nmap -p- localhost")
    result = run_command("sudo nmap -p- localhost")
    print(f"{result}")
    print("Scan Complete")

def network_scan():
    print("\n--- Network Port Scan ---")
    print("Scanning all network ports (this may take a moment)...")
    # Relpace with your ip
    run_command("sudo nmap YOURIP")
    result = run_command("sudo nmap YOURIP")
    print(f"{result}")
    print("Scan Complete")

def virus_scan():
    def confirm():
            confirm = input ("Would you like to run virus scan? y/n: ")
            return confirm == 'y'
    print("\n--- Virus Scan ---")
    if confirm():
        print("Updating known threat list...")
        run_command("sudo freshclam")
        print("List updated...")
        target = input("Enter PATH you wish to scan: ")
        print("Scanning all files(this may take a moment)...")
        run_command(f"sudo clamscan -r {target} --log=/home/euclid/Desktop/Opsec/scan_dump/{current_time}.txt")
        print("Scan Complete")
        print("Scan Saved To /Opsec/scan_dump ")
    else:
        print("Virus scan cancled...")

def run_program():
    check_updates()
    firewall_check()
    port_scan()
    virus_scan()



if __name__ == "__main__":
    # Check for root privileges first
    if os.geteuid() != 0:
        print("Please run this script with sudo.")
    else:
        def confirm():
            confirm = input ("Would you like to run network scan? y/n: ")
            return confirm == 'y'
        if confirm():
            print("Starting System Security Scan...")
            run_program()
            print(f"\n--- System Security Scan Complete @{current_time} ---")
        else:
            print("\n--- Scan Cancled ---")
