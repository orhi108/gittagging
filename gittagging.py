#!/usr/bin/env python3.7
from git import Repo
from datetime import datetime
import sys

#declaring tags list
tags=[]

# if one argument is provided for tagname then it is added to the list 
if len(sys.argv) >= 2: 
	tags.append(sys.argv[1])

# adding to the list with tags formatted current date and time
now = datetime.now()
tags.append(now.strftime("%Y-%m-%d-%H-%M-%S"))

#creationg repo object for the repo in current directory 
try:
  repo = Repo('.')
except:
  print("Make sure that your current directory is a local git repo!")
  exit(1)
#gettin the name of current branch 
current_braanch=repo.head.reference.name

#if the current brunch is different than master then adding that branch name to the list with tags 
if current_braanch != "master":
	tags.append(current_braanch)

#creating all the git tags 
for tag in tags:
	try:
	  repo.create_tag(tag)
	  print("Tag with name [{}] has been creted successfully".format(tag))

	except:
	  print("Tag with name [{}] already exist. Recreation will be skipped".format(tag))
	 
#pushing newly created tags to the origin
origin = repo.remotes.origin
origin.push("--tags")
