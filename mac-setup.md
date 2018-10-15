# Setting up your Mac for development

Getting your tools right is an important step in becoming a developer. This guide will walk you through every step you need to take.

There are multiple options that can be used when setting up your computer. This guide is opinionated about those options. Our guidelines are:

- When possible, use what you already have instead of installing something new.
- Use the most common development tool unless it is deficient.
- Less setup is better.

## Update your system

Before anything else, update your operating system. To do that, go to the **Apple Menu () > About This Mac > Software Update**.

## Security settings

Open **System Preferences > Security & Privacy** and set the following:

- Under General, set _require a password after sleep or screen saver begins_ to _immediately_.
- Click _Advanced…_ and select _Require an administrator password to access system-wide preferences_.
- Under _Firewall_, click _Turn Firewall On_.
- Under _FileVault_, enable FileVault. This will encrypt your disk. Without it, anyone with a bootable USB drive can get full access to your computer.

## iTerm2

iTerm2 is an open source replacement for Apple's Terminal. It's highly customizable and comes with a lot of useful features.

You can get the app from [the iTerm2 downloads page](http://www.iterm2.com/downloads.html). Once downloaded, drag and drop the iTerm application file into your Applications folder.

See [this iTerm2 setup guide](http://sourabhbajaj.com/mac-setup/iTerm/) for optional suggested settings.

**NOTE:** Run iTerm now to open a terminal window. For the rest of this guide, when we ask you to run something in the terminal or "on the command line", we will be referring to typing the command into an iTerm terminal window and pressing Enter. We will often just say "run" with a command beneath, like this:

    $ cd ~

When you see these commands, **do not** paste the `$`. This dollar sign is there to indicate the terminal prompt.

## XCode

XCode is a set of developer tools from Apple that have to be installed. To install them, go to the App Store and install XCode. This is a big package and will take quite a while.

Once XCode is installed, run the following in your terminal:

    $ sudo xcodebuild -license
    $ xcode-select --install

The first line will prompt you to read the license and agree to it. It will ask for your password. The second line will prompt you to install the command line tools. Follow the instructions and you'll have Xcode and Xcode command line tools both installed.

## Homebrew

[Homebrew](https://brew.sh/) calls itself _The missing package manager for macOS_ and is an essential tool for any developer.

To install Homebrew paste the following command in your terminal, hit **Enter**, and follow the steps on the screen:

    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

One thing we need to do is tell the system to use programs installed by Homebrew (in `/usr/local/bin`) rather than the OS default if it exists. We do this by adding `/usr/local/bin` to your `$PATH` environment variable:

    $ echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile

To be able to use `brew` you need to start a new terminal session. Do this by opening a new terminal tab with **Cmd+T** (you should also close the old one), then run the following command to make sure everything is working:

    $ brew doctor

### Using Homebrew

To install a package (or **formula** in Homebrew vocabulary) simply run:

    brew install <formula>

To update Homebrew's directory of formulae, run:

    brew update

To see if any of your packages need to be updated:

    brew outdated

To update a package:

    brew upgrade <formula>

To see what you have installed (with their version numbers):

    brew list --versions

## Git and GitHub

If you do not yet have a [GitHub](https://github.com/) account, go there and register for one.

[Git](http://git-scm.com/) is the version control tool we will use in class to manage your code. To install it, run:

    $ brew install git

When done, to test that it installed correctly, you can run:

    $ git --version

And `$ which git` should output `/usr/local/bin/git`.

Next, we'll define your Git user (this should be the same name and email you use for [GitHub](https://github.com/)):

```sh
$ git config --global user.name "Your Name Here"
$ git config --global user.email "your_email@youremail.com"
```

This data will get added to your `.gitconfig` file.

To push code to your GitHub repositories, we're going to use the recommended HTTPS method. So you don't have to type your username and password everytime, enable Git password caching as described [here](https://help.github.com/articles/caching-your-github-password-in-git/):

    $ git config --global credential.helper osxkeychain

### Git and .DS_Store files

On a Mac, it is important to remember to add `.DS_Store` (a hidden macOS system file that's put in folders) to your `.gitignore` files.

Configure your Git to globally exclude those files:

```sh
# specify a global exclusion list
$ git config --global core.excludesfile ~/.gitignore
# adding .DS_Store and other Mac-specific files to that list
$ curl https://raw.githubusercontent.com/github/gitignore/master/Global/macOS.gitignore -o ~/.gitignore
```

### Git and the command line

We want to add two things to your command line: the ability to autocomplete Git commands and information about Git to your prompt. To do this, run:

```
$ brew install bash-completion bash-git-prompt
$ echo '[[ -f "$(brew --prefix)/etc/bash_completion" ]] && source "$(brew --prefix)/etc/bash_completion"' >> ~/.bash_profile
$ echo '[[ -f "$(brew --prefix)/opt/bash-git-prompt/share/gitprompt.sh" ]] && source "$(brew --prefix)/opt/bash-git-prompt/share/gitprompt.sh"' >> ~/.bash_profile
```

Exit the terminal and start a new window. Your command line should now look like this:

```
✔ ~
13:09 $
```

## Python

Python has two different major versions, Python 2 and Python 3. We will use Python 3 throughout this course. While Python 3 is widely used, Python 2 is the default still on OS X, so we will have to install Python 3, as well as a tool we will use throughout the course to manage Python projects, `pipenv`. To install these, run:

```
$ brew install python3 pipenv
```

Once this is done, you should be able to run the following commands and get output like this:

```
$ python3 --version
Python 3.7.0
$ pipenv --version
pipenv, version 2018.10.13
```

Python has its own way of installing Python-specific packages, called "pip". To use the Python 3 version of pip, we have to run `pip3`. Run the following to install a few more tools we'll need:

```
$ pip3 install flake8 autopep8 pep8-naming isort
```

## Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) (VSCode) is the program we will primarily use to edit code. Go to [the VSCode homepage](https://code.visualstudio.com/) and download it. Once downloaded, drag and drop the Visual Studio Code application file into your Applications folder.

## Google Chrome

[Google Chrome](https://www.google.com/chrome/) is the browser we will use in class. Download it. Once downloaded, drag and drop the Google Chrome application file into your Applications folder.
