# Till yet we have done is 

#         To revert any changes we made locally in working space ie before stagging the changes and committing it. 

#         To revert any commit and reach to a certain specific previous commit. 

# Now here we will revert any push request, if it is done.

# Here we reach to a commit level code ie again this request also is associated with a commit id. 


# Here we commit as well as push the final code ie the version of code associated with commit id. 

# Here we need to be carefull as it is irreversible. 

# This command is used, if in case we have multiple versions of code, we have reached somehow to 6th version of a code, 
#         but soon we realise that it is fine to keep this code at 4th level commit. 

#         All the code after 4th commit is useless, so in this case we will use reset command to reach at the 4th commit state. 

#         Here we will not use revert command as we are sure that we want to erase all the code versions after 4th commit, 
#                 we dont need to keep whole version of code after 4th commit. 

                
# git reset --hard 'commit-id' 

# We will get commit-id from 'git log' command. 