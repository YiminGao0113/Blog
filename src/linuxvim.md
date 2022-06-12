---
layout: post
title: Linux and vim cheatsheet
slug: linux&vim
date: 2022-06-11 23:27
status: publish
author: Yimin
categories: 
  - Cheatsheet
tags: 
  - Linux
  - Vim
excerpt: 常用的linux指令和Vim指令

---
[notice]记录常用的linux指令和Vim指令[/notice]

## Linux
```shell
pwd     # Find out the path of the current working directory
cd -    # Move to your previous directory
ls -R   # List all the files in sub-directories as well
ls -a   # Show the hidden files
ls -al  # List add detailed information
cp -r /from /dest
mv -r /from /dest
rm -rf # 删库跑路(无法撤回)
grep -r “fdfdsaf” lib/*/*prx   # Find patterns in followed location
diff f1.v f2.v # Find differences between two files
jobs    # List your background processes
kill %n # Kill a process by ID
```

## Vim

```shell
:s/foo/bar/       # Substitute first work     
:s/foo/bar/g      # Substitute first line
:%s/foo/bar/g     # Substitute all
:%s/foo/bar/gc    # Substitute all but ask for confirmation
:split            # Split the screen
:vsplit           # (ctrl+w followed by arrow key to switch)
:e /location      # Open a file
grep "" /         # Find patterns in a directory      
:e $MYVIMRC       # Edit the configurable file
```
