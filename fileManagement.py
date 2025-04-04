# organize the videos
import os
import shutil

def organizeFiles():
    while(True):

        try:
            # directory to search the files of
            sourcepath='.'
            # search the files of that directory
            sourcefiles = os.listdir(sourcepath)
            # if the files in parent directory are .mp4 files, move them into this path
            destinationpath = 'musicVideos'
            # check if every file is an .mp4
            for file in sourcefiles:
                if file.endswith('.webm'):
                    # if so, move them to the destination path
                    shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
            # uncomment to move downloaded video files to the "Video" directory
            """
            shutil.copytree( 
                            os.path.join('Working', 'musicVideos'),
                            os.path.join('Videos', 'musicVideos'),
                            dirs_exist_ok=True
                            )

            # remove the videos from the original location after moving them to the "Videos" directory
            shutil.rmtree(Working', 'musicVideos'))
            """
            break
        except:
            # if there is an error, attempt to create the directory and print error message
            os.makedirs('musicVideos',
                        exist_ok=True)
            print("ERROR: directory did not exist. Created!")

    # open the directory containing the resulting videos
    # os.startfile('C:\\users\\camer\\Videos\\musicVideos')

    #this command will be used (because the videos were not moved over to that directory)
    os.startfile('musicVideos')

def changeFileType():
    # directory to search the files of
    sourcepath='musicVideos'
    # search the files of that directory
    sourcefiles = os.listdir(sourcepath)
    # check if every file is an .webm
    for file in sourcefiles:
        old_filepath = os.path.join(sourcepath, file)  # Full path to original file
        new_filepath = os.path.join(sourcepath, file[:-5] + '.mp3') # Full path to new file
        try:
            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{file}' to '{file[:-5]}.mp3'")
        except FileNotFoundError:
            print(f"Error: File '{old_filepath}' not found.")
        except FileExistsError:
            print(f"Error: A file named '{file[:-5]}.mp3' already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")