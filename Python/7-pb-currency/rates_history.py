HISTORY_FILE = "currency_history.txt"
RAW_JSON_RESPONSES = "raw_responses.txt"


def update_file(stringed_info, file_to_update):
    with open(file_to_update, "a+") as file:
        file.seek(0)
        if stringed_info not in file.read():
            file.seek(0)
            lines = file.readlines()
            lines.append(stringed_info)
            lines.append("\n")

            file.writelines(lines)

        file.close()
