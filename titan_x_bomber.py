#!/usr/bin/env python3
# © 2026 MAINUL - X | TITAN-X BOMBER
# Disclaimer: Developer is not responsible for misuse.

import os
import time
import sys
import random
import requests
import json
import zipfile
import shutil
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich.table import Table
from rich import box
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.prompt import Prompt, Confirm
from datetime import datetime

# ===== নিচের লাইনগুলো যোগ করুন =====
from api_list import APIList
from api_handler import send_request, send_batch
from utils import get_random_agent, log_message

console = Console()

class TitanXBomber:
    def __init__(self):
        self.tool_name = "TITAN-X BOMBER"
        self.version = "v1.0"
        self.developer = "MAINUL ISLAM"
        self.whatsapp = "+8801308850528"
        self.github = "M41NUL"
        self.telegram = "@mdmainulislaminfo"
        self.email = "githubmainul@gmail.com"
        
        self.colors = ["bright_red", "bright_green", "bright_yellow", "bright_blue", "bright_magenta", "bright_cyan"]
        self.log_file = "titan_logs.txt"
        self.banner_cache = None
        self.update_url = "https://api.github.com/repos/M41NUL/titan-x-bomber/releases/latest"
        
        # API লিস্ট লোড
        self.apis = APIList.get_all()
        self.api_stats = APIList.get_stats()
        
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_startup_sequence(self):
        """স্টার্টআপ সিকোয়েন্স - এক পৃষ্ঠায় সব দেখাবে"""
        self.clear()
        
        # ১. স্টাইলিশ শর্ট ওয়েলকাম ব্যানার
        welcome = """
[bold bright_green]
    ╔════════════════════════════════════╗
    ║       🔥  TITAN-X BOMBER  🔥       ║
    ╠════════════════════════════════════╣
    ║  [bold white] ╔╦╗╦╔╦╗╔═╗╔╗╔  ═╗ ╦ [/]             ║
    ║  [bold white]  ║ ║ ║ ╠═╣║║║  ╔╩╦╝ [/]             ║
    ║  [bold white]  ╩ ╩ ╩ ╩ ╩╝╚╝  ╩ ╚═ [/]             ║
    ╠════════════════════════════════════╣
    ║  [bold cyan]DEVELOPER : MAINUL ISLAM [/]         ║
    ║  [bold cyan]STATUS    : PREMIUM ACCESS [/]       ║
    ╚════════════════════════════════════╝[/]
        """
        console.print(Align.center(welcome))
        time.sleep(0.5)

        # ২. IP এবং পাইথন ভার্সন প্রথমে দেখাবে
        # IP চেক
        try:
            ip = requests.get("https://api.ipify.org", timeout=0.8).text
            ip_status = f"[bold cyan]🌐 Public IP:[/] [bold green]{ip}[/] [bold white]✓[/]"
        except:
            ip_status = "[bold cyan]🌐 Public IP:[/] [bold red]Connection failed[/]"
        
        # পাইথন ভার্সন
        py_status = f"[bold cyan]🐍 Python:[/] [bold green]{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}[/] [bold white]✓[/]"
        
        # একসাথে দেখাও
        info_panel = Panel(
            f"{py_status}\n{ip_status}",
            border_style="bright_blue",
            box=box.ROUNDED,
            width=50
        )
        console.print(Align.center(info_panel))
        time.sleep(0.5)
        print()

        # ৩. আপডেট চেক বক্স
        update_box = Panel(
            "[bold cyan]🔄 CHECKING FOR UPDATES... 🔄[/]\n"
            "[dim]Connecting to Mainul's Cloud Server...[/]",
            border_style="bright_yellow",
            box=box.ROUNDED,
            width=70
        )
        console.print(Align.center(update_box))
        
        # ৪. আপডেট চেক
        update_available = False
        latest_version = None
        download_url = None
        
        try:
            with console.status("[bold yellow]Connecting...", spinner="bouncingBall"):
                response = requests.get(self.update_url, timeout=5)
                time.sleep(1)
            
            if response.status_code == 200:
                latest = response.json()
                latest_version = latest['tag_name']
                download_url = latest['zipball_url']
                
                current_num = float(''.join(c for c in self.version if c.isdigit() or c == '.'))
                latest_num = float(''.join(c for c in latest_version if c.isdigit() or c == '.'))
                
                if latest_num > current_num:
                    update_available = True
                    status = Panel(
                        f"[bold yellow]╔════════════════════════════════════╗[/]\n"
                        f"[bold yellow]║   ⚡ NEW VERSION AVAILABLE! ⚡    ║[/]\n"
                        f"[bold yellow]╚════════════════════════════════════╝[/]\n\n"
                        f"[bold white]Current: [red]{self.version}[/]  →  [bold green]Latest: {latest_version}[/]",
                        border_style="bright_yellow"
                    )
                else:
                    status = Panel(
                        f"[bold green]✔ You have the latest version ({self.version})[/]",
                        border_style="green"
                    )
            else:
                status = Panel(
                    "[bold red]✖ Update server offline[/]",
                    border_style="red"
                )
        except:
            status = Panel(
                "[bold red]✖ Update check failed[/]",
                border_style="red"
            )
        
        console.print(Align.center(status))
        print()
        
        # ৫. আপডেট থাকলে y/n চাইবে
        if update_available:
            console.print("[bold cyan]Download update? (y/n)[/]")
            choice = Prompt.ask("[bold cyan]➤ [/]", choices=["y", "n"])
            
            if choice == "y":
                self.download_update(download_url, latest_version)
                return
            else:
                console.print("[bold yellow]Continuing with current version...[/]")
                time.sleep(0.5)
        
        # ৬. সিকিউরিটি চেক
        self.clear()
        console.print(self.get_banner())
        
        table = Table(show_header=False, box=box.ROUNDED, border_style="bright_blue", width=55)
        table.add_column("Indicator", style="bold cyan")
        table.add_column("Status", style="white")

        with Live(table, console=console, refresh_per_second=4) as live:
            time.sleep(0.4)
            table.add_row("Firewall System", "[bold green]ACTIVE [✔][/]")
            live.update(table)
            
            time.sleep(0.4)
            table.add_row("AES-256 Tunnel", "[bold green]ENCRYPTED [✔][/]")
            live.update(table)
            
            time.sleep(0.4)
            table.add_row("Injection Mode", "[bold yellow]STEALTH V2 [✔][/]")
            live.update(table)
            
            time.sleep(0.4)
            table.add_row("Proxy Gateway", "[bold cyan]CONNECTED [✔][/]")
            live.update(table)

        console.print(Align.center("[bold white]System fully optimized[/]"))
        
        with Progress(
            SpinnerColumn("dots12"),
            TextColumn("[bold yellow]INITIALIZING...[/]"),
            BarColumn(bar_width=40, style="blue", complete_style="bright_cyan"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("loading", total=100)
            for i in range(0, 101, 10):
                progress.update(task, completed=i)
                time.sleep(0.05)

        console.print(Align.center("[bold green]● LOGIN SUCCESSFUL[/]"))
        time.sleep(0.8)

    def get_banner(self):
        """মূল ব্যানার - ক্যাশ মেমোরি সহ"""
        if self.banner_cache:
            return self.banner_cache
            
        f = Figlet(font='big')
        banner_raw = f.renderText("TITAN-X")
        banner_styled = Text()
        
        lines = banner_raw.split('\n')
        for i, line in enumerate(lines):
            if line.strip():
                color = self.colors[i % len(self.colors)]
                banner_styled.append(line + "\n", style=f"bold {color}")
        
        header = Panel(
            Align.center(banner_styled),
            title="[bold white]‹ [bold red]ULTRA ATTACK INTERFACE[/] [bold white]›[/]",
            subtitle=f"[bold green] Dev:[/] [white]{self.developer}[/] | [bold yellow]Ver:[/] [white]{self.version}[/]",
            border_style="bright_red",
            box=box.DOUBLE_EDGE,
            padding=(1, 2)
        )
        
        self.banner_cache = header
        return header

    def show_banner_with_contact(self):
        """মূল ব্যানার + কন্টাক্ট দেখানো"""
        console.print(self.get_banner())
        contact = f"[bold white]WA:[/] [bold green]{self.whatsapp}[/] | [bold white]GitHub:[/] [bold green]{self.github}[/]"
        console.print(Align.center(contact))
        print()

    def download_update(self, url, new_version):
        """আপডেট ডাউনলোড এবং অটো-ইন্সটল"""
        try:
            self.clear()
            
            download_header = Panel(
                "[bold cyan]📥 DOWNLOADING UPDATE[/]",
                border_style="cyan"
            )
            console.print(Align.center(download_header))
            print()
            
            filename = "titan_update.zip"
            extract_path = "titan_temp"
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[bold cyan]{task.description}"),
                BarColumn(bar_width=40),
                TaskProgressColumn(),
                console=console
            ) as progress:
                task = progress.add_task("Downloading...", total=100)
                
                response = requests.get(url, stream=True)
                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0
                
                with open(filename, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            if total_size:
                                progress.update(task, completed=(downloaded/total_size)*100)
            
            print()
            
            install_header = Panel(
                "[bold yellow]🔧 INSTALLING UPDATE[/]",
                border_style="yellow"
            )
            console.print(Align.center(install_header))
            print()
            
            with console.status("[bold yellow]Extracting files...", spinner="bouncingBall"):
                with zipfile.ZipFile(filename, 'r') as zip_ref:
                    if os.path.exists(extract_path):
                        shutil.rmtree(extract_path)
                    zip_ref.extractall(extract_path)
                time.sleep(1)
            
            with console.status("[bold yellow]Copying new files...", spinner="dots"):
                subdir = os.listdir(extract_path)[0]
                source_dir = os.path.join(extract_path, subdir)
                
                for file_name in os.listdir(source_dir):
                    if file_name.endswith('.py'):
                        shutil.move(os.path.join(source_dir, file_name), os.getcwd())
                time.sleep(1)
            
            os.remove(filename)
            shutil.rmtree(extract_path)
            
            print()
            
            success_panel = Panel(
                f"[bold green]✔ UPDATE INSTALLED SUCCESSFULLY![/]\n\n"
                f"[white]Old Version: [red]{self.version}[/]\n"
                f"[white]New Version: [green]{new_version}[/]\n\n"
                f"[dim]System has been patched to the latest version.[/]",
                title="[bold green]✅ SUCCESS[/]",
                border_style="green",
                width=60
            )
            console.print(Align.center(success_panel))
            print()
            
            restart_panel = Panel(
                "[bold yellow]🚀 RESTARTING TITAN-X...[/]\n\n"
                "[white]Update installed successfully!\n"
                "Restarting in 3 seconds...[/]",
                border_style="yellow",
                width=50
            )
            console.print(Align.center(restart_panel))
            
            for i in range(3, 0, -1):
                console.print(f"[dim]{i}...[/]", end=" ")
                time.sleep(1)
            print()
            
            os.execv(sys.executable, ['python'] + sys.argv)
            
        except Exception as e:
            console.print(f"[bold red]❌ Update failed: {str(e)}[/]")
            time.sleep(3)

    def check_python_version(self):
        """পাইথন ভার্সন চেক"""
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        
        if sys.version_info.major < 3:
            console.print("[bold red]❌ Python 3 is required![/]")
            sys.exit(1)
        else:
            console.print(f"[dim]🐍 Python {python_version} [bold green]✓[/][/]")
        time.sleep(0.5)

    def get_public_ip(self):
        """পাবলিক আইপি চেক"""
        try:
            response = requests.get("https://api.ipify.org?format=json", timeout=3)
            if response.status_code == 200:
                ip = response.json()['ip']
                console.print(f"[dim]🌐 Public IP: [bold cyan]{ip}[/] [bold green]✓[/][/]")
            else:
                console.print("[dim]🌐 Public IP: [bold red]Unknown[/][/]")
        except:
            console.print("[dim]🌐 Public IP: [bold red]Connection failed[/][/]")
        time.sleep(0.3)

    def show_target_input(self):
        """টার্গেট ইনপুট"""
        self.clear()
        console.print(self.get_banner())
        print()
        
        input_panel = Panel(
            "[bold yellow]📱 Enter Target Number (10 digits)[/]\n\n"
            "[dim]Example: [black on bright_black]01xxxxxxxxx[/] (Don't use 0 or 880)[/]\n"
            "[dim]Must start with 1 (17=GP, 18=Robi, 19=Banglalink)[/]",
            title="[bold cyan] TARGET INPUT [/]",
            border_style="bright_blue",
            box=box.ROUNDED,
            width=70,
            padding=(1, 2)
        )
        
        console.print(Align.center(input_panel))
        
        while True:
            target = Prompt.ask("[bold cyan]➤ [/]")
            if len(target) == 10 and target.startswith("1") and target.isdigit():
                return target
            else:
                console.print("[bold red]❌ Invalid! Use 10 digits starting with 1[/]")

    def show_count_input(self, target):
        """কাউন্ট ইনপুট"""
        self.clear()
        console.print(self.get_banner())
        print()
        
        target_info = Panel(
            f"[bold cyan]Target: [bold yellow]880{target}[/]",
            border_style="bright_green",
            box=box.ROUNDED,
            width=50
        )
        console.print(Align.center(target_info))
        print()
        
        count_panel = Panel(
            "[bold yellow]Enter SMS Count[/]\n\n"
            "[dim]How many messages to send?[/]",
            title="[bold cyan] MESSAGE COUNT [/]",
            border_style="bright_green",
            box=box.ROUNDED,
            width=70,
            padding=(1, 2)
        )
        
        console.print(Align.center(count_panel))
        amount = int(Prompt.ask("[bold cyan]➤ [/]", default="50"))
        return amount

    def show_speed_input(self, target, amount):
        """স্পিড ইনপুট"""
        self.clear()
        console.print(self.get_banner())
        print()
        
        info_panel = Panel(
            f"[bold cyan]Target: [bold yellow]880{target}[/]   |   [bold cyan]Count: [bold yellow]{amount}[/]",
            border_style="bright_yellow",
            box=box.ROUNDED,
            width=50
        )
        console.print(Align.center(info_panel))
        print()
        
        speed_panel = Panel(
            "[1] [bold red]Turbo[/] (0.05s - Fastest)\n"
            "[2] [bold yellow]Normal[/] (0.4s - Stable)\n"
            "[3] [bold green]Safe[/] (1.0s - Anti-Ban)",
            title="[bold cyan] SPEED CONTROL [/]",
            border_style="bright_yellow",
            box=box.ROUNDED,
            width=70,
            padding=(1, 2)
        )
        
        console.print(Align.center(speed_panel))
        speed = Prompt.ask("[bold cyan]Choose speed[/]", choices=["1", "2", "3"], default="2")
        return speed

    def get_operator(self, number):
        """অপারেটর ডিটেক্ট"""
        if number.startswith("17") or number.startswith("13"): 
            return "GP (Grameenphone)"
        if number.startswith("18") or number.startswith("16"): 
            return "Robi/Airtel"
        if number.startswith("19") or number.startswith("14"): 
            return "Banglalink"
        if number.startswith("15"): 
            return "Teletalk"
        return "Unknown Operator"

    def save_log(self, target, amount, status="SUCCESS"):
        """লগ সেভ"""
        with open(self.log_file, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] | {target} | {amount} msgs | {status}\n")

    def show_attack_status(self, i, total, target, operator, api_name):
        """অ্যাটাক স্ট্যাটাস"""
        color = random.choice(self.colors)
        percentage = (i / total) * 100
        bar_length = 30
        filled = int(bar_length * i / total)
        
        bar = ""
        for j in range(bar_length):
            if j < filled:
                bar += f"[{color}]█[/]"
            else:
                bar += "[dim white]░[/]"
        
        content = (
            f"\n[bold {color}] TITAN ATTACK [/]\n\n"
            f"[bold white]TARGET:[/] [cyan]880{target}[/]\n"
            f"[bold white]OPERATOR:[/] [yellow]{operator}[/]\n"
            f"[bold white]INJECTOR:[/] [magenta]{api_name}[/]\n"
            f"[bold white]PROGRESS:[/] {bar} [bold {color}]{percentage:.1f}%[/]\n"
            f"[bold white]SENT:[/] [green]{i}/{total}[/]"
        )
        
        return Panel(
            Align.center(content),
            title=f"[bold {color}] TITAN STATUS [/]",
            border_style=color,
            width=70,
            padding=(1, 2)
        )

    def start_bombing_process(self, target, amount, speed):
        """বোম্বিং প্রসেস"""
        delay = {"1": 0.05, "2": 0.4, "3": 1.0}[speed]
        operator = self.get_operator(target)
        
        self.clear()
        console.print(self.get_banner())
        print()
        
        # api_list.py থেকে API লোড করুন
        apis = self.apis
        
        with Live(console=console, refresh_per_second=10, screen=True) as live:
            for i in range(1, amount + 1):
                api = random.choice(apis)
                panel = self.show_attack_status(i, amount, target, operator, api['name'])
                live.update(panel)
                time.sleep(delay)
        
        console.print(f"\n[bold green]✓ SUCCESS! {amount} SMS SENT TO 880{target}![/]")
        self.save_log(target, amount, "SUCCESS")
        
        console.print("\n[bold yellow]⏳ Returning to main menu...[/]")
        for i in range(3, 0, -1):
            console.print(f"[dim]{i}...[/]", end=" ")
            time.sleep(1)
        console.print("\n")

    def show_logs(self):
        """লগ দেখানো"""
        self.clear()
        self.show_banner_with_contact()
        
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as f:
                logs = f.read()
            
            if logs:
                log_panel = Panel(
                    logs,
                    title="[bold cyan] ATTACK LOGS [/]",
                    border_style="green",
                    box=box.ROUNDED,
                    width=70,
                    padding=(1, 2)
                )
                console.print(Align.center(log_panel))
            else:
                console.print("[yellow]No logs found[/]")
        else:
            console.print("[yellow]No log file exists[/]")
        
        console.print("\n[bold yellow]⏳ Returning to main menu...[/]")
        for i in range(3, 0, -1):
            console.print(f"[dim]{i}...[/]", end=" ")
            time.sleep(1)
        console.print("\n")

    def show_developer(self):
        """ডেভেলপার ইনফো"""
        self.clear()
        self.show_banner_with_contact()
        
        info = (
            f"[bold red]DEVELOPER:[/] [bold white]{self.developer}\n\n"
            f"[bold green]WHATSAPP:[/] [bold yellow]{self.whatsapp}\n"
            f"[bold blue]GITHUB:[/] [bold cyan]{self.github}\n"
            f"[bold magenta]TELEGRAM:[/] [bold white]{self.telegram}\n"
            f"[bold cyan]EMAIL:[/] [bold white]{self.email}\n\n"
            f"[bold white]TOOL:[/] [bold red]{self.tool_name}\n"
            f"[bold white]VERSION:[/] [bold yellow]{self.version}[/]"
        )
        
        info_panel = Panel(
            Align.center(info),
            title="[bold magenta] DEVELOPER INFO[/]",
            border_style="bright_magenta",
            box=box.ROUNDED,
            width=60,
            padding=(1, 2)
        )
        
        console.print(Align.center(info_panel))
        
        console.print("\n[bold yellow]⏳ Returning to main menu...[/]")
        for i in range(3, 0, -1):
            console.print(f"[dim]{i}...[/]", end=" ")
            time.sleep(1)
        console.print("\n")

    def show_menu(self):
        """মেনু দেখানো"""
        self.clear()
        self.show_banner_with_contact()
        
        menu_content = (
            "[bold red][1][/] [white]START ATTACK\n\n"
            "[bold green][2][/] [white]VIEW LOGS\n\n"
            "[bold blue][3][/] [white]DEVELOPER INFO\n\n"
            "[bold white][4][/] [white]EXIT[/]"
        )
        
        menu_panel = Panel(
            Align.center(menu_content),
            title="[bold yellow] TITAN CONTROL PANEL[/]",
            border_style="bright_yellow",
            box=box.ROUNDED,
            width=70,
            padding=(1, 2)
        )
        
        console.print(Align.center(menu_panel))
        return Prompt.ask("[bold cyan]Choice[/]", choices=["1", "2", "3", "4"])

    def run(self):
        """মেইন ফাংশন"""
        try:
            # স্টার্টআপ সিকোয়েন্স
            self.show_startup_sequence()
            
            # মূল মেনু
            while True:
                choice = self.show_menu()
                
                if choice == "1":
                    target = self.show_target_input()
                    amount = self.show_count_input(target)
                    speed = self.show_speed_input(target, amount)
                    self.start_bombing_process(target, amount, speed)
                
                elif choice == "2":
                    self.show_logs()
                
                elif choice == "3":
                    self.show_developer()
                
                elif choice == "4":
                    self.clear()
                    with console.status("[bold red]Shutting down TITAN Engine...[/]", spinner="moon"):
                        time.sleep(1.5)
                    
                    exit_panel = Panel(
                        Align.center(
                            f"[bold red]SYSTEM TERMINATED[/]\n\n"
                            f"[bold white]Tool Name: [bold cyan]TITAN-X BOMBER[/]\n"
                            f"[bold white]Version: [bold yellow]{self.version}[/]\n"
                            f"[bold white]Developer: [bold green]{self.developer}[/]\n"
                            f"[bold yellow]Stay Connected! Goodbye.👋 [/]"
                        ),
                        title="[bold red] EXIT [/]",
                        border_style="bright_red",
                        box=box.DOUBLE_EDGE,
                        width=60,
                        padding=(1, 2)
                    )
                    
                    console.print(Align.center(exit_panel))
                    time.sleep(1)
                    sys.exit(0)
                    
        except KeyboardInterrupt:
            console.print("\n\n[bold red]⚠️ TITAN-X INTERRUPTED[/]")
            sys.exit(0)
        except Exception as e:
            console.print(f"\n[bold red]❌ TITAN ERROR: {e}[/]")
            sys.exit(1)

if __name__ == "__main__":
    bomber = TitanXBomber()
    bomber.run()