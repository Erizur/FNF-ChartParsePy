import fnf_parse
import time

class Main():
    valid_options = {
        1: "1"
    }
    def do_action(opt):
        if(opt == 1):
            print("now playing your chart!")
            for x in range(1, 10):
                print(fnf_parse.FNF_ParseData("charts/winter-horrorland.json", x))
            
            notes = fnf_parse.FNF_ParseData("charts/winter-horrorland.json", 8)
            i = 0
            for x in notes:
                sec_parse = fnf_parse.FNF_ParseSections(notes, i)
                print(sec_parse)
                i += 1
                print("line break")
    
    print("FNF CHART PARSER")
    print("Select an option:\n1.-Play song from charts folder")
    option = int(input("Choose an option: "))
    if str(option) != valid_options.get(option):
        print("bad!!!")
    else:
        do_action(1)

Main()