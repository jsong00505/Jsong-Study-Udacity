# Creating and modifying a repository

I just lost my work, and below is all of I remembered this time.

`git diff`
`git diff -staged`

## Branches

label called `Branch`

* master : main branch
* exp: experimental feature
* italian: Italian version

## Making a Branch

git branch
git branch `branch name`
	ex) git branch easy-mode

git checkout easy-mode

## Branches for Collaboration

git log --graph --oneline `branch name1` `branch name2`
	ex) git log --graph --oneline master coin