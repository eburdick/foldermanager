#!/usr/bin/python3
"""

This program is a tool for manipulating file system directories and files, doing things normally
not found in file manager applications. There are two main components of this process...

Selection of files/directories to act on based on one or more of these...
 file extension
 parts of the file name
 file dates (create, modify, etc)
 file metadata (image files)
 file size, directory file count or total file size
 file sorting like all files starting with a-l, m-s, t-z
 ...more, tbd...

Move these files to a different directory, sometimes deleting the source directory or creating new
directories. Examples...
 remove current directory and pull files into the directory containing it, or replace it with
   new ones as described below.
 create a new directory for the selected files, either below the source directory, parallel to it,
   or somewhere else.
 create new directories as above depending on multiple selection criteria. For example, one directory
   for each file type, one directory for files having names matching a pattern, or multiple directories
   for each of multiple patterns.

Additional functionality...
 save an operation so it can be repeated on other parts of the directory tree. Maybe this takes the
   form of small scripts that can be run on selected directories.

 User interface notes...

Tkinter provides a modal popup file selection dialog, but I have so far not been able to find
a file browser widget that I can just put in a frame in my main window. The popup is robust has good
OS integration, so it seems wise to use it, but I originally envisioned a GUI that has two permanent
file displays so I can highlight files based on selection criteria. So how would a UI based on the
popup file dialog look? My first thought is that we use the file dialog for the following things...
  navigate to the initial directory we want to work on
  select files and directories
Our main working window needs to have a dialog for setting up filters, a list of files with an
indication of whether they match filter patterns, etc. Using an existing file browser might not
be a good way to do this, so list boxes, tree displays, etc, might be the way to go anyway. Some
basic navigation would be good as part of this, like moving up and down the tree, but being able
to pop up a file browser when needed would be handy and avoid the necessity of duplicating that
functionality.

Information we need to display to the user:
- The files we want to work on, including some kind of highlighting to mark files to be moved, and
  maybe the ability to select and deselect some.
- Preview of what is going to happen, maybe as simple as text or icons per selected item.


"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

root = tk.Tk()
root.wm_title("Folder Mgr")

style = ttk.Style(root)
style.theme_use("winnative")


def c_open_file():
    rep = filedialog.askopenfilenames(parent=root, initialdir='/', initialfile='tmp',
                                      filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("All files", "*")])
    print(rep)


def c_open_dir():
    rep = filedialog.askdirectory(parent=root, initialdir='/')
    print(rep)


def c_save():
    rep = filedialog.asksaveasfilename(parent=root, defaultextension=".png", initialdir='/tmp', initialfile='image.png',
                                       filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("All files", "*")])
    print(rep)


ttk.Label(root, text='Default dialogs').grid(row=0, column=0, padx=4, pady=4, sticky='ew')
ttk.Button(root, text="Open files", command=c_open_file).grid(row=1, column=0, padx=4, pady=4, sticky='ew')
ttk.Button(root, text="Open folder", command=c_open_dir).grid(row=2, column=0, padx=4, pady=4, sticky='ew')
ttk.Button(root, text="Save file", command=c_save).grid(row=3, column=0, padx=4, pady=4, sticky='ew')

root.mainloop()
