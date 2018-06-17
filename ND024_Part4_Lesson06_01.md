# Lesson 6.1 Introduction

Instructor:
Carl

Course is about HTTP and web servers. HTTP, the Hypertext Transfer Protocol, is the language that web browsers and web servers speak to each other. Every time you open a web page, or download a file, or watch a video like this one, it's HTTP that makes it possible. In this course, you'll take a look at how all that takes place. In lesson one, you'll explore the building blocks of HTTP. In lesson 2, you'll write web server and client programs from the ground up and handle user input from HTML forms. In lesson 3, you'll learn about web server hosting, cookies, and many other more practical aspects of building web services. This course is a bridge. It's going to connect your knowledge of basic web technologies, like HTML, with your experience writing code in python. With that foundation, you can go on to learn and build many more awesome things. Let's get started.


### Introduction: HTTP and Web Servers
Welcome to our course on HTTP and Web Servers! In this course, you'll learn how web servers work. You'll write web services in Python, and you'll also write code that accesses services out on the web.

This course isn't about installing Apache on a Linux server, or uploading HTML files to the cloud. It's about how the protocol itself works. The examples you'll build in this course are meant to illustrate the low-level behaviors that higher-level web frameworks and services are built out of.

### Getting started
You'll be using the command line a lot in this course. A lot of the instructions in this course will ask you to run commands on the terminal on your computer. You can use any common terminal program —

- On Windows 10, you can use the bash shell in [Windows Subsystem for Linux](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide). **Personal note: I used this option. Interesting option, we can install linux distribution as well to our Windows 10 system.**
- On earlier versions of Windows, you can use the Git Bash terminal program from [Git](https://git-scm.com/download/win).
- On Mac OS, you can use the built-in Terminal program, or another such as iTerm.
- On Linux, you can use any common terminal program such as gnome-terminal or xterm.

### Python 3
This course will not use a VM (virtual machine). Instead, you will be running code directly on your computer. This means you will need to have Python installed on your computer. The code in this course is built for Python 3, and will not all work in Python 2.

- Windows and Mac: Install it from python.org: https://www.python.org/downloads/
- Mac (with Homebrew): In the terminal, run brew install python3
- Debian/Ubuntu/Mint: In the terminal, run sudo apt-get install python3

Open a terminal and check whether you have Python installed:

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/October/57fbecbd_image-0/image-0.png">

Checking Python versions with the --version option.

    Depending on your system, the Python 3 command may be called python or python3. Take a moment to check! Due to changes in the language, the examples in this course will not work in Python 2.

    In the screenshot above, the python command runs Python 2.7.12, while the python3 command runs Python 3.5.2. In that situation, we'd want to use python3 for this course.

### Interactive Python
You should be familiar with the Python interactive interpreter. When you see code examples with the >>> prompt in this course, those are things you can try out in Python on your own computer. For instance:
```
>>> from urllib.parse import urlparse
>>> urlparse("https://classroom.udacity.com/courses/ud303").path
'/courses/ud303'
```
### Git
You will need to have the git version control software installed. If you don't have it already, you can download it from https://git-scm.com/downloads.

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/January/58866e37_screen-shot-2017-01-23-at-12.57.08/screen-shot-2017-01-23-at-12.57.08.png">

Checking that git is installed, by running git --version in the terminal.

You'll be using Git to download course materials from the Github repository https://github.com/udacity/course-ud303. (You don't need to do this yet.) You'll also use it as part of an exercise on deploying a server to a hosting provider.

### Nmap
You'll also need to install ncat, which is part of the Nmap network testing toolkit. We'll be using ncat to investigate how web servers and browsers talk to each other.

- Windows: Download and run https://nmap.org/dist/nmap-7.30-setup.exe
- Mac (with Homebrew): In the terminal, run brew install nmap
- Mac (without Homebrew): Download and install https://nmap.org/dist/nmap-7.30.dmg
- Debian/Ubuntu/Mint: In the terminal, run sudo apt-get install nmap


To check whether ncat is installed and working, open up two terminals. In one of them, run ncat -l 9999 then in the other, ncat localhost 9999. Then type something into each terminal and press Enter. You should see the message on the opposite terminal:

ncat is not running on HTTP, but at the network layer below HTTP, called TCP. But we can use this to experiment with HTTP servers, which we'll do later in this lesson. 

What's going on here? Well, one of the ncat programs is acting as a very simple network server, and the other is acting as a client.

Note: If you get an error such as "Address already in use", this means that another program on your computer is using port 9999. You can pick another port number and use it. Make sure to use the same port number on the server and client sides.

To exit the ncat program, type Control-C in the terminal. If you exit the server side first, the client should automatically exit. This happens because the server ends the connection when it shuts down.

You'll be learning much more about the interaction between clients and servers throughout this course.


- - -
Next up: [Your first web server](ND024_Part4_Lesson06_02.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
