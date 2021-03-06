import os
import sys

import xml.etree.ElementTree as ET


# Reel's structure
class Reel:
    def __init__(self, id, symbols):
        self.id = id
        self.symbols = symbols


# Getting unique symbols from reel
def get_unique(symbols):
    unique_symbols = []
    for symbol in symbols:
        if symbol in unique_symbols:
            continue
        else:
            unique_symbols.append(symbol)
    unique_symbols.sort()
    return unique_symbols


# getting stacked symbols from reel
def get_stacked(symbols):
    stacked_symbols = []

    modified_symbols = symbols
    # adding n[0] and n[1] elements to the end of list
    for i in range(0, 2):
        modified_symbols.append(symbols[i])

    # Checking if n[i], n[i+1], n[i+2] are the same symbols
    for index, symbol in enumerate(modified_symbols):
        # Iterating till [n-2] element
        if index < (modified_symbols.__len__()-2):
            if (symbol == modified_symbols[index+1]) and (symbol == modified_symbols[index+2]):
                if not (stacked_symbols.__contains__(symbol)):
                    stacked_symbols.append(symbol)

    stacked_symbols.sort()
    return stacked_symbols


# Function for printing an issue
def throw_warning(symbol, issue_type):
    print("\t\tWARNING - SYMBOL '{}' {}".format(symbol, issue_type))


def check_unique_symbols(r_unique, d_unique):
    if not (r_unique == d_unique):
        for symbol in r_unique:
            if not (d_unique.__contains__(symbol)):
                throw_warning(symbol, "IS ABSENT ON A DISPLAY REEL")


def check_extra_display_symbols(r_unique, d_unique):
    if not (r_unique == d_unique):
        for symbol in d_unique:
            if not (r_unique.__contains__(symbol)):
                throw_warning(symbol, "IS EXTRA AS IT DOESN'T PRESENT ON REAL REEL")


def check_stacked_symbols(r_reel_stack, d_reel_stack):
    if not (r_reel_stack == d_reel_stack):
        for symbol in r_reel_stack:
            if not (d_reel_stack.__contains__(symbol)):
                throw_warning(symbol, "DOESN'T STACKED ON A DISPLAY REEL")


def check_extra_stacked_symbols(r_reel_stack, d_reel_stack):
    if not (r_reel_stack == d_reel_stack):
        for symbol in d_reel_stack:
            if not (r_reel_stack.__contains__(symbol)):
                throw_warning(symbol, "HAS EXTRA STACK AS IT DOESN'T PRESENT ON REAL REEL")


# starts set of checks
def check_display_reel(r_reel, d_reel):
    try:
        r_unique = get_unique(r_reel)
        d_unique = get_unique(d_reel)
        r_stacked = get_stacked(r_reel)
        d_stacked = get_stacked(d_reel)
        check_unique_symbols(r_unique, d_unique)
        check_extra_display_symbols(r_unique, d_unique)
        check_stacked_symbols(r_stacked, d_stacked)
        check_extra_stacked_symbols(r_stacked, d_stacked)
    except (IndexError, TypeError):
        print("Oops... Something really went wrong...")


# starts set of checks for each founded reel set
def start_reels_check(reels_set, display_reels_set):
    for index, reel in enumerate(reels_set):
        print("Checking set: "+str(index))
        for symbol_set_index, symbol_set in enumerate(reel.symbols):
            print("\tChecking reel: "+str(symbol_set_index))
            check_display_reel(symbol_set, display_reels_set[index].symbols[symbol_set_index])
        print(50*"-")


# scanning of folder for *.xml files
def get_xml_files():
    files = []

    path = sys.argv[1]
    for file in os.listdir(path):
        if file.endswith(".xml"):
            if not (str(path).endswith("\\")):
                path = path+"\\"
            files.append(path+file)
    return files


# parsing *.xml file (getting reel_sets)
def extract_from_xml(xml_file, reels_type):
    all_reels = []

    #    getting root of xml (<config...>)
    config = ET.parse(xml_file).getroot()
    #    <reels_set>
    reels_set = config.find(reels_type)
    if reels_set_tag == "reels_set":
        for set in reels_set:
            symbols = []
            set_id = set.get("id")
            for reel in set:
                reel_symbols = reel.get('symbols')

                # handler for situations <reel i="2" reel="1" type="copy"/>
                if reel_symbols is None and reel.get('type') == 'copy':
                    reel_symbols = symbols[int(reel.get('reel'))]
                    symbols.append(reel_symbols)
                    continue

                symbols.append(list(map(int, reel.get('symbols').split(','))))
                # print(reel.get("symbols"))
            all_reels.append(Reel(set_id, symbols))

    else:
        symbols = []
        set_id = 0
        for reel in reels_set:
            symbols.append(list(map(int, reel.get('symbols').split(','))))
            # print(reel.get("symbols"))
        all_reels.append(Reel(set_id, symbols))

    return all_reels


reels_set_tag = 'reels_set'
display_reels_set_tag = 'display_reels_set'
#reels_set_tag = 'reels'
#display_reels_set_tag = 'display_reels'

# variables for storing sets of real and display reels
reels_set = []
display_reels_set = []


# variable for storing list of found xml files
xml_files = get_xml_files()

# processing by each found xml-config
for xml_file in xml_files:
    print("Processing "+str(xml_file)+"...\n")
    #   reels_set = 'reels_set' or 'reels'
    reels_set = extract_from_xml(xml_file, reels_set_tag)
    #   display_reels_set = 'display_reels_set' or 'display_reels'
    display_reels_set = extract_from_xml(xml_file, display_reels_set_tag)
    start_reels_check(reels_set, display_reels_set)
    print("\n"+50*" * "+"\n")
