"""
TKINTER LABELFRAME

\\\\\\\\\\\\\\\\\\\\\

Specify the label position

- To specify the position of the label on the widget, you use the labelanchor option. The labelanchor defaults to 'nw', which places the label at the left end of the top border: pic-1

- The following program illustrates the label anchor options. When you select a label option, the label of the LabelFrame widget change accordingly: pic-2

"""

#

import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.title("LabelFrame Label Anchor")


# label frame
lf = ttk.LabelFrame(root, text="Label Anchor")
lf.grid(column=0, row=0, padx=20, pady=20, sticky=tk.NSEW)


anchor_var = tk.StringVar()
anchors = {
    "nw": {"row": 0, "column": 1},
    "n": {"row": 0, "column": 2},
    "ne": {"row": 0, "column": 3},
    "en": {"row": 1, "column": 4},
    "e": {"row": 2, "column": 4},
    "es": {"row": 3, "column": 4},
    "se": {"row": 4, "column": 3},
    "s": {"row": 4, "column": 2},
    "sw": {"row": 4, "column": 1},
    "ws": {"row": 3, "column": 0},
    "w": {"row": 2, "column": 0},
    "wn": {"row": 1, "column": 0},
}


def change_label_anchor():
    lf["labelanchor"] = anchor_var.get()


# create radio buttons and place them on the label frame
for key, value in anchors.items():
    # create a radio button
    radio = ttk.Radiobutton(
        lf,
        text=key.upper(),
        value=key,
        command=change_label_anchor,
        variable=anchor_var,
    ).grid(**value, padx=10, pady=10, sticky=tk.NSEW)


# set the radio button selected
anchor_var.set(lf["labelanchor"])


root.mainloop()
