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
excerpt: 常用的linux指令和vim指令

---
[notice]记录常用的linux指令和vim指令[/notice]

## Linux
```shell
pwd     # Find out the path of the current working directory
cd -    # Move to your previous directory
ls -R   # List all the files in sub-directories as well
ls -a   # Show the hidden files
ls -al  # List add detailed information
cp -r /(from) /(dest) 
mv -r /(from) /(dest) 
rm -rf # 删库跑路
grep -r “fdfdsaf” lib/*/*prx   # Find patterns in followed location
diff f1.v f2.v # Find differences between two files
jobs    # List your background processes
kill %n # Kill a process by ID
```

## Vim

# Substitute first work     :s/foo/bar/

# Substitute first line     :s/foo/bar/g

# Substitute all        :%s/foo/bar/g

# Substitute all but ask for confirmation       :%s/foo/bar/gc

# Split     :split  :vsplit (ctrl+w followed by arrow key to switch) :e /location(Open a file)

# Find patterns in a directory      grep “fdfdsaf” lib/*/*prx

# Edit the configurable file  :e $MYVIMRC