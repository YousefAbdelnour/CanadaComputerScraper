#Script made by Yousef Abdelnour

## Necessary libraries
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn
from rich.traceback import install

## Initializing the Rich handler so the formatting is visible
install()

## Initializing the console
console = Console()

## Initial Panel
header = Panel(
    "[bold magenta]Canada Computers Inventory Checker[/bold magenta]\n[v1.0] Check product availability in real time!",
    title=":mag: Inventory Checker :mag:",
    border_style="bright_blue"
)
console.print(header)

## Credentials for Twilio
TWILIO_SID = "YOUR SID"
TWILIO_AUTH_TOKEN = "YOUR AUTH TOKEN"
TWILIO_PHONE_NUMBER = "YOUR TWILIO PHONE NUMBER"
YOUR_PHONE_NUMBER = "MESSAGE RECIPIENT"

## Products you want to check
PRODUCT_URLS = [ ## Add your own links, this is an example
    "https://www.canadacomputers.com/en/powered-by-nvidia/268138/gigabyte-geforce-rtx-5080-gaming-oc-ai-gaming-graphics-card-gv-n5080gaming-oc-16gd.html",
]

## Checking if the add to cart button is there (It will not be if it is not in stock, only applicable to Canada Computers)
def is_in_stock(soup):
    """
    Checks if the 'Add to cart' button is present in the page.
    If found, we assume the product is in stock.
    """
    add_to_cart_button = soup.find("button", {"data-button-action": "add-to-cart"})
    return add_to_cart_button is not None

## Request to the webpage and progress bar handling
def check_inventory():
    headers = {"User-Agent": "Mozilla/5.0"}
    in_stock_products = []
    
    with Progress(
        SpinnerColumn(style="cyan"),
        BarColumn(bar_width=40, style="magenta"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeRemainingColumn(),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("[bold green]Checking inventory...[/bold green]", total=len(PRODUCT_URLS))
        
        for url in PRODUCT_URLS:
            try:
                response = requests.get(url, headers=headers)
            except Exception as e:
                console.log(f"[yellow][EXCEPTION][/yellow] {url}: {e}")
                progress.advance(task)
                continue
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                if is_in_stock(soup):
                    in_stock_products.append(url)
                    console.log(f"[green]IN STOCK[/green] → {url}")
                else:
                    console.log(f"[red]OUT OF STOCK[/red] → {url}")
            else:
                console.log(f"[yellow]ERROR[/yellow] {url}: HTTP {response.status_code}")
            progress.advance(task)
    
    return in_stock_products

## Sending a text message using the credentials from Twilio
def send_text_message(products):
    if products:
        message = "In stock! Go to Canada Computers NOW!\n" + "\n".join(products)
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_PHONE_NUMBER
        )
        console.print(Panel("[bold blue]Notification sent via SMS.[/bold blue]", border_style="blue"))

## Main Running sequence
if __name__ == "__main__":
    console.rule("[bold green]Starting Inventory Check[/bold green]")
    available = check_inventory()
    console.rule("[bold green]Inventory Check Complete[/bold green]")
    
    if available:
        panel_message = "\n".join(available)
        summary = Panel(
            f"[bold green]Found {len(available)} product(s) in stock![/bold green]\n{panel_message}",
            title=":white_check_mark: In Stock",
            border_style="green"
        )
        console.print(summary)
        send_text_message(available)
    else:
        console.print(Panel("[bold red]No stock available.[/bold red]", title=":x: Out of Stock", border_style="red"))
