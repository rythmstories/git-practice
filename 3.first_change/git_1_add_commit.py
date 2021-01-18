# Now open your repository locally. 

# Now we can make any change we want to make eg adding any file, editing any code or text inside any file of the repository. 

# First step after editing the repository is to start the process to commit changes in the repository. 

# Step a: Go to the repository location in cmd (not at any file/folder location inside the repository).  
# Step b: Write the following command at cmd - 

# git add 'filename'   (To add the changes you have made in the specific file)

# git add --all         (To add all the changes in one step)


# Step c: After this, we need to commit the code by the following command at cmd - 

# git commit -m ""      (Here in inverted comma we need to write a short message about commit)



# Eg: Folder structure (Example repository name - Check)

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



# Suppose I have made changes in file4.py 

# Then I should commit by the following process - 

# git add file4.py
# git commit -m "updated file4"


# Another situation where we have made multiple changes in various files and folders of the repository, here we don't need to commit changes of every file individually. 
# In this condition we will simply write this command at cmd. 

# git add --all
# git commit -m "Updated repository"


# This is how we commit the changes in the Git repository.

print("git add 'filename'")
print("\n")
print('git commit -m ""')
print("\n")

# We are not done yet. 

# Till yet we have only commited the changes. Another step is to push the code in repository. 

# Till yet no changes would have been reflected in the repository. 

# Lets move to Push request in next file. 