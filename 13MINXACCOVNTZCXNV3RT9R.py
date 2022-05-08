from pyfiglet import figlet_format
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(figlet_format("13MINXACCOVNTZCXNV3RT9R", font="small", width=57))


def converting_process(password: str):
    emails_txt = open("emails.txt", "r")
    accounts_json = open("accounts.json", "a")
    accounts_json.write("[")
    for line in emails_txt:
        email = line.strip()
        accounts_json.write(
            f'\n{{\n"email": "{email}",\n"password": "{password}"\n}},')
    accounts_json.write("\n}\n]")
    accounts_json.close()
    print(f"Converted all accounts!")


converting_process(password=input("-- Password For All Accounts::: "))
