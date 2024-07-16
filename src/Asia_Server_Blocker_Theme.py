import tkinter as tk
from tkinter import font, messagebox, ttk
import subprocess
import re
import sys
import os

server_ips = {
    "Seoul": "146.66.152.1",
    "Tokyo": "45.121.184.1",
    "HongKong": "103.28.54.1",
    "India": "116.202.224.1",
    "Singapore": "103.28.54.1"
}

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def ping_server(ip):
    try:
        startupinfo = None
        if sys.platform == "win32":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        output = subprocess.check_output(["ping", "-n", "1", "-w", "1000", ip], 
                                         universal_newlines=True, 
                                         startupinfo=startupinfo,
                                         creationflags=subprocess.CREATE_NO_WINDOW)
        match = re.search(r"시간=(\d+)ms", output)
        if match:
            return int(match.group(1))
        else:
            return "Timeout"
    except subprocess.CalledProcessError:
        return "Timeout"

def run_ping_test():
    for server, ip in server_ips.items():
        ping_time = ping_server(ip)
        if isinstance(ping_time, int):
            status_labels[server].config(text=f"{ping_time}ms ●", fg='red')
        else:
            status_labels[server].config(text="Timeout ●", fg='red')

def check_sdr_rule_exists():
    command = "netsh advfirewall firewall show rule name=blockSDR"
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True, creationflags=subprocess.CREATE_NO_WINDOW)
        return "No rules match the specified criteria." not in output
    except subprocess.CalledProcessError:
        return False

def add_sdr_rule():
    if not check_sdr_rule_exists():
        command = "netsh advfirewall firewall add rule name=blockSDR dir=out action=block profile=any protocol=any remoteip=143.137.146.0-143.137.146.255"
        try:
            subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            print("SDR rule added successfully.")
        except subprocess.CalledProcessError:
            print("Failed to add SDR rule.")

def toggle_server_block(server):
    try:
        if server == "Seoul":
            if checkKorea.get() == 1:
                command = "netsh advfirewall firewall add rule name=blockSeoul dir=out action=block profile=any protocol=any remoteip=146.66.152.0-146.66.152.255"
                subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                messagebox.showinfo("Success", "Seoul server blocked successfully!")
                status_labels["Seoul"].config(text="● ", fg='#39FF14')
            else:
                command = "netsh advfirewall firewall delete rule name=blockSeoul"
                subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                messagebox.showinfo("Success", "Seoul server block removed!")
                status_labels["Seoul"].config(text="● ", fg='red')
        elif server == "Tokyo":
            if checkJapan.get() == 1:
                command = "netsh advfirewall firewall add rule name=blockTokyo dir=out action=block profile=any protocol=any remoteip=45.121.184.0-45.121.184.255,45.121.186.0-45.121.186.255,45.121.187.0-45.121.187.255,61.14.157.0-61.14.157.255,146.66.152.0-146.66.152.255,155.133.239.0-155.133.239.255,155.133.245.0-155.133.245.255"
                subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                messagebox.showinfo("Success", "Tokyo server blocked successfully!")
                status_labels["Tokyo"].config(text="● ", fg='#39FF14')
            else:
                command = "netsh advfirewall firewall delete rule name=blockTokyo"
                subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                messagebox.showinfo("Success", "Tokyo server block removed!")
                status_labels["Tokyo"].config(text="● ", fg='red')
        elif server == "HongKong":
            if checkHongkong.get() == 1:
                command = "netsh advfirewall firewall add rule name=blockHongKong dir=out action=block profile=any protocol=any remoteip=103.28.54.0-103.28.54.255,155.133.244.0-155.133.244.255,153.254.86.0-153.254.86.255"
                subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                messagebox.showinfo("Success", "HongKong server blocked successfully!")
                status_labels["HongKong"].config(text="● ", fg='#39FF14')
            else:
                command = "netsh advfirewall firewall delete rule name=blockHongKong"
                subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                messagebox.showinfo("Success", "HongKong server block removed!")
                status_labels["HongKong"].config(text="● ", fg='red')
        elif server == "India":
            if checkIndia.get() == 1:
                command = "netsh advfirewall firewall add rule name=blockIndia dir=out action=block profile=any protocol=any remoteip=10.130.205.0-10.130.205.255,45.113.191.0-45.113.191.255,116.202.224.0-116.202.224.255,155.133.232.0-155.133.232.255,155.133.233.0-155.133.233.255,180.149.41.0-180.149.41.255,182.79.252.0-182.79.252.255"
                subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                messagebox.showinfo("Success", "India server blocked successfully!")
                status_labels["India"].config(text="● ", fg='#39FF14')
            else:
                command = "netsh advfirewall firewall delete rule name=blockIndia"
                subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                messagebox.showinfo("Success", "India server block removed!")
                status_labels["India"].config(text="● ", fg='red')
        elif server == "Singapore":
            if checkAsia.get() == 1:
                command = "netsh advfirewall firewall add rule name=blockSingapore dir=out action=block profile=any protocol=any remoteip=45.121.184.0-45.121.184.255,45.121.185.0-45.121.185.255,10.156.7.0-10.156.7.255,103.28.54.0-103.28.54.255,103.28.55.0-103.28.55.255,103.10.124.0-103.10.124.255"
                subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                messagebox.showinfo("Success", "Singapore server blocked successfully!")
                status_labels["Singapore"].config(text="● ", fg='#39FF14')
            else:
                command = "netsh advfirewall firewall delete rule name=blockSingapore"
                subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                messagebox.showinfo("Success", "Singapore server block removed!")
                status_labels["Singapore"].config(text="● ", fg='red')

        # SDR 규칙 확인 및 추가
        add_sdr_rule()

    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to apply settings. Make sure you're running as administrator.")

def reset_all_blocks():
    commands = [
        "netsh advfirewall firewall delete rule name=blockSeoul",
        "netsh advfirewall firewall delete rule name=blockTokyo",
        "netsh advfirewall firewall delete rule name=blockHongKong",
        "netsh advfirewall firewall delete rule name=blockIndia",
        "netsh advfirewall firewall delete rule name=blockSingapore",
        "netsh advfirewall firewall delete rule name=blockSDR"
    ]
    
    success = True
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
        except subprocess.CalledProcessError:
            success = False
    
    checkKorea.set(0)
    checkJapan.set(0)
    checkHongkong.set(0)
    checkIndia.set(0)
    checkAsia.set(0)
    
    for label in status_labels.values():
        label.config(fg='red')
    
    if success:
        messagebox.showinfo("Success", "All server blocks have been removed!")
    else:
        messagebox.showinfo("Partial Success", "Some server blocks may not have been removed. Please check your firewall settings.")
        
def all_blocks():
    commands = [
        "netsh advfirewall firewall add rule name=blockSeoul dir=out action=block profile=any protocol=any remoteip=146.66.152.0-146.66.152.255",
        "netsh advfirewall firewall add rule name=blockTokyo dir=out action=block profile=any protocol=any remoteip=45.121.184.0-45.121.184.255,45.121.186.0-45.121.186.255,45.121.187.0-45.121.187.255,61.14.157.0-61.14.157.255,146.66.152.0-146.66.152.255,155.133.239.0-155.133.239.255,155.133.245.0-155.133.245.255",
        "netsh advfirewall firewall add rule name=blockHongKong dir=out action=block profile=any protocol=any remoteip=103.28.54.0-103.28.54.255,155.133.244.0-155.133.244.255,153.254.86.0-153.254.86.255",
        "netsh advfirewall firewall add rule name=blockIndia dir=out action=block profile=any protocol=any remoteip=10.130.205.0-10.130.205.255,45.113.191.0-45.113.191.255,116.202.224.0-116.202.224.255,155.133.232.0-155.133.232.255,155.133.233.0-155.133.233.255,180.149.41.0-180.149.41.255,182.79.252.0-182.79.252.255",
        "netsh advfirewall firewall add rule name=blockSingapore dir=out action=block profile=any protocol=any remoteip=45.121.184.0-45.121.184.255,45.121.185.0-45.121.185.255,10.156.7.0-10.156.7.255,103.28.54.0-103.28.54.255,103.28.55.0-103.28.55.255,103.10.124.0-103.10.124.255"
    ]
    
    success = True
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
        except subprocess.CalledProcessError:
            success = False
            
    checkKorea.set(1)
    checkJapan.set(1)
    checkHongkong.set(1)
    checkIndia.set(1)
    checkAsia.set(1)
    
    for label in status_labels.values():
        label.config(fg='#39FF14')
    
    # SDR 규칙 추가
    add_sdr_rule()
    
    if success:
        messagebox.showinfo("Success", "All servers blocked successfully!")
    else:
        messagebox.showinfo("Error", "Failed to apply settings. Make sure you're running as administrator.")

window = tk.Tk()

window.title("CS2 Server Blocker")
icon_path = resource_path('cs2.ico')
window.iconbitmap(icon_path)
window.geometry("300x450")
window.configure(bg='#1E1E1E')
window.resizable(False, False)  # 창 크기 조정 불가능하게 설정

style = ttk.Style()
style.theme_use('clam')

title_font = font.Font(family="Consolas", size=16, weight="bold")
button_font = font.Font(family="Consolas", size=10)

style.configure('TCheckbutton', background='#1E1E1E', foreground='#39FF14', font=button_font)
style.map('TCheckbutton', 
          foreground=[('active', '#FFFFFF')],
          background=[('active', '#2C3E50')])

style.configure('TButton', font=button_font, background='#39FF14', foreground='#1E1E1E')
style.map('TButton',
          foreground=[('active', '#FFFFFF')],
          background=[('active', '#2C3E50')])

main_frame = tk.Frame(window, bg='#1E1E1E')
main_frame.pack(fill=tk.BOTH, expand=True)

main_frame.columnconfigure(0, weight=0)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=0)  

locationTitle = tk.Label(main_frame, text='CS2 Server Blocker', font=title_font, bg='#1E1E1E', fg='#39FF14')
asiaTitle = tk.Label(main_frame, text='Asia Servers', font=title_font, bg='#1E1E1E', fg='#39FF14')

checkKorea = tk.IntVar()
checkJapan = tk.IntVar()
checkHongkong = tk.IntVar()
checkIndia = tk.IntVar()
checkAsia = tk.IntVar()

locationTitle.grid(row=0, column=0, columnspan=3, pady=(20, 20), sticky='ew')
asiaTitle.grid(row=1, column=0, columnspan=3, pady=(0, 10), sticky='ew')

status_labels = {}

def create_server_row(row, text, variable, command):
    frame = tk.Frame(main_frame, bg='#1E1E1E')
    frame.grid(row=row, column=0, columnspan=3, sticky='ew')
    frame.columnconfigure(1, weight=1)

    icon = tk.Label(frame, text="🖧", bg='#1E1E1E', fg='#39FF14', font=("Segoe UI Symbol", 14))
    icon.grid(row=0, column=0, padx=(20, 5), pady=2, sticky='w')
    
    check = ttk.Checkbutton(frame, text=text, variable=variable, style='TCheckbutton', command=command)
    check.grid(row=0, column=1, padx=(0, 5), pady=2, sticky='ew')
    
    status = tk.Label(frame, text="● ", bg='#1E1E1E', fg='red', font=("Segoe UI Symbol", 14))
    status.grid(row=0, column=2, padx=(0, 20), pady=2, sticky='e')
    status_labels[text] = status

    def toggle(event):
        variable.set(not variable.get())
        command()

    frame.bind("<Button-1>", toggle)
    icon.bind("<Button-1>", toggle)
    check.bind("<Button-1>", lambda e: e.widget.invoke(), add="+")
    status.bind("<Button-1>", toggle)

    spacer = tk.Label(frame, bg='#1E1E1E')
    spacer.grid(row=0, column=3, sticky='nsew')
    spacer.bind("<Button-1>", toggle)

    frame.grid_propagate(False)
    frame.config(height=30)

create_server_row(2, "Seoul", checkKorea, lambda: toggle_server_block("Seoul"))
create_server_row(3, "Tokyo", checkJapan, lambda: toggle_server_block("Tokyo"))
create_server_row(4, "HongKong", checkHongkong, lambda: toggle_server_block("HongKong"))
create_server_row(5, "India", checkIndia, lambda: toggle_server_block("India"))
create_server_row(6, "Singapore", checkAsia, lambda: toggle_server_block("Singapore"))

button_frame = tk.Frame(main_frame, bg='#1E1E1E')
button_frame.grid(row=7, column=0, columnspan=3, pady=(20, 0), sticky='ew')
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

allResetBtn = ttk.Button(button_frame, text="UNBLOCK ALL", command=reset_all_blocks, style='TButton')
allBlockBtn = ttk.Button(button_frame, text="BLOCK ALL", command=all_blocks, style='TButton')

allResetBtn.grid(row=0, column=0, padx=(20, 5), sticky='ew')
allBlockBtn.grid(row=0, column=1, padx=(5, 20), sticky='ew')

ping_btn = ttk.Button(main_frame, text="PING TEST", style='TButton', command=run_ping_test)
ping_btn.grid(row=8, column=0, columnspan=3, pady=(20, 0), padx=20, sticky='ew')

firewall_status = tk.Label(main_frame, text="Made by NameLess\nhttps://github.com/NLessW", font=button_font, bg='#1E1E1E', fg='#39FF14')
firewall_status.grid(row=9, column=0, columnspan=3, pady=(20, 20), sticky='ew')

window.mainloop()
