# Week 02 — Linux Fundamentals

## Overview

During this week I studied the fundamentals of Linux and learned how to work efficiently with the terminal. The focus was on navigating the filesystem, managing files and directories, inspecting processes, searching data, handling permissions, and using essential Linux commands.

---

## Topics

### Filesystem Navigation

* pwd
* ls
* cd

### File & Directory Management

* mkdir
* touch
* cp
* mv
* rm
* rmdir

### Viewing Files

* cat
* less
* head
* tail

### Searching & Text Processing

* find
* grep
* sort
* uniq
* wc
* cut

### Input / Output Redirection

*

>

1.

> >

1. 2>
2. 2>&1
3. |

### Process Management

* ps
* pgrep
* kill
* pkill

### System Information

* free
* df
* du
* lsblk
* id
* whoami

### File Permissions

* chmod
* chown

### Archiving

* tar

### Services

* systemctl
* journalctl

---

## Practical Skills

* Navigate the Linux filesystem
* Create, copy, move, and delete files
* Read and inspect file contents
* Search files and filter text
* Redirect command output and errors
* Monitor and manage running processes
* Check memory, storage, and disk usage
* Change file permissions and ownership
* Create and extract archives
* Manage Linux services

---

## Commands Learned

| Category Commands |                                             |
| ----------------- | ------------------------------------------- |
| Navigation        | `pwd`, `ls`, `cd`                           |
| Files             | `mkdir`, `touch`, `cp`, `mv`, `rm`, `rmdir` |
| Viewing           | `cat`, `less`, `head`, `tail`               |
| Search            | `find`, `grep`                              |
| Text Processing   | `sort`, `uniq`, `wc`, `cut`                 |
| Processes         | `ps`, `pgrep`, `kill`, `pkill`              |
| System            | `free`, `df`, `du`, `lsblk`, `id`, `whoami` |
| Permissions       | `chmod`, `chown`                            |
| Archives          | `tar`                                       |
| Services          | `systemctl`, `journalctl`                   |
| Redirection       | `>`, `>>`, `2>`, `2>&1`, `                  |

---

## Outcome

By the end of this week I became comfortable using the Linux terminal for everyday tasks. I can navigate the filesystem, manage files and processes, inspect system resources, search and manipulate data, work with permissions, and use core command-line utilities confidently.Week 02 — Linux Fundamentals

## Overview

During this week I studied Linux fundamentals and practiced working with the command line.

The focus was on understanding the Linux filesystem, managing files and directories, searching and processing text, working with processes and services, handling permissions, and combining commands through shell pipelines and redirection.

---

## Topics

### Linux Filesystem

Studied the purpose of common Linux directories:

```text
/
├── /home
├── /root
├── /etc
├── /var
├── /var/log
├── /tmp
├── /usr
├── /opt
├── /dev
├── /proc
└── /sys
```

Learned the general purpose of these directories and how they fit into the Linux filesystem hierarchy.

### File and Directory Management

Practiced:

* `cp`
* `mv`
* `rm`
* `mkdir`
* `touch`

### Viewing and Inspecting Files

* `cat`
* `less`
* `head`
* `tail`

### Searching and Text Processing

* `find`
* `grep`
* `sort`
* `uniq`
* `cut`
* `wc`
* `tee`
* `xargs`

### Shell Pipelines and Redirection

Studied how command input and output can be combined and redirected:

```text
|
>
>>
2>
2>&1
/dev/null
&&
||
```

Practiced building pipelines from multiple commands and redirecting standard output and errors.

---

## File Permissions

Studied the Linux permission model:

* User
* Group
* Other
* Read (`r`)
* Write (`w`)
* Execute (`x`)

Practiced:

* `chmod`
* `chown`
* `id`
* `groups`
* `umask`
* `sudo`

The goal was to understand how Linux controls access to files and directories.

---

## Processes and Services

Studied how Linux manages running processes and services.

### Processes

* `ps`
* `pgrep`
* `kill`

### Services and System Information

* `systemctl`
* `journalctl`
* `dmesg`

Practiced finding processes, checking their state, stopping processes, inspecting services, and reading system logs.

---

## Practical Work

During this week I practiced:

* navigating the Linux filesystem;
* finding files;
* searching for text inside files;
* inspecting file contents;
* finding running processes;
* stopping processes;
* checking services and their logs;
* changing file permissions;
* working with ownership;
* building command pipelines;
* redirecting command output and errors.

---

## Commands Learned

| Category        | Commands                                          |
| --------------- | ------------------------------------------------- |
| Navigation      | `cd`, `ls`, `pwd`                                 |
| Files           | `cp`, `mv`, `rm`, `mkdir`, `touch`                |
| Viewing         | `cat`, `less`, `head`, `tail`                     |
| Search          | `find`, `grep`                                    |
| Text Processing | `sort`, `uniq`, `cut`, `wc`, `tee`, `xargs`       |
| Processes       | `ps`, `pgrep`, `kill`                             |
| Permissions     | `chmod`, `chown`, `id`, `groups`, `umask`, `sudo` |
| Services        | `systemctl`, `journalctl`, `dmesg`                |

---

## What I Can Explain

By the end of this week I can explain:

* the purpose of the main Linux filesystem directories;
* how to navigate and work with files from the terminal;
* how to search for files and text;
* how pipelines work;
* how standard output and errors can be redirected;
* how Linux permissions are divided between user, group, and other;
* what `r`, `w`, and `x` permissions mean;
* how to inspect and manage processes;
* how to inspect services and their logs;
* how basic Linux command-line tools can be combined to perform practical tasks.

---

## Summary

This week focused on becoming comfortable with the Linux command line and understanding the basic mechanisms used to work with files, permissions, processes, services, and system information.

The practical work provided the foundation needed for later networking, scripting, and security tasks.

---

## Status

**DONE**
