import time
import random
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.align import Align
from datetime import datetime

console = Console()

def get_timestamp():
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]

def generate_banner():
    print("GITHUB : ISTIMAEDE")
    banner = """
    ██▓  ██████  ██▓▄▄▄█████▓███▄    █  ▄▄▄       █████▒▓█████ 
    ▓██▒▒██    ▒ ▓██▒▓  ██▒ ▓▒██ ▀█   █ ▒████▄   ▓██   ▒ ▓█   ▀ 
    ▒██▒░ ▓██▄   ▒██▒▒ ▓██░ ▒░██  ▀█ ██▒▒██  ▀█▄ ▒████ ░ ▒███   
    ░██░  ▒   ██▒░██░░ ▓██▓ ░ ██▒  ▐▌██▒░██▄▄▄▄██░▓█▒  ░ ▒▓█  ▄ 
    ░██░▒██████▒▒░██░  ▒██▒ ░ ▒██░   ▓██░▓█   ▓██▒░▒█░   ░▒████▒
    """
    return Panel(Align.center(banner, style="bold red"), subtitle="[v2.1.2 Production]", border_style="red")
    

def main():
    console.clear()
    console.print(generate_banner())
    
    target = console.input("[bold yellow][?] Target Host: [/bold yellow]")
    try:
        limit = int(console.input("[bold yellow][?] Request Limit: [/bold yellow]"))
    except:
        limit = 500

    console.print(f"\n[bold cyan][*] Initializing Attack Vectors on {target}...[/bold cyan]")
    time.sleep(1.5)

    buffer = []

    with Live(console=console, refresh_per_second=15) as live:
        for i in range(1, limit + 1):
            ratio = i / limit
            
            if ratio < 0.75:
                status = "[bold green]200 OK[/bold green]"
                latency = f"{random.randint(20, 50)}ms"
                msg = "SUCCESS"
                sleep_time = 0.02
            elif ratio < 0.92:
                status = "[bold yellow]429 BUSY[/bold yellow]"
                latency = f"{random.randint(500, 1500)}ms"
                msg = "THROTTLED"
                sleep_time = 0.08
            else:
                status = "[bold red]503 DOWN[/bold red]"
                latency = "[bold red]TIMEOUT[/bold red]"
                msg = "FAILED"
                sleep_time = 0.15

            buffer.append([get_timestamp(), "POST", status, latency, msg])
            
            if len(buffer) > 10:
                buffer.pop(0)

            table = Table(expand=True, border_style="grey30")
            table.add_column("TIMESTAMP", width=15)
            table.add_column("METHOD", justify="center")
            table.add_column("STATUS", justify="center")
            table.add_column("LATENCY")
            table.add_column("RESPONSE")

            for row in buffer:
                table.add_row(*row)
            
            live.update(table)
            time.sleep(sleep_time)

    console.print("\n[bold red][!] ALERT: CONNECTION RESET BY PEER - TARGET IS UNRESPONSIVE[/bold red]")
    
    with Progress(SpinnerColumn(), TextColumn("[bold red]{task.description}"), console=console) as progress:
        task = progress.add_task("Verifying Shutdown...", total=100)
        while not progress.finished:
            progress.update(task, advance=random.uniform(1, 5))
            time.sleep(0.1)

    result_content = f"""
    [bold white]SIMULATION SUMMARY[/bold white]
    --------------------------
    Target Endpoint : [cyan]{target}[/cyan]
    Packets Routed  : [white]{limit}[/white]
    Peak Latency    : [red]INF[/red]
    Final State     : [bold red]OFFLINE[/bold red]

    [italic grey50]Infrastructure collapse detected at {get_timestamp()}[/italic grey50]
    """
    console.print(Panel(Align.center(result_content), title="[bold red]TERMINAL REPORT[/bold red]", border_style="bold red"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)