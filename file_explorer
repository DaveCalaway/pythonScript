from tkinter import filedialog,Tk

# global variables
serial_file_name = ""

# File exlorer for the path
def file_explorer():
    
    # browseFiles
    def browseFiles(): 
        global serial_file_name
        tk.file_path = filedialog.askopenfilename(initialdir = "/", 
                                    title = "Select a File", 
                                    filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        if len(tk.file_path) > 1:
            # print("preso")
            serial_file_name = tk.file_path
            window.destroy()

    # unique window
    window = tk.Tk() 
    window.geometry("500x200")      
    window.grid_columnconfigure(0, weight=1)

    # welcome label
    welcome_label = tk.Label(window,
                            text="Welcome to the txt to csv for Hybrid!\nGive the log file:",
                            font=("Helvetica", 15))
    welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10) 

    button_explore = tk.Button(window,  
                            text = "Browse Files", 
                            command = browseFiles) 
    button_explore.grid(column = 0, row = 2) 

    button_exit = tk.Button(window,  
                        text = "Exit", 
                        command = exit)
    button_exit.grid(column = 0,row = 3)

    window.mainloop() 
    

# ---- MAIN ----#
file_explorer()
print("The file selected from explorer is: " + serial_file_name )
