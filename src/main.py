import random, sys
from colorama import init, Fore, Back, Style

def main():
    elmnts = get_elements()
    print("Enter the atomic number of the given elements.")
    while True:
        try:
            elmnt = random.choice(elmnts)
            print(f"\nElement: {elmnt.get('name')}")
            at_no = input(">>> ")
            try: 
                at_no = int(at_no)
            except ValueError:
                print(f"That's not even a number, baka!\nAnyway the correct answer is {elmnt.get('number')}")
            if at_no == elmnt.get('number'):
                print("Good job!")
            else: 
                print(f"{Fore.RED}Not really...{Fore.WHITE} it's actually {elmnt.get('number')}")
        except EOFError:
            print("\nFine I will exit... baka.")
            sys.exit(0)

def get_elements():
    from json import loads
    from json.decoder import JSONDecodeError

    try:
        with open('data/periodic_table.json', 'r', encoding='utf-8') as f:
            try:
                elmnts = loads(f.read())
            except JSONDecodeError:
                print_err("corrupt")
    except FileNotFoundError:
        print_err("missing")

    return elmnts.get("elements")

def print_err(reason: str):
    print(f"{Fore.RED}ERROR: `periodic_table.json` is {reason}.")
    print(f"Visit {Fore.BLUE}https://github.com/dotmashrc/periodic_table#errors{Fore.WHITE} for more info.")
    sys.exit(1)


if __name__ == '__main__':
    init(autoreset=True)
    main()