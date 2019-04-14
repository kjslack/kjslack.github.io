#!/usr/bin/env python
import pyperclip
import future


def GetTime(text_header):
    print(text_header)
    hours = input("Hours: ")
    minutes = input("Minutes: ")
    seconds = input("Seconds: ")
    total_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
    print(total_seconds)
    return total_seconds

url = input("Youtube Video URL = ")

while True:    
    start_time = GetTime("Start Time");
    end_time = GetTime("End Time");
    
    html_embed_code = '<iframe width="300" height="169" src="' + url + '?rel=0&amp;start=' + str(start_time) + ';end=' + str(end_time) + '" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>'
    pyperclip.copy(html_embed_code)
    print(html_embed_code)
    print('\n\n')
