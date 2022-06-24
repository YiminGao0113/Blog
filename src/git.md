---
layout: post
title: Git Command
slug: git
date: 2022-06-24 18:51
status: publish
author: Yimin
categories: 
  - cheatsheet
tags: 
  - git
excerpt: 常用的git指令
---


[notice]记录一些常用的git指令[/notice]

## Clone
Clone a remote repo to local
```
$ git clone <url>
```
Clone a specific branch
```
$ git clone <url> -b AIRISCPiM  - -single-branch <url> 
```

## Branch
Show current branch
```
$ git branch
```
Switch to another branch
```
$ git checkout 
```

## Stage files
Stage all the files
```
$ git add . 
```
Add only C files
```
$ git add *.c 
```
Add specific files
```
$ git add fortz.c diff.py 
```

## Unstage 
Discard uncommitted local changes in the local branch. (Want to redo after git add)
```
$ git restore --stage <file>
```

## Commit
Commit the changes
```
$ git commit -m "First Commit" 
```

## Reset
Remove git commit but keep the change, AIRISCPiM is the branch name, ~11 is how many commits to remove
```
$ git reset --soft AIRISCPiM~11 
```
Untrack a specific file
```
$ git reset <file>
```

## Push to Remote
Push to a branch(AIRISCPiM) from local repo(origin)
```
$ git push -u origin AIRISCPiM 
```
When you are on the right branch just do git push
```
$ git push 
```

## Fetch and update
Fetch and download content from a remote repo and update local repo
```
$ git pull 
```

## Display Status
Displays the state of the working directory and the staging area
```
$ git status 
```
