import json
from tkinter import *
from tkinter import ttk, filedialog


def add_data(data_add):
    pass

def update_data():
    pass

data = list()
user_inteface = dict()
with open("data.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)
    user_inteface.update(json_data[0])
    data.extend(json_data[1])


WIDTHW, HEIGHTW, XW, YW = 500, 500, 100, 50
if __name__ == "__main__":
    root = Tk()
    root.title(user_inteface["app_name"])
    root.geometry(f"{WIDTHW}x{HEIGHTW}+{XW}+{YW}")
    root.minsize(300, 200)
    
    root.columnconfigure(0,weight=3)
    root.columnconfigure(1,weight=1)
    root.rowconfigure(4,weight=6)
        
    #row0
    ttk.Label(text="Parameters:").grid(column=0, row=0, sticky=EW, padx=5, pady=2)

    object_parameters_combobox = ttk.Combobox(root, values=data[0]["object_properties"], state="readonly")
    object_parameters_combobox.current(0)
    object_parameters_combobox.grid(column=0, row=1, sticky=EW, padx=5, pady=2)

    object_variable_entry = ttk.Entry(root)
    object_variable_entry.grid(column=0, row=2, sticky=EW, padx=5, pady=2)

    def search_data():
        pass
    ttk.Button(root, text="Search", command=search_data).grid(column=0, row=3, sticky=EW, padx=5, pady=2)

    #row1
    def clear_one_property():
        pass
    ttk.Button(root, text=" Clear this\nparameter", command=search_data).grid(column=1, row=1, rowspan=2, sticky=EW, padx=5, pady=2)

    def clear_search():
        pass
    ttk.Button(root, text="Clear all parameters", command=search_data).grid(column=1, row=3, sticky=EW, padx=5, pady=2)

    #table
    count_columns = []
    for i in range(len(data[0]["object_properties"])+1):
        count_columns.append(i)
    object_table = ttk.Treeview(root, columns=count_columns, show="headings")
    for i in range(len(count_columns)):
        if i == 0:
            object_table.heading(0, text="name")
            object_table.column(0, width=50)
        else:
            object_table.heading(i, text=data[0]["object_properties"][i-1])
            object_table.column(i, width=50)
    object_table.grid(column=0,columnspan=2, row=4, sticky=NSEW, padx=5, pady=2)

    root.mainloop()