# In previous example we have seen how revert changes if we havnt made add and commit request. 

# In this example we will see how to revert changes if we have committed the changes. 

# Here we will use revert command for our case. 

# Revert can be used for reverting multiple changes as well as for single change.


# Step a: 
#       First we need to find commit id to revert specific commit as commit id will uniquely identify the commit we want to revert
#       To find commit id we need to use command given below - 
            # git log
#       Now we will copy specific commit id. 

        # eg -
        # git log 
        # Git log interface will end after ':q' input

        # git log output

                # Author: rythmstories <gauravgupta1051996@gmail.com>
                # Date:   Mon Jan 18 19:18:18 2021 +0530

                #     add commit git complete

                # commit 3960f3b56458187e3ad61983f571f587cd100e0f
                # Author: rythmstories <gauravgupta1051996@gmail.com>
                # Date:   Mon Jan 18 18:39:51 2021 +0530

                #     create a git repo complete

                # commit 7c2f06ad505e1d8733d7e3622a9930e05ed12f7d
                # Author: rythmstories <gauravgupta1051996@gmail.com>
                # Date:   Mon Jan 18 18:21:20 2021 +0530

                #     clone complete

                # commit a8a2711cc17024e73c87ef6539a98e6053ef60b0

                # :q

#       Here we will copy commit id for the specific commit we want to undo eg I want undo 'GIT COMPLETE' commit - 
                #     add commit git complete

                # commit 3960f3b56458187e3ad61983f571f587cd100e0f

                # commit id = 3960f3b56458187e3ad61983f571f587cd100e0f

#       Now we will enter this command to reach at 'GIT COMPLETE' commit -

                # git revert 'commit id'
                # git revert 3960f3b56458187e3ad61983f571f587cd100e0f

#       Now the initial code just before 'GIT COMPLETE' will be restore

#       I hope this will help
#