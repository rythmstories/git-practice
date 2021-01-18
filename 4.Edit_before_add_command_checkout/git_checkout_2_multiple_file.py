# Till yet we have made new repository, added new files and new folders in the repository. 

# We have also edited various files and folders. And commited as well as pushed the chnages in the repository. 

# Now we will see in case of any unwanted commit or push, how can we undo the step easily. 

# Here we will discuss 'how we can undo the changes we have made before making add request ie beore moving changes from working area to staging area'. 

# Eg - 

# we have check folder - 


# Check 
#   |
#   -----file1.txt          (File)
#   |
#   -----file2.py           (File)
#   |
#   -----newway             (Folder)
#           |
#           -----file6.txt          (File)
#           |
#           -----file7.py           (File)
#   |
#   -----file3.py           (File)
#   |
#   -----file4.txt           (File)
#   |
#   -----README.md          (File)
#   |
#   -----.git               (Hidden File)




# We have edited multiple files. 

# But now we found that we have made certain error in the code and we want to undo these changes. 

# We can restore to previous version by this command - 

# git checkout -- .

# Remember - This command is helpful only and only, if add and commit commands are not made. 

