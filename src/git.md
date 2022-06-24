---
layout: post
title: Git Command
slug: git
date: 2022-06-24 18:51
status: publish
author: Yimin
categories: 
  - cheetsheet
tags: 
  - git
excerpt: Hello World!
---

---
[notice]记录常用的git指令[/notice]


```shell
$ git clone # Clone a repo to local
$ git clone -b AIRISCPiM  - -single-branch <url> # Clone a specific branch
$ git branch # Show current branch
$ git checkout # Switch to another branch
$ git add . # adds all changes in the working directory to the staging area
$ git add *.c # Add only C files
$ git add fortz.c diff.py # Add specific files
$ git restore --stage <file> # Unstage: Discard uncommitted local changes in the local branch. (Want to redo after git add)
$ git commit -m "First Commit" # Commit the changes
$ git reset --soft AIRISCPiM~11 # Remove git commit but keep the change, AIRISCPiM is the branch name, ~11 is how many commits to remove
$ git reset <file> # Untrack a specific file
$ git push -u origin AIRISCPiM # Push to a branch(AIRISCPiM) from local repo(origin)
$ git push # When you are on the right branch just do git push
$ git pull # Fetch and download content from a remote repo and update local repo
$ git status # Displays the state of the working directory and the staging area
```
