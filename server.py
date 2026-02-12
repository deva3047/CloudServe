import os, time, sys, re, string, random, datetime, shutil, subprocess, webbrowser, socket, urllib.request, threading
from tkinter import Tk, filedialog

BOLD = "\033[1m"
RED = "\033[1;91m"
GREEN = "\033[1;92m"
GREY = "\033[1;96m"
YELLOW = "\033[1;93m"
BLUE = "\033[1;94m"
WHITE = "\033[1;37m"  
ORANGE = "\033[1;33m"  
PUR = "\033[1;98m"
P = "\033[1;95m"
RESET = "\033[0m"

def slow(text, color=RESET, delay=0.03):
    try:
        sys.stdout.write(color)
        sys.stdout.flush()
        for sh in text:
            sys.stdout.write(sh)
            sys.stdout.flush()
            time.sleep(delay)
    finally:
        sys.stdout.write(RESET + '\n')
        sys.stdout.flush()
def baner():
    slow(f'''
			███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ 
			██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
			███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
			╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
			███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
			╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    
			       Ver 1.0 - by {GREY}[ Jay Joshi {RESET}
		 {GREEN}https://github.com/deva3047{RESET}
		 {GREEN}https://www.instagram.com/deva_3047_?igsh=czkxemIxc2QxcTF1{RESET}
		     {WHITE} Easy To Create Server{RESET}
         {BLUE} ==========================================================================={RESET}
    ''',BLUE,delay=0.002) 
def get_local_ip():
    """Get the local network IP address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def get_public_ip():
    """Get the public IP address."""
    try:
        with urllib.request.urlopen('https://api.ipify.org', timeout=5) as response:
            return response.read().decode('utf-8').strip()
    except Exception:
        return None

def menu():
    pass  

def install_apache2():
    os.system('clear')
    slow('Apache2 installing.........', GREEN)
    try:
        subprocess.run(['sudo', 'apt', 'update'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['sudo', 'apt', 'install', '-y', 'apache2'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['sudo', 'chown', '-R', 'www-data:www-data', '/var/www/html'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['sudo', 'chmod', '-R', '775', '/var/www/html'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.system('clear')
        slow('Apache2 installed successfully ...... \n\nPress Enter to return to main menu...', GREEN)
    except subprocess.CalledProcessError as e:
        slow(f'Error during installation: {e}', RED)
    input(GREEN + "" + RESET)

def start_php_server():
    os.system('clear')
    try:
        subprocess.run(['sudo', 'service', 'apache2', 'start'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        slow('Server started successfully.', GREEN)
    except subprocess.CalledProcessError as e:
        slow(f'Error starting server: {e}', RED)
    input(GREEN + "\nPress Enter to return to main menu..." + RESET)

def stop_php_server():
    os.system('clear')
    try:
        subprocess.run(['sudo', 'service', 'apache2', 'stop'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        slow('Server stopped successfully.', GREEN)
    except subprocess.CalledProcessError as e:
        slow(f'Error stopping server: {e}', RED)
    input(GREEN + "\nPress Enter to return to main menu..." + RESET)

def check_php_status():
    os.system('clear')
    try:
        result = subprocess.run(['sudo', 'service', 'apache2', 'status'], capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        slow(f'Error checking status: {e}', RED)
    input(GREEN + "\nPress Enter to return to main menu..." + RESET)

def upload_php_file():
    os.system('clear')
    slow('Opening file selection dialog...', YELLOW)
    
    root = Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(
        title="Select a file to upload (e.g., .txt, .php)",
        filetypes=[("All files", "*.*")]
    )
    
    if file_path:
        filename = os.path.basename(file_path)
        destination = f'/var/www/html/{filename}'
        try:
            result = subprocess.run(['sudo', 'cp', file_path, destination], capture_output=True, text=True)
            if result.returncode == 0:
               
                subprocess.run(['sudo', 'chmod', '775', destination], check=True)
                subprocess.run(['sudo', 'chown', 'www-data:www-data', destination], check=True)
                slow(f'Successfully uploaded {filename} to /var/www/html.', GREEN)
                slow(f'Access it at: http://localhost/{filename}', BLUE)

                subprocess.run(['sudo', 'service', 'apache2', 'restart'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                slow(f'Error uploading file: {result.stderr.strip()}', RED)
        except Exception as e:
            slow(f'Error uploading file: {str(e)}', RED)
    else:
        slow('No file selected.', YELLOW)
    
    input(GREEN + "\nPress Enter to return to main menu..." + RESET)

def delete_upload_file():
    os.system('clear')
    slow('Opening file selection dialog to delete a file from /var/www/html...', YELLOW)
    
    root = Tk()
    root.withdraw()
    
    slow('Files in /var/www/html:', YELLOW)
    try:
        result = subprocess.run(['ls', '/var/www/html'], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            slow('Error listing files.', RED)
            input(GREEN + "\nPress Enter to return to main menu..." + RESET)
            return
    except Exception as e:
        slow(f'Error listing files: {str(e)}', RED)
        input(GREEN + "\nPress Enter to return to main menu..." + RESET)
        return
    
    filename = input(YELLOW + 'Enter the filename to delete (without path): ' + RESET).strip()
    if filename:
        file_path = f'/var/www/html/{filename}'
        try:
            result = subprocess.run(['sudo', 'rm', file_path], capture_output=True, text=True)
            if result.returncode == 0:
                slow(f'Successfully deleted {filename} from /var/www/html.', GREEN)
            else:
                slow(f'Error deleting file: {result.stderr.strip()}', RED)
        except Exception as e:
            slow(f'Error deleting file: {str(e)}', RED)
    else:
        slow('No filename entered.', YELLOW)
    
    input(GREEN + "\nPress Enter to return to main menu..." + RESET)

def open_server_page():
    os.system('clear')
    slow('Opening server page in default browser...', YELLOW)
    try:
        webbrowser.open('http://localhost')
        slow('Server page opened.', GREEN)
    except Exception as e:
        slow(f'Error opening browser: {str(e)}', RED)
    
    input(GREEN + "\nPress Enter to return to main menu..." + RESET)

def share_server_link():
    os.system('clear')
    local_ip = get_local_ip()
    public_ip = get_public_ip()
    slow(f'Local IP: {local_ip} (access via http://{local_ip})', BLUE)
    if public_ip:
        slow(f'Public IP: {public_ip} (access via http://{public_ip})', BLUE)
    else:
        slow('Unable to fetch public IP.', RED)
    input(GREEN + "\nPress Enter to return to main menu..." + RESET)

def create_cloudflared_link():
    os.system('clear')

    slow('Install PHP ...................', GREEN, delay=0.003)
    os.system(
    'nohup sudo dpkg -i cloudflared-linux-amd64.deb '
    '&& sudo apt --fix-broken install -y '
    '> /dev/null 2>&1 </dev/null &')

    slow('Link Is Creating........................', GREEN)

    os.system('cloudflared --protocol http2 --url http://127.0.0.1:80')

    input(GREEN + "\nPress Enter to return to main menu..." + RESET)
def main():
    while True:
        os.system('clear')
        baner()
        menu()
        slow('\n\n\t\t' + RED + '[' + WHITE + '01' + RED + ']' + ORANGE + ' Install Apache2      ' + RED + '[' + WHITE + '04' + RED + ']' + ORANGE + ' Check Status          ' + RED + '[' + WHITE + '07' + RED + ']' + ORANGE + ' Open Server Page', delay=0.003)
        slow('\n\n\t\t' + RED + '[' + WHITE + '02' + RED + ']' + ORANGE + ' Start Server         ' + RED + '[' + WHITE + '05' + RED + ']' + ORANGE + ' Upload File           ' + RED + '[' + WHITE + '08' + RED + ']' + ORANGE + ' Send Server Link', delay=0.003)
        slow('\n\n\t\t' + RED + '[' + WHITE + '03' + RED + ']' + ORANGE + ' Stop Server          ' + RED + '[' + WHITE + '06' + RED + ']' + ORANGE + ' Delete Upload File    ' + RED + '[' + WHITE + '09' + RED + ']' + ORANGE + ' Generate Seacure Link ', delay=0.003)
        slow('\n\n\t\t' + RED + '[' + WHITE + '99' + RED + ']' + ORANGE + ' Exit', delay=0.003)


        try:
            choice = int(input(PUR + '\n\nChoose Your Choice: ' + RESET))
        except ValueError:
            slow("Invalid choice. Please enter a number.", RED)
            input(GREEN + "\nPress Enter to return to main menu..." + RESET)
            continue

        if choice == 1:
            install_apache2()
        elif choice == 2:
            start_php_server()
        elif choice == 3:
            stop_php_server()
        elif choice == 4:
            check_php_status()
        elif choice == 5:
            upload_php_file()
        elif choice == 6:
            delete_upload_file()
        elif choice == 7:
            open_server_page()
        elif choice == 8:
            share_server_link()
        elif choice == 9:
            create_cloudflared_link()
        elif choice == 99:
            slow("Exiting........", GREEN)
            sys.exit(0)
        else:
            slow("Invalid choice.", RED)

if __name__ == "__main__":
    main()
