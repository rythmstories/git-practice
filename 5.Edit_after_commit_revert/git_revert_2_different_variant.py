# In previous code we saw how we use 'revert' by the following command - 

# git revert 'commit-id'

print("GIT revert with committed code")
print("\n")

# Using this command we undo the latest commit and reach the level of the commit, whose commit id is mentioned in the command. 

# Here it changes takes place in 2 steps - 

#         a. First, we reach the level of the commit, whose commit id is mentioned
#         b. Now we commit the changes ie the final repository ie now all the changes that occurred because of the revert command will not exist in the working area or the stagging area. 
#            They will be committed to the repository. 


# We have an option of preventing code from commit ie changes will be reflected and will be present in the staging area. 

#         Here we need to commit the code/repository explicitly. 

#         We use this condition for checking the usability of code. 

#         Ie if we are on 6th version of certain code and we want to check whether 4th version of code works or not ie we 
#             just only want to check the code, we don't want to commit the code. In this case, this technique will be used. 

#         This technique is also used when we want to run 3rd or 4th version of code while being on the 6th version of code, 
#             we can use this technique and thus we will reach at the desired version of code, while not finalizing ie 
#             not committing the code. 

# Here is the command - 

# git revert -n 'git-id'

print("GIT revert without committed code")
print("\n")