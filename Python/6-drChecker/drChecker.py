import os

import xml.etree.ElementTree as ET

class Reel:
    def __init__(self, id, symbols):
        self.id = id
        self.symbols = symbols

    def printMe(self):
        print(str(self.id)+"\n"+str(self.symbols))

    def get_symbol_set(self,symbol_set_id):
        return self.symbols[symbol_set_id]

def get_unique(symbols):
    unique_symbols = []
    for symbol in symbols:
        if symbol in unique_symbols:
            continue
        else:
            unique_symbols.append(symbol)
    unique_symbols.sort()
    return unique_symbols


def get_stacked(symbols):
    stacked_symbols = []

    border_symbols = [symbols[symbols.__len__()-3],
                      symbols[symbols.__len__()-2],
                      symbols[symbols.__len__()-1],
                      symbols[0]]

    for index, symbol in enumerate(symbols):
        if index < (symbols.__len__() - 3):
            if (symbol == symbols[index + 1]) and (symbol == symbols[index + 2]):
                if not(stacked_symbols.__contains__(symbol)):
                    stacked_symbols.append(symbol)

    for symbol in border_symbols:
        if (border_symbols.count(symbol)) > 2:
            if not (stacked_symbols.__contains__(symbol)):
                stacked_symbols.append(symbol)
            break
    stacked_symbols.sort()
    return stacked_symbols


def check_unique_symbols(r_unique, d_unique):
    if not(r_unique == d_unique):
        for symbol in r_unique:
            if not(d_unique.__contains__(symbol)):
                print("\t\t!!! WARNING !!! SYMBOL " + symbol.__str__() + " DOESN'T PRESENT ON DISPLAY REEL!")


def check_extra_display_symbols(r_unique, d_unique):
    if not(r_unique == d_unique):
        for symbol in d_unique:
            if not(r_unique.__contains__(symbol)):
                print("\t\t!!! WARNING !!! SYMBOL " + symbol.__str__() + " IS EXTRA AS IT DOESN'T PRESENT ON REAL REEL!")


def check_stacked_symbols(r_reel_stack, d_reel_stack):
    if not(r_reel_stack == d_reel_stack):
       for symbol in r_reel_stack:
            if not(d_reel_stack.__contains__(symbol)):
                print("\t\t!!! WARNING !!! STACK OF " + symbol.__str__() + " DOESN'T PRESENT ON DISPLAY REEL!")


def check_extra_stacked_symbols(r_reel_stack, d_reel_stack):
    if not(r_reel_stack == d_reel_stack):
        for symbol in d_reel_stack:
            if not(r_reel_stack.__contains__(symbol)):
                print("\t\t!!! WARNING !!! STACK OF " + symbol.__str__() + " IS EXTRA AS IT DOESN'T PRESENT ON REAL REEL!")


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
        print("Oops... check if reels' value properly pasted...")


def start_reels_check(reels_set, display_reels_set):
    for index, reel in enumerate(reels_set):
        print ("Checking set: "+str(index))
        for symbol_set_index, symbol_set in enumerate(reel.symbols):
            print ("\tChecking reel: "+str(symbol_set_index))
            check_display_reel(symbol_set, display_reels_set[index].symbols[symbol_set_index])
        print(50*"-")

def get_xml_files():
    files = []

    for file in os.listdir():
        if file.endswith(".xml"):
            files.append(file)
    print("")
    return files

#reels type = 'reels_set' or 'display_reels_set' //TODO: in config can be tag 'reels'


def extract_from_xml(xml_file,reels_type):
    all_reels = []
#    getting root of xml (<config...>)
    config = ET.parse(xml_file).getroot()
#    <reels_set>
    reels_set = config.find(reels_type)
    for set in reels_set:
        symbols = []
        set_id = set.get("id")
        for reel_symbols in set:
            symbols.append(list(map(int, reel_symbols.get('symbols').split(','))))
            #print(reel_symbols.get("symbols"))
        all_reels.append(Reel(set_id, symbols))
    return all_reels

reels_set = []
display_reels_set = []
xml_files = get_xml_files()

#for with counter by sets in real reels. next for - compare indexed reels

for xml_file in xml_files:
    print("Processing "+str(xml_file)+"...\n" )
    reels_set = extract_from_xml(xml_file, 'reels_set')
    display_reels_set = extract_from_xml(xml_file, 'display_reels_set')
    start_reels_check(reels_set, display_reels_set)



