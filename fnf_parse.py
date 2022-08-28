import json
import os
import random
import time

data_to_parse = {
    1: "song",
    2: "player1",
    3: "player2",
    4: "speed",
    5: "bpm",
    6: "validScore",
    7: "needsVoices",
    8: "notes",
    9: "sections",
    10: "sectionLengths"
}

note_obtain_data = {
    1: "lengthInSteps",
    2: "bpm",
    3: "changeBPM",
    4: "mustHitSection",
    5: "sectionNotes",
    6: "typeOfSection",
    7: "altAnim"
}

def FNF_AddCustom(parse_list, value):
    if(parse_list == 1):
        data_to_parse[len(data_to_parse) + 1] = value
    elif(parse_list == 2):
        note_obtain_data[len(note_obtain_data) + 1] = value
    else:
        print("Something occured.")


def FNF_ParseData(chart_path, parse_element):
    f = open(chart_path)
    data = json.load(f)
    song = data["song"]
    return song[data_to_parse.get(parse_element, "Invalid Option.")]
    

def FNF_ParseSections(sec_data, sec_index):
    sec = sec_data
    if sec_index <= len(sec):
        return sec[sec_index]
    else:
        print("ERROR!")

def FNF_ParseSectionData(cur_section, parse_element):
    section = cur_section
    return section[note_obtain_data.get(parse_element, "Invalid Option.")]

def FNF_ParseNotes(sec_notes, note_index):
    section_notes = sec_notes
    if note_index <= len(section_notes):
        return section_notes[note_index]
    else:
        print("ERROR!")
    


