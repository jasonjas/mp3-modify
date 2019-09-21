from mutagen.easyid3 import EasyID3
import pathlib
from os import path, rename
import tkinter as tk
from tkinter import filedialog
import re

def main():
    # ask for location of file(s)
    root = tk.Tk()
    root.withdraw()
    # open individual file
    # file_path = filedialog.askopenfilename()
    # open multiple files
    file_path = filedialog.askopenfiles(filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
    root.destroy()
    get_files(file_path)


def get_files(item_path):
    modify_mp3_file(item_path)

def rename_file(file, newname):
    rename(file, newname)


def modify_mp3_file(files):
    # check if mp3 extension
    for f in files:
        file = f.name
        if file.endswith('.mp3'):
            if '-' in file:
                print('Processing file: ' + file)
                # artist = path.basename(file).split('-', 1)[0]
                artist = path.basename(file).rsplit('-', 1)[0]
                dirpath = pathlib.Path(file).parent
                newfilename = re.sub('^' + artist + '-', '', path.basename(file))
                newpath = str(dirpath) + '\\' + newfilename
                title = str(path.splitext(newfilename)[0])
                audio = EasyID3(file)
                audio['artist'] = artist
                audio['albumartist'] = artist
                audio['title'] = title
                # audio['album'] = u"My album"
                # audio['composer'] = u""  # clear
                audio.save(v2_version=3)
                # close open file
                f.close()
                rename(file, newpath)
            else:
                print('hyphen (-) not in file name for ' + file)
        else:
            print(file + ' is not an MP3 file')


if __name__ == '__main__':
    main()
