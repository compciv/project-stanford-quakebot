# Creating a new folder and git and Github repo



<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Creating a new folder off of your home Desktop folder](#creating-a-new-folder-off-of-your-home-desktop-folder)
- [Creating and adding to files from the command-line](#creating-and-adding-to-files-from-the-command-line)
  - [Redirecting output stream from a command/program into a file](#redirecting-output-stream-from-a-commandprogram-into-a-file)
  - [Downloading files via `curl`](#downloading-files-via-curl)
    - [Using `curl` to download a file](#using-curl-to-download-a-file)
    - [Redirecting `curl` to a file](#redirecting-curl-to-a-file)
    - [Using option-flags on `curl`](#using-option-flags-on-curl)
- [Adding a .gitignore file to the repo](#adding-a-gitignore-file-to-the-repo)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Creating a new folder off of your home Desktop folder

Start by opening your Terminal/PowerShell. 

At the prompt, type the following to change your working directory to your **Desktop** folder:

```sh
$ cd ~/Desktop
```

(Remember to use **Tab** for auto-completion, *always*, and as soon as possible. Hit it as soon as you type `cd ~/Des`)

Assuming you don't already have a sub-directory named `project-stanford-quakebot`, the following use of the `mkdir` command will create this subdirectory:

```sh
$ mkdir project-stanford-quakebot
```

Note that we could have created this folder with a more *absolute* reference. In other words, instead of this:

```sh
$ cd ~/Desktop
$ mkdir project-stanford-quakebot
```

-- do this:

```sh
$ mkdir ~/Desktop/project-stanford-quakebot
```

I bring this up to make you aware that these steps can have variations depending on your *state* -- i.e. is your current working directory `~/Desktop`, or some other directory. If you don't follow the steps exactly, you could have a problem, i.e. you make the subdirectory somewhere *not* inside your `~/Desktop` directory. It's not hard to figure out or untangle, but easy to get confused if you get in the habit of just copy-pasting my examples instead of having a little insight of what's going on...


## Creating a git repo inside of a folder

OK, now let's create a **git repo** inside of the folder that you've just created for this exercise.

**But**, just to make sure you're in that directory -- e.g. you aren't resuming this step-by-step lesson after restarting your computer and reopening your Terminal, which by default would make your working directory your *home directory* -- use `cd` to make sure you're in the place that this lesson expects you to be:


```sh
$ cd ~/Desktop/project-stanford-quakebot
```


We are going to make this folder a **git repo**, which means running `git init` inside of it. Remember that `git init` is meant to be run only *once* when creating a new repo, and only inside a specific folder (a common mistake is to run `git init` in your *home* or `Desktop` directory, which is most definitely not what you want):

![image git-init-quakebot-repo.png](files/images/git-init-quakebot-repo.png)


## Creating and adding to files from the command-line

Again, you can add files to your `project-stanford-quakebot` folder as you would the "regular" way by dragging/dropping files into it. Let's try a few command-line ways.

### Redirecting output stream from a command/program into a file


Normally, the `echo` command by itself will spit arguments back to the screen -- otherwise known as *printing to screen*. 

```sh
$ echo 'hello world'
hello world
```

Using the **redirection** operator -- the right-angle-bracket `>` -- we can *redirect* the output of `echo` (and similar programs) into a file with a given filename. The following command will create a new file named `hey.txt` (or obliterate an existing file by that name) and fill its contents simply with the text, `hello world`:

```sh
$ echo 'hello world' > hey.txt
```

Again, redirection wipes out the existing file -- the following command would replace all of what was in `hey.txt` with the number `42`:


```sh
$ echo 42 > hey.txt
```

Double-right-angle-brackets -- `>>` -- will *append* the contents of a stream to a file:

```sh
$ echo 'This land is your land' > hey.txt
$ echo 'This land is my land' >> hey.txt
$ echo 'From the California to the New York island' >> hey.txt
```

### Downloading files via `curl`

Constructing files by manually appending words/lines is not very fun. Generally, we are pulling in data/text from external sources, i.e. the Internet, i.e. downloading.

This is where the **curl** program comes in ([read more](http://www.compciv.org/recipes/cli/downloading-with-curl/). 

> **Note: curl on Windows vs Mac**

>  Mac OS comes with `curl` installed. Windows PowerShell, in an utterly stupefying software design choice, decided to usurp the `curl` name for [something that is not really `curl` at all](http://thesociablegeek.com/azure/using-curl-in-powershell/)

> I'm assuming if you're reading this, you got Anaconda Python installed, which means you should be able to run this command to install the actual `curl` program and have it accessible via PowerShell:
> 
>     $ conda install curl

> **However**, in this guide (and elsewhere), when you see a shell command with `curl`, you will have to write `curl.exe` instead.

#### Using `curl` to download a file

`curl` is pretty easy. Its standard usage is to pass in a single argument, a URL that you want to download from. Check out the very simple webpage found at this URL:

https://compciv.github.io/stash/hello.html

And then use `curl` to download and stream its contents to your Terminal (i.e. print to screen):

![image curl-hello-html.png](files/images/curl-hello-html.png)

**Windows users**: Remember, when you see `curl` in the example shell code:

```sh
$ curl https://compciv.github.io/stash/hello.html
```

-- you want to type `curl.exe`

```sh
$ curl https://compciv.github.io/stash/hello.html
```

#### Redirecting `curl` to a file

Like `echo`, we can redirect the stream from `curl` into a file:

```sh
$ curl https://compciv.github.io/stash/hello.html > hey.txt
```


#### Using option-flags on `curl`

Like virtually every command-line program, `curl` has a set of options that can be specified. You can [read about a bunch of them in this other `curl` guide](http://www.compciv.org/recipes/cli/downloading-with-curl/). For the purposes of *this* guide and class, you'll see me use the `-o` flag (short for `--output`), which lets me specify a filename to save to:

```sh
$ curl -o stuff.html http://www.example.com
```

If you're thinking that the above seems to do the same thing as:

```sh
$ curl http://www.example.com > stuff.html
```

You're *pretty much* correct (there is a subtle difference). For me it's a style preference.

Anyway, we now know of a way to pull in external files from the Internet with ease. Read on for out that applies to this project.

## Adding a .gitignore file to the repo

In most repo/project folders of significant functionality, you'll have a bunch of files that you *do not* want to make part of the repo "history". The `git` convention is to specify.


