import tkinter as tk
from tkinter import font, messagebox
import subprocess

def toggle_server_block(server):
    try:
        if server == "Seoul":
            if checkKorea.get() == 1:
                command = "netsh advfirewall firewall add rule name=blockSeoul dir=out action=block profile=any protocol=any remoteip=146.66.152.0-146.66.152.255"
                subprocess.run(command, shell=True, check=True)
                messagebox.showinfo("Success", "Seoul server blocked successfully!")
            else:
                command = "netsh advfirewall firewall delete rule name=blockSeoul"
                subprocess.run(command, shell=True, check=True)
                messagebox.showinfo("Success", "Seoul server block removed!")
        elif server == "Tokyo":
            if checkJapan.get() == 1:
                command = "netsh advfirewall firewall add rule name=blockTokyo dir=out action=block profile=any protocol=any remoteip=45.121.184.0-45.121.184.255,45.121.186.0-45.121.186.255,45.121.187.0-45.121.187.255,61.14.157.0-61.14.157.255,146.66.152.0-146.66.152.255,155.133.239.0-155.133.239.255,155.133.245.0-155.133.245.255"
                subprocess.run(command, shell=True, check=True)
                messagebox.showinfo("Success", "Tokyo server blocked successfully!")
            else:
                command = "netsh advfirewall firewall delete rule name=blockTokyo"
                subprocess.run(command, shell=True, check=True)
                messagebox.showinfo("Success", "Tokyo server block removed!")
        elif server == "HongKong":
            if checkHongkong.get() == 1:
                command = "netsh advfirewall firewall add rule name=blockHongKong dir=out action=block profile=any protocol=any remoteip=103.28.54.0-103.28.54.255,155.133.244.0-155.133.244.255,153.254.86.0-153.254.86.255"
                subprocess.run(command, shell=True, check=True)
                messagebox.showinfo("Success", "HongKong server blocked successfully!")
            else:
                command = "netsh advfirewall firewall delete rule name=blockHongKong"
                subprocess.run(command, shell=True, check=True)
                messagebox.showinfo("Success", "HongKong server block removed!")
        elif server == "India":
            if checkIndia.get() == 1:
                command = "netsh advfirewall firewall add rule name=blockIndia dir=out action=block profile=any protocol=any remoteip=10.130.205.0-10.130.205.255,45.113.191.0-45.113.191.255,116.202.224.0-116.202.224.255,155.133.232.0-155.133.232.255,155.133.233.0-155.133.233.255,180.149.41.0-180.149.41.255,182.79.252.0-182.79.252.255"
                subprocess.run(command, shell=True, check=True)
                messagebox.showinfo("Success", "India server blocked successfully!")
            else:
                command = "netsh advfirewall firewall delete rule name=blockIndia"
                subprocess.run(command, shell=True, check=True)
                messagebox.showinfo("Success", "India server block removed!")
        elif server == "Singapore":
            if checkAsia.get() == 1:
                command = "netsh advfirewall firewall add rule name=blockSingapore dir=out action=block profile=any protocol=any remoteip=45.121.184.0-45.121.184.255,45.121.185.0-45.121.185.255,10.156.7.0-10.156.7.255,103.28.54.0-103.28.54.255,103.28.55.0-103.28.55.255,103.10.124.0-103.10.124.255"
                subprocess.run(command, shell=True, check=True)
                messagebox.showinfo("Success", "Singapore server blocked successfully!")
            else:
                command = "netsh advfirewall firewall delete rule name=blockSingapore"
                subprocess.run(command, shell=True, check=True)
                messagebox.showinfo("Success", "Singapore server block removed!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to apply settings. Make sure you're running as administrator.")

def reset_all_blocks():
    commands = [
        "netsh advfirewall firewall delete rule name=blockSeoul",
        "netsh advfirewall firewall delete rule name=blockTokyo",
        "netsh advfirewall firewall delete rule name=blockHongKong",
        "netsh advfirewall firewall delete rule name=blockIndia",
        "netsh advfirewall firewall delete rule name=blockSingapore"
    ]
    
    success = True
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError:
            success = False
    
    checkKorea.set(0)
    checkJapan.set(0)
    checkHongkong.set(0)
    checkIndia.set(0)
    checkAsia.set(0)
    
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
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError:
            success = False
            
    checkKorea.set(1)
    checkJapan.set(1)
    checkHongkong.set(1)
    checkIndia.set(1)
    checkAsia.set(1)
    if success:
        messagebox.showinfo("Success", "All server blocks successfully!")
    else:
        messagebox.showinfo("Error", "Failed to apply settings. Make sure you're running as administrator.")
        
window = tk.Tk()

window.title("CS2 Server Blocker")
window.iconbitmap('cs2.ico')
window.geometry("300x300")

title_font = font.Font(family="Arial", size=15, weight="bold")
button_font = font.Font(family="Arial", size=12)

locationTitle = tk.Label(window, text='Select Location', font=title_font)
asiaTitle = tk.Label(window, text='Asia', font=title_font)

checkKorea = tk.IntVar()
checkJapan = tk.IntVar()
checkHongkong = tk.IntVar()
checkIndia = tk.IntVar()
checkAsia = tk.IntVar()

checkKoreaBtn = tk.Checkbutton(window, text="Seoul", variable=checkKorea, font=button_font, anchor='w', command=lambda: toggle_server_block("Seoul"))
checkJapanBtn = tk.Checkbutton(window, text="Tokyo", variable=checkJapan, font=button_font, anchor='w', command=lambda: toggle_server_block("Tokyo"))
checkHongkongBtn = tk.Checkbutton(window, text="Hong Kong", variable=checkHongkong, font=button_font, anchor='w', command=lambda: toggle_server_block("HongKong"))
checkIndiaBtn = tk.Checkbutton(window, text="India", variable=checkIndia, font=button_font, anchor='w', command=lambda: toggle_server_block("India"))
checkAsiaBtn = tk.Checkbutton(window, text="Singapore", variable=checkAsia, font=button_font, anchor='w', command=lambda: toggle_server_block("Singapore"))
allResetBtn = tk.Button(window, text="All Unblock", command=reset_all_blocks, font=button_font)
allBlockBtn = tk.Button(window, text="All Block",command=all_blocks,font=button_font)
locationTitle.pack(side="top", pady=(0, 5))
asiaTitle.pack(pady=(0, 10)) 

checkKoreaBtn.pack(anchor='w', fill='x', pady=3, padx=10)
checkJapanBtn.pack(anchor='w', fill='x', pady=3, padx=10)
checkHongkongBtn.pack(anchor='w', fill='x', pady=3, padx=10)
checkIndiaBtn.pack(anchor='w', fill='x', pady=3, padx=10)
checkAsiaBtn.pack(anchor='w', fill='x', pady=3, padx=10)
allResetBtn.pack(side="left", padx=10)
allBlockBtn.pack(side="left",padx=10)
window.mainloop()
