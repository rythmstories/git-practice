# Till yet we have made new repository, added new files and new folders in the repository. 

# We have also edited various files and folders. And commited as well as pushed the chnages in the repository. 

# Now we will see in case of any unwanted commit or push, how can we undo the step easily. 

# Here we will discuss 'how we can undo the changes we have made before making add request ie beore moving changes from working area to staging area'. 

# Eg - 

# We have edited file.py file. 

# But now we found that we have made certain error in the code and we want to undo this. 





# Eg - 

# file.py (File)

# File content - 

# (old content)

# First line 
# second line 
# third line 
# fourth line 

# (New content after changes)

# First line 
# second line 
# third line 
# fourth line 
# First line post post
# second line  post post
# third line  post post
# fourth line  post post


# But now we want to undo the change as it should not be like that.

# We can restore to previous version by this command - 

# git checkout --file.py

# Remember - This command is helpful only and only, if add and commit commands are not made. 

# git checkout --file.py , will restore the file.py file into this - 


# (Old content before checkout command)

# First line 
# second line 
# third line 
# fourth line 
# First line post post
# second line  post post
# third line  post post
# fourth line  post post


# (new content after checkout command)

# First line 
# second line 
# third line 
# fourth line 

