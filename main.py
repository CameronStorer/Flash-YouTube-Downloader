import fileManagement
import ytDownloader
import tkinter as Tk

def start():
    # collect user input
    save_to_file()
    # retrieve desired url's
    urls = ytDownloader.collectUrls()
    # do the operation on said url's
    ytDownloader.theOperation(urls)
    # move the downloaded files
    fileManagement.organizeFiles()
    # change the file type from webm to mp3
    fileManagement.changeFileType()
    return

def save_to_file():
    user_input = urlInputBox.get("1.0", Tk.END)  # Get text from Text widget
    if (user_input != "\n"):
        try:
            with open("desiredURLS.txt", "w") as file:  # Open file in write mode ("w")
                file.write(user_input)  # Write the text to the file
            status_label.config(text="Text saved to user_input.txt") #update status label
        except Exception as e:
            status_label.config(text=f"Error saving: {e}") #update status label with error message


# some basic window attributes for looks
root = Tk.Tk()
root.geometry("1000x500")
root.title("YT2MP3 Converter")

# names of labels and buttons
labelNames = {"Output Directory", "Paste URLS here. Separate by commas"}
buttonNames = {"Start Process"}

# IMPORTANT RULE LEARNED: DO NOT ATTEMPT TO
# PACK ITEMS ON THE SAME LINE AS DEFINING THEM

# create some frames
frame1 = Tk.Frame(root, height=100, width= 100, bg = "dark grey")
frame1.pack(pady=20, padx=20, side="left")

frame2 = Tk.Frame(root, height=100, width= 100, bg = "grey")
frame2.pack(pady=5, padx=5, side="right")

for button in buttonNames:
    tempButton = Tk.Button(frame1, text = button, fg = "blue", bg = "white", command=start)
    tempButton.pack(fill="x", side="top", pady= 3)

for label in labelNames:
    tempLabel = Tk.Label(frame2, text= label, fg = "blue", bg = "white" )
    tempLabel.pack(fill="x", side="top", pady= 3)


urlInputBox = Tk.Text(frame2, height=200, width=200)
urlInputBox.pack()

status_label = Tk.Label(root, text="") #status Label
status_label.pack()

root.mainloop()

