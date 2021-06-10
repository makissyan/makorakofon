HISTORY_FILE = "currency_history.txt"


def update_currency_history_file(stringed_info):
    with open(HISTORY_FILE, "a+") as file:
        file.seek(0)
        if stringed_info not in file.read():
            file.seek(0)
            lines = file.readlines()
            lines.append(stringed_info)
            lines.append("\n")

            file.writelines(lines)

        file.close()
