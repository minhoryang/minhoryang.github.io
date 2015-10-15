<!-- 
.. title: Gardening/Grooming My OS X Environment
.. slug: gardeninggrooming-os-x-for-developer
.. date: 2015-10-15 19:10:22 UTC+09:00
.. tags: brew, cask, docker, osx, pyenv, xcode, rootless, preferences, settings
.. category: tip
.. link: 
.. description: 
.. type: text
-->

## Clean Install OS X Latest
with Recovery Partition

-----
## App Store
~~Kakaotalk.app~~
**Microsoft Remote Desktop.app**
~~Movist.app~~
**Realm Browser.app**
**Slack.app**
**Xcode.app**

-----
## Xcode working-on-version: 6.4
`xcode-select -s <path>`

-----
## Keychain Assistants
Install certificates properly (please!!)

Get your default status screenshot.

-----
## Rootless
[Read carefully, please.](https://www.quora.com/How-do-I-turn-off-the-rootless-in-OS-X-El-Capitan-10-11)
and `csrutil disable`.

-----
## [brew](http://brew.sh/)
autoconf
automake
**bash**
**bash-completion2**
**brew-cask**
**[carthage](https://github.com/Carthage/Carthage)**
**[ccat](https://github.com/jingweno/ccat)**
**cloc**
coreutils
**[dark-mode](https://github.com/sindresorhus/dark-mode)**
docbook
docbook-xsl
**docker**
findutils
gdbm
**git**
**git-lfs**
grep
**htop-osx**
**[ish](https://github.com/grahamc/ish)**
jpeg
libevent
libidn
lzlib
**[mobile-shell](https://mosh.mit.edu/)**
moreutils
**[nload](http://www.roland-riegel.de/nload/)**
**nmap**
**openssh**
**openssl**
**p7zip**
pcre
**pigz**
**[pngpaste](https://github.com/jcsalterego/pngpaste)**
protobuf
**rabbitmq**
readline
**[reattach-to-user-namespace](https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard)**
**ssh-copy-id**
**[thefuck](https://github.com/nvbn/thefuck)**
**tmux**
**[trash](http://hasseg.org/trash/)**
tree
**vim**
**wget**
xz
**[z](https://github.com/rupa/z)**
**zsh**

(When installing, careful with various options -- See brew info first!)

-----
### zsh: [antigen](https://github.com/zsh-users/antigen)
`git`

`rimraf/k` ([link](https://github.com/rimraf/k))

`https://gist.github.com/2355834.git` ([git_prompt_info](https://gist.github.com/2355834.git))

`https://gist.github.com/342b10d7609679d8c566.git miloshadzic-minhoryang`  ([theme](https://gist.github.com/342b10d7609679d8c566.git))

-----
### vim: ~~[vundle](https://github.com/VundleVim/Vundle.vim)~~ [vim-plug](https://github.com/junegunn/vim-plug)

`set backspace=2`

`set backspace=indent,eol,start`

-----
### [pyenv-installer](https://github.com/yyuu/pyenv-installer)
[common-build-problems will block you](https://github.com/yyuu/pyenv/wiki/Common-build-problems)

-----
### tmux: .conf with personalized keymap

-----
## [brew cask](http://caskroom.io/)
**betterzipql**
cert-quicklook
~~chromecast~~
**cloud**
**cyberduck**
**fabric**
**filezilla**
**flux**
**google-chrome**
**handbrake**
**iterm2**
**java**
**launchrocket**
**macs-fan-control**
**mou**
~~navicat-for-postgresql~~
**ngrok**
**pgadmin3**
**postgres**
**pusher**
**pycharm**
qlcolorcode
qlimagesize
qlstephen
quicklook-json
**spectacle**
**tunnelblick**

-----
### chrome extensions
~~google cast~~
pushbullet

-----
### spectacle.app
`command-shift`
`+ arrows`

`+ spacebar` for fullscreen

`+ 1 and 2` for swapping display

`+ - and =`(+) for smaller/larger

-----
### tunnelblick.app `with VPN Certs`

-----
## downloads
[**Bandizip-X**](http://www.bandisoft.co.kr/bandizip/x/)


-----
## Trim Enable
`sudo trimforce enable`


-----
## System Preferences
### Security & Privacy
`filevault-enable`

`firewall-block-all`

`session-timeout-1m`

`login-window-add-description`

`location-services-only-for-find-my-mac`

`disable-remote-control-infrared-receiver`


### Sharing
`Computer-Naming and No-Sharing`

### Bluetooth
`can't-wakeup`

### Trackpad
`right-click`

### Accessibility (?!)
`3-click-drag`

### Dock
`auto-hide`

### Networks
`google-dns`

`wifi-security-wpa2-enterprise`

### iCloud
`sync-disable`

### Language
`keyboard-switching-keymap`

### Spotlight
`only-for-apps`

### Battery
`percent`

### Users
`fast-user-switching`

`guest-approved`


-----
## Deep Configs [.osx](https://github.com/mathiasbynens/dotfiles/blob/master/.osx)
Warn! from here, weird thingy happened :)

### used keywords:
**`Disable the sound effects on boot`**

**`Disable transparency in the menu bar and elsewhere on Yosemite`**

**`Set highlight color to green`**

`Set sidebar icon size to medium`

`Increase window resize speed for Cocoa applications`

`Expand save panel by default`

**`Save to disk (not to iCloud) by default`**

`Automatically quit printer app once the print jobs complete`

`Disable the “Are you sure you want to open this application?” dialog`

`Remove duplicates in the “Open With” menu`

`Display ASCII control characters using caret notation in standard text views`

`Disable Resume system-wide`

`Set Help Viewer windows to non-floating mode`

`Restart automatically if the computer freeze`

**`Check for software updates daily, not just once per week`**

**`Disable Notification Center and remove the menu bar icon`**

`Disable smart quotes as they’re annoying when typing code`

`Disable smart dashes as they’re annoying when typing code`

`Disable local Time Machine snapshots`

`Disable hibernation`

`Remove the sleep image file to save disk space`

`Disable the sudden motion sensor as it’s not useful for SSDs`

**`Trackpad: enable tap to click for this user and for the login screen`**

**`Trackpad: map bottom right corner to right-click`**

`Increase sound quality for Bluetooth headphones/headsets`

`Enable full keyboard access for all controls`

`Disable press-and-hold for keys in favor of key repeat`

**`Set a blazingly fast keyboard repeat rate`**

`Disable auto-correct`

**`Stop iTunes from responding to the keyboard media keys`**

**`Require password immediately after sleep or screen saver begins`**

**`Save screenshots to`**

`Save screenshots in PNG format`

`Finder: allow quitting via ⌘ + Q`

`Show icons for hard drives, servers, and removable media on the desktop`

`Finder: show hidden files by default`

`Finder: show all filename extensions`

`Finder: show status bar`

`Finder: show path bar`

`Display full POSIX path as Finder window title`

`When performing a search, search the current folder by default`

`Disable the warning when changing a file extension`

`Enable spring loading for directories`

`Remove the spring loading delay for directories`

**`Avoid creating .DS_Store files on network volumes`**

`Automatically open a new Finder window when a volume is mounted`

`Show item info near icons on the desktop and in other icon views`

`Show item info to the right of the icons on the desktop`

`Enable snap-to-grid for icons on the desktop and in other icon views`

`Increase grid spacing for icons on the desktop and in other icon views`

`Increase the size of icons on the desktop and in other icon views`

`Use list view in all Finder windows by default`

`Enable AirDrop over Ethernet and on unsupported Macs running Lion`

`Show the ~/Library folder`

`Expand the following File Info panes: “General”, “Open with”, and “Sharing & Permissions”`

**`Disable Dashboard`**

`Don’t show Dashboard as a Space`

`Don’t automatically rearrange Spaces based on most recent use`

`Remove the auto-hiding Dock delay`

`Remove the animation when hiding/showing the Dock`

`Automatically hide and show the Dock`

`Make Dock icons of hidden applications translucent`

**`Disable the Launchpad gesture`**

`Reset Launchpad, but keep the desktop wallpaper intact`

**`Privacy: don’t send search queries to Apple`**

`Press Tab to highlight each item on a web page`

`Show the full URL in the address bar`

`Allow hitting the Backspace key to go to the previous page in history`

`Hide Safari’s bookmarks bar by default`

`Hide Safari’s sidebar in Top Sites`

`Disable Safari’s thumbnail cache for History and Top Sites`

**`Only use UTF-8 in Terminal.app`**

`Prevent Time Machine from prompting to use new hard drives as backup volume`

`Show the main window when launching Activity Monitor`

`Visualize CPU usage in the Activity Monitor Dock icon`

`Show all processes in Activity Monitor`

`Sort Activity Monitor results by CPU usage`

**`Allow installing user scripts via GitHub Gist or Userscripts.org`**


-----
## Permanently Fixed Anonymous Session
Using fast-user-switcher, swap `/System/Library/User Template/English.lproj` with well-groomed `/Users/Guest`. [Guide](https://youtu.be/JU-W2-_c5bA)
