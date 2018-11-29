I contributed to several apspects of this project. More specifically, I fixed the voting page to never 
display a user their own pet(because the user will just vote for their own pet), and added 
voting functionality, so now users can vote for pets. I also improved the person detailed page, to now
include a user's pets and their total profile votes. I also removed pet model field PID, on Brandon's suggestion. 

I also rewrote the init.py script to now account for users being linked to persons. The old script only made persons and
signed pets to them randomly. The new script makes users, (and thus makes persons, since person is an extension of user)
and assigns pets to each user's person. The new script also allows creates a moderators group, gives permissions to said group, and adds Admin user to moderator group. A small quality of life fix implemented in the new init script is the matching of
pictures to species. Originally species were given at random, regardless of picture. Now species given matches the picture,
so now a picture of a cat won't have a species listed as "dog" for example. 

Finally, I also provided some technical assistance with Git, answered some team member's questions regarding git, and also
debugged/fixed the remote repo after a site-breaking commit was pushed (twice). To see what I specfically did, please check the 
repository commits. It's worth noting that one commit I made was actualy Patrick's edits (I believe I credited him in the commit 
message), I ended up commiting his changes because the remote repo was having some problems with his commit. 
