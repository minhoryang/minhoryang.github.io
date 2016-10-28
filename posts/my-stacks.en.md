<!-- 
.. title: 난 무슨 프로그램을 사용하는가?
.. slug: my-stacks
.. date: 2016-10-28 23:40:12 UTC+09:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

# 난 무슨 프로그램을 사용하는가?

## usesthis.com
내가 정기구독 하는 사이트 중에 재밌는 곳이 하나 있다.

[usesthis.com](https://usesthis.com) 라고, 유명한 사람들의 작업환경을 소개하는 블로그인데, 2009년도에 [Alex Payne](https://usesthis.com/interviews/alex.payne/)로 스타트를 끊어서, [Gabe Newell](https://usesthis.com/interviews/gabe.newell/), [Paul Graham](https://usesthis.com/interviews/paul.graham/)의 지원사격으로 시작된, 그야말로 말도안되는 사이트로서, 보다시피 X쩌는 분들의 TechStack을 엿볼 수 있다.

지금까지 700명의 인터뷰가 올라가있고, 매주 화요일 목요일에 새 글이 올라오니까 볼만할거다.

우선 내가 좋아하는 몇분을 더 추려보자면
- [Aaron Boodman](https://usesthis.com/interviews/aaron.boodman/)
- [Eric Meyer](https://usesthis.com/interviews/eric.meyer/)
- [Andy Smith](https://usesthis.com/interviews/andy.smith/)
- [Tom Preston-Werner](https://usesthis.com/interviews/tom.preston-werner/)
- [Robert Böhnke](https://usesthis.com/interviews/robert.bohnke/)
- [Eric S Raymond](https://usesthis.com/interviews/eric.s.raymond/)
- [Daniel Stenberg](https://usesthis.com/interviews/daniel.stenberg/)
- [Greg Kroah-Hartman](https://usesthis.com/interviews/greg.kh/)
- [Yan Zhu](https://usesthis.com/interviews/yan.zhu/)
- [Diana Kimball](https://usesthis.com/interviews/diana.kimball/)
- [George Nachman](https://usesthis.com/interviews/george.nachman/)
- [Bjarne Stroustrup](https://usesthis.com/interviews/bjarne.stroustrup/)
- [Monica Dinculescu](https://usesthis.com/interviews/monica.dinculescu/)
- [Jessie Frazelle](https://usesthis.com/interviews/jessie.frazelle/)
  이정도? 

## dotfiles.github.io
또 재밌는 운동 중에 하나는 [dotfiles.github.io](https://dotfiles.github.io/)가 있다.

dotfile이란 간단히 말해서 `.`으로 시작하는 파일을 의미하는데, 이러면 Unix계열 운영체제에서는 숨김파일처럼 보여서 사용자의 환경설정을 보관하는데 많이들 사용한다. [dotfiles.github.io](https://dotfiles.github.io/)에 가면, 유명한 or 잘만들어진 dotfiles의 예시와 dotfiles를 관리하기 위한 많은 자료들을 볼 수 있다.

사실 환경설정 안에는 개발자들의 작업환경부터 시작해서, 쓰는 프로그램, 습관, 또 그 습관을 고치기 위한 툴들을 발견할 수 있고, 나에게 맞는 것을 하나씩 하나씩 적용하다보면, 자신의 작업환경도 상당히 쾌적하게 바뀌고 능률도 상승하는 것을 경험할 수 있다.

개발자들의 커뮤니티인 Github에서 [dotfiles를 검색](https://github.com/search?o=desc&q=dotfiles&ref=opensearch&s=stars&type=Repositories)해보면 많은 개발자들의 환경설정을 볼 수 있으니, 시간이 남고, 더 이상 작성할 테스트가 없으며, 심지어 yak shaving도 재미가 없어진다면, 이만한 타임머신이 또 없다. 강추.

## minhoryang's stacks

나도 약 일년 전에 [Gardening/Grooming My OS X Environment](https://minhoryang.github.io/en/posts/gardeninggrooming-os-x-for-developer/)라는 글을 작성한 적이 있는데, 약간 불친절했지. 백업용처럼 썼으니까. 이번에는 좀 더 친절히 써보기로했다. <!-- 여자친구가 이번에 맥을 구매했다 :) -->

나는 **Unibody Macbook 13" Late 2008**과 **Macbook Pro 15" Retina Mid 2015**를  쓴다.
하나는 내가 대학 입학할 때 산거고, 후자는 이번에 회사에 입사하면서 지급받았다.

고로 내 설정은:

- Mac
- 낮은 성능 (2008년도 맥북에서도 화가 나지 않아야 함)
- 업무와 일상의 분리
- 항상 최신버전
- 보안

이런 특징을 가지고 있다. 차근차근히 나열해볼테니 좋은걸 하나 건질 수 있기를.

### Mac OS (OS X)
깨끗한 Mac OS를 준비한다.

> 깨끗하다는 뜻은, 갓 노트북의 포장을 뜯었거나 갓 전체포맷을 하여, 설치화면이 띄워져 있고, iCloud 연결이 아직 되지 않은 상태를 말한다.

- iCloud는 업데이트가 다 끝나고 나서야 설정에서 로그인 할 것이다.
- Recovery Partition이 있어야 한다. (전체포맷시 날아갈 수도 있다. 부팅시 Option키를 눌러서 꼭 확인해보도록.)
- 맥에서 프로그램을 설치할 때는 **[Mac App Store](https://itunes.apple.com/kr/)**Ⓐ와 **[Homebrew](http://brew.sh/index_ko.html)**Ⓑ 그리고 **[Homebrew Cask](https://caskroom.github.io/)**Ⓒ를 이용한다.
  - 관리하기에도 업데이트하기에도 보안에도 좋다.

#### My System Preferences
- Security & Privacy
  - Required password `immediately` 로 설정해서 잠자기 이후 자동으로 잠기게 해둔다.
  - Set Lock Message를 등록해놓는다. (휴대폰번호/소속)
  - Advanced... 버튼을 눌러서 다음 두가지 항목을 설정한다.
    - Log out after `10` minutes
    - Required an administrator password to access system-wide preferences
  - FileVault를 꼭 켠다.
    - Disk암호화를 해주며, 시간이 오래걸리니 맥 설치 직후 걸어두는게 좋다.
  - Firewall에서 Block all incoming connections을 설정해두고 개발시 필요할 때마다 열어서 사용한다.
  - Privacy에서 Location Services는 Find my mac만 걸어두고 나머지는 다 끈다.
- Sharing
  - 컴퓨터의 이름을 적절히 바꾸고, 모든 공유를 끈다.
- Bluetooth
  - 블루투스 장치를 사용하지 않을경우 꼭 끄고, 필요할 때만 킨다.
  - Advanced를 눌러 자신의 상황에 맞게 설정한다. (난 블루투스 장치를 사용하지 않으니 셋 다 끈다.)
  - Bluetooth 아이콘을 메뉴바에 꺼낸다.
- Trackpad
  - 오른쪽 클릭을 위해 `Secondary Click`을 켠다.
- Accessibility
  - Mouse & Trackpad에서 Trackpad Options을 들어가서 `Three Finder Drag` 옵션을 킨다.
- Dock
  - 자신의 상황에 맞추지만 난 오른쪽 중앙에 가장 작은 사이즈로 Auto Hide 해놓는다.
- Networks
  - DNS를 8.8.8.8를 쓴다.
  - Wifi 아이콘을 메뉴바에 꺼낸다.
- iCloud
  - 자신이 사용하는 것만 켜는데, Keychain과 Back to my mac은 추천하지 않는다. (사실 Find My Mac빼고는 다 추천하지 않는다.)
- Language
  - Keyboard 설정에서 Shortcuts을 수정할 수 있는데
    - Input Source 설정을 Command-Space로 설정한다.
    - Spotlight를 Command-Space-/ 로
    - Spotlight/Finder Search를 Command-Space-. 로
    - App Shortcut에 Help Menu를 끈다.
- Spotlight
  - Application과 Other와 System Preferences만 켠다.
  - Privacy로 홈폴더를 검색하지 않게 해놓는다. (적절히)
- Battery
  - Battery 아이콘을 메뉴바에 꺼낸다.
    - 메뉴바에서 배터리 잔량을 %로 표시하도록 바꾼다.
- Users
  - Guest User를 사용한다.
    - [`/System/Library/User Template/English.lproj`를 교체해서 Guest User의 세팅을 내가 Tweak할 수 있다.](https://youtu.be/JU-W2-_c5bA)
      - Network 분석을 하거나, 믿지 못하는 Network를 사용하거나, 회사와 관련되지 않은 일을 할 때, Guest User를 사용하는 편이다.
  - Login Options에서 Fast User Switching을 사용한다.

#### Keychain Assistants

Keychain Assistants는 맥에서 인증서와 인증키들을 관리하는 곳인데, 각각의 인증 정보들이 잘 관리가 되지 않는 문제가 있다. **초기 세팅을 꼭 스크린샷을 찍어두든지, 이름을 바꾸는걸 추천한다. (바꿔도 문제없다.)**

맥에서 인증문제가 생기면 여기서 필요없는 것들을 찾아서 지워야하니, 꼭 확인해주시라.

- 공용 Mac에서 특정 서비스(HTTP/HTTPS/SSH/+GIT)에 로그인을 한 적이 있어서 지우고 싶다.
- Xcode 의 개발자 계정을 2개 이상 쓰고 싶다. (기존에 쓰던 계정이 있었는데, 새 계정을 쓰고싶다.)
- Xcode 의 개발자 계정을 다른사람과 나눠쓰고 싶다.
- Xcode 에서 App Release를 해야하는데 App Signing이 잘 안된다.
- Git의 인증이 credential-osxkeychain 모드로 처리되고 있어서 내가 원하는 방식으로 인증이 진행되고 있지 않았다.
  - Github의 OAuth2 Token인증이 이상하다.
- iTunes 계정을 여러개를 쓰는데, 갑자기 전환이 잘 안된다.
- iMessage 인증이 깨졌다.
- 자동로그인을 하는 앱이 무한 로그인 실패를 겪고있다.

이런 문제를 겪을 때는 Keychain Assistant의 뒤를 밟아라.

#### [OS X Server](https://itunes.apple.com/kr/app/os-x-server/id883878097?mt=12)Ⓐ

OS X Server는 OS X의 서버기능을 사용할 수 있도록 운영체제를 바꿔주는건데, 여기서 *정확히 필요한 기능이 있지 않는 이상, 설치하는걸 추천하지 않는다*.

- IP/DNS가 고정될 수 있는 환경에서 쓰는걸 추천 (Macbook은 여기에서 부적합하다.)
- [(나에게) 불필요한 OS X Server 서비스를 끄는 스크립트](https://gist.github.com/minhoryang/4c7b56324c5f2e5a8694)

#### [`.OSX` Script](https://github.com/mathiasbynens/dotfiles/blob/master/.macos)

OS X의 매우 Deep한 설정을 바꿀 수 있다. 한줄한줄 읽어보며 자신에게 필요한 걸 챙겨보고, 실행하기전에 한번만 더 생각해보라.

- [내가 쓰는 옵션들](https://gist.github.com/minhoryang/e48c865875e163f8897c3899e298c21c)

### Everywhere & Everyday Programs
어떤 OS던지 간에 공통적으로 쓰는 툴들은 다음과 같다.

- **[LastPass](https://lastpass.com/ko/)**Ⓒ

  비밀번호를 관리해주는 프로그램인데, 말 그대로 내가 가입해놓은 많은 사이트들의 ID와 비밀번호를 한곳에서 통합관리를 해준다.
  Chrome과 합치면 자동 로그인도 해주며, 나는 SSH에 접속하기 위한 PEM파일도 맞기는 편이다.
  Role에 따라 계정을 분리해서 사용하고 있다. (개인/회사)

- **[Google Chrome](https://www.google.com/chrome/)**Ⓒ

  다른 좋은 웹브라우져도 많은데 (Firefox, Edge, ...) 이걸 쓰는 이유는
  - **Extension** 기능 : 확장 프로그램이라고 부른다. Chrome을 더욱 풍부하게 만들어준다.
  - **People** 기능 : 프로파일이라고 부르는데 각 사용자 별로 환경설정을 분리할 수 있다. Command + `로 전환해서 사용한다.
    - "회사 Google Account"용
      - 사용시 바로 이슈 관리 시스템인 Jira와 모니터링 시스템인 NewRelic에 접속된다.
      - [LastPass](https://chrome.google.com/webstore/detail/hdokiejnpimakedhajhdlcegeplioahd) : 회사 계정 관리
      - [Google Calendar](https://chrome.google.com/webstore/detail/google-calendar-by-google/gmbgaklkmjakoegficnlkhebmhkjfich) : 회사 일정 안내
      - [Google Mail Checker](https://chrome.google.com/webstore/detail/mihcahmgecmbnbcchbopgniflfhgnkff) : 회사 메일 안내
      - [Google Docs Offline](https://chrome.google.com/webstore/detail/google-docs-offline/ghbmnnjooekpmoecnnnilnnbdlolhkhi) : 회사 문서를 오프라인일 때도 보고 편집할 수 있게 해준다. (회사가 있는 곳에 게임회사들이 많아서, 게임들이 업데이트 될 때에는 인터넷이 잘 안된다...)
    - "개발 및 소스코드 서핑"용
      - [LastPass](https://chrome.google.com/webstore/detail/hdokiejnpimakedhajhdlcegeplioahd) : 개발 계정 관리
      - **[SimpleExtManager](https://chrome.google.com/webstore/detail/simpleextmanager/kniehgiejgnnpgojkdhhjbgbllnfkfdk?hl=ko)** : Extensions이 많을 때 간단히 끄고 킬 수 있게 해준다. 사용하지 않는 건 끄는게 좋다.
      - [Secure Shell](https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo?hl=ko) : ssh에 접속할 수 있게 해준다.
      - [Mosh](https://chrome.google.com/webstore/detail/mosh/ooiklbnjmhbcgemelgfhaeaocllobloj) : ssh의 발전된 형태인 mosh에 접속할 수 있게 해준다. 인터넷 연결이 좋지 않아도 ssh를 편하게 쓸 수 있다.
      - **[JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc)** : Json을 멋지게 보여준다. 현재 어느 노드에 있는지를 말해준다.
      - [User Agent Switcher for Chrome](https://chrome.google.com/webstore/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg) : UserAgent를 테스트할 때 쓸 수 있다. Developer Tools에서도 비슷한 기능을 이용할 수 있다.
      - [Pushbullet](https://www.pushbullet.com/) : 개발용 푸시를 주고 받을 때 사용하고 있다.
    - "SoundCloud/Youtube 음악감상"용
      - **[Looper for Youtube](https://chrome.google.com/webstore/detail/looper-for-youtube/iggpfpnahkgpnindfkdncknoldgnccdg)** : Youtube에서 반복재생을 할 수 있다!
  - **Incognito** 기능 : 시크릿모드라고 알고있는 기능으로 작업중, 위의 3가지 일이 아닐 때는 이 기능을 이용해 Extensions을 쓰지 않고 사용한다.
    - [Off The Record History](https://chrome.google.com/webstore/detail/off-the-record-history/djbaolpiihkcmmfjnjdmomeeheldhhdp?hl=en-US) 라는 익스텐션을 이용해서, 시크릿 모드에서도 사용 내역을 기록한다.
    - [NoCountryRedirect (NCR)](https://chrome.google.com/webstore/detail/nocountryredirect-ncr/ciboebddidackjicoeoiigdnbmchkdll) : 항상 google.com 으로 들어갈 수 있게 해준다.
    - **[SVG Screenshot](https://chrome.google.com/webstore/detail/svg-screenshot/fdjeimdcjbkbddhedpppgjnhfkjdkpcc?hl=ja)** : 링크를 누를 수 있는 스크린샷을 찍어준다!! 확장자는 SVG.
    - [HTTPS Everywhere](https://chrome.google.com/webstore/detail/https-everywhere/gcbommkclmclpchllfjekcdonpmejbdp?hl=ko) : HTTPS를 쓸 수 있으면 쓰게해준다.
    - [uMatrix](https://chrome.google.com/webstore/detail/umatrix/ogfcmafjalglgifnmanfmnieipoejdcf) : NoScript의 Chrome 버전이라고 생각하고 쓰고있다. 믿지않는 사이트들에서 JavaScript를 사용하지 않게 해준다.
    - **[Starsucks](https://chrome.google.com/webstore/detail/starsucks/ccpijncgingpepdgbjaglhnomiikmenp?hl=ko)**

  - **Developer Tools** 기능 : 개발할때 정말 많은 도움이 된다. Remote Debugging 기능을 정말 애용하고있다.
  - **Google Cast** 기능 : Chromecast에 화면이나 소리를 보낼 수 있다!
  - **Google Cloud Print** 기능 : 인터넷으로 연결된 프린터를 사용할 수 있다. 회사의 프린터를 회사계정을 통해 로그인 하면 바로 사용할 수 있다!

대부분의 경우, 노트북에서 바로 개발을 한다기 보다는 개발 서버에 접속해서 개발을 진행한다.

- 맥이나 리눅스에 접속할때는 **SSH**를 이용한다.
  - 윈도우에서는 [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
  - 맥/리눅스에서는 *최신* OpenSSH를 이용한다.
  - Mosh로 접속할 수 있는 서버라면 꼭 Mosh로 접속한다.
- 윈도우에 접속할 때는 **[Microsoft Remote Desktop](https://itunes.apple.com/kr/app/microsoft-remote-desktop/id715768417?mt=12)**Ⓐ를 이용한다. ([CoRD](http://cord.sourceforge.net/)Ⓒ를 사용하는 분들도 있더라)
- **[FileZilla](https://filezilla-project.org/)**Ⓒ : 개발 서버와 파일을 주고받기 위해 쓴다.
- **[OpenVPN](https://openvpn.net/)**Ⓑ : 닫혀있는 망에 접속하기 위해 구성된 VPN서버에 연결하기 위해 쓴다. *(주의!)*
  - 맥에서는 **[TunnelBlick](https://tunnelblick.net/)**Ⓒ을
  - 리눅스나 윈도우에서는 OpenVPN을 바로 쓴다.

사실 이 6개만 있으면 웬만한 일은 다 처리할 수 있다.

### IDE / Editor
- **[Xcode](https://itunes.apple.com/kr/app/xcode/id497799835?mt=12)**Ⓐ

  - SDK와 Simuation은 환경 설정에서 따로 받아야 한다.
  - **개발 환경을 백업해두는게 굉장히 중요한데**, [Xcode](https://itunes.apple.com/kr/app/xcode/id497799835?mt=12)는 특히 더 중요하다.
    **무언가 개발하고 있는게 있고, 그게 런치되기 직전이라면, Mac에서 업데이트를 섯불리 누르지 마라.** 
    - 새로운 SDK와 새로운 Xcode와 새로운 Compiler는 되던걸 안되게 만드는 n년간의 노하우가 있다.
    - 잘 돌던 Bash Script도 깨진다. (진짜임)
    - Xcode가 운영체제에 영향을 미치는 범위가 꽤나 커서, 그만큼 되던게 안된다고 생각하는게 편하다.
  - 개발환경 백업은 상당히 편한데, `Xcode.app`의 이름을 `Xcode.7.3.1.app`으로 바꾸고, 새  Xcode를 앱스토어에서 받으면 된다.
    - 기존의 Xcode를 사용하고 싶다면, 아래와 비슷한 명령이 필요하다.
      `xcode-select -s /Applications/Xcode.7.3.1.app/Contents/Developer` 
  - 놀랍게도 Xcode에도 Plugin System이 있다. [Alcatraz](http://alcatraz.io/) 를 확인해보라!
  - [Xcode를 Ramdisk에 띄워서 좋은 성능을 얻는 스크립트](https://gist.github.com/derjohng/a828e4c40a328fe5881f)가 있다.

- **Vim**

  - Mac에 기본으로 깔려있는 Vim을 이용하려면 이런 .vimrc가 필요하더라.

    ```text
    # .vimrc
    syntax on
    set backspace=2
    set backspace=indent,eol,start
    command -bar -bang Q quit<bang>
    ```

  - 그러나 나는 **[NeoVim](https://neovim.io/)**Ⓑ이라는 Vim을 쓰며, 새 [init.vim](https://gist.github.com/minhoryang/f70de285cee22b827f2c3c6c7f8e7f09)를 사용하고 있다.

  - 아래는 내가 사용하는 플러그인들 목록이며, 웬만한 링크는 클릭하면 스크린샷으로 작동화면을 볼 수 있다ㅇ

    - **[vim-plug](https://github.com/junegunn/vim-plug)** 로 vim의 플러그인을 관리하며,

    - **[scrooloose/nerdtree](https://github.com/scrooloose/nerdtree)** 로 폴더목록을 보고,

    - [Xuyuanp/nerdtree-git-plugin](https://github.com/Xuyuanp/nerdtree-git-plugin) 으로 각 파일의 git 상태를 보며,

    - **[bogado/file-line](https://github.com/bogado/file-line)** 은 `vi app.py:101`이라는 명령을 칠 수 있도록 해준다.
      (Traceback이나 Stacktrace 줄을 바로 복사/붙여넣기 -> 행복!)

    - **[simnalamburt/vim-mundo](https://github.com/simnalamburt/vim-mundo)** 으로 실수를 바로잡고 (undo),

    - **[rhysd/committia.vim](https://github.com/rhysd/committia.vim)** 로 `git commit`을 편하게 진행한다.

      ```text
      # .gitconfig
      [diff]
              tool = nvimdiff
      [difftool "nvimdiff"]
              cmd = "nvim -d \"$LOCAL\" \"$REMOTE\""
      ```

    - **[airblade/vim-gitgutter](https://github.com/airblade/vim-gitgutter)** 는 어떤 줄이 git에서 변경되었는지를 보여준다.

    - **[bkad/CamelCaseMotion](https://github.com/bkad/CamelCaseMotion)** 단어사이를 넘나들 수 있는 기능을 제공해준다.

    - [vasconcelloslf/vim-foldfocus](https://github.com/vasconcelloslf/vim-foldfocus) 특정 Fold 부분만 접어서 볼 수 있도록 해준다.

    - **[terryma/vim-multiple-cursors](https://github.com/terryma/vim-multiple-cursors)** 원하는 문자열을 쉽게 선택해서 치환할 수 있는 기능을 제공해준다.

    - [terryma/vim-expand-region](https://github.com/terryma/vim-expand-region) 선택영역을 브라켓단위로 더 넓혀준다.

    - [tpope/vim-eunuch](https://github.com/tpope/vim-eunuch) Unix명령을 지원해준다 `:SudoWrite` 가 완소.

    - **[osyo-manga/vim-anzu](https://github.com/osyo-manga/vim-anzu)** 검색시 전체 m개 중 n번째인지 알려준다.

    - **[kassio/neoterm](https://github.com/kassio/neoterm)** Vim안에 Terminal을 사용할 수 있도록 해준다. `:T zsh`

    - **[nathanaelkane/vim-indent-guides](https://github.com/nathanaelkane/vim-indent-guides)** Indent를 잘 쪼개서 알려준다!

    - **[tweekmonster/local-indent.vim](https://github.com/tweekmonster/local-indent.vim)** 그 Indent 중 어디에 너가 있는지 알려준다! Scope를 판단할 수 있다.

    - [vim-airline/vim-airline](https://github.com/vim-airline/vim-airline) Vim에 상태바를 띄워준다. (추가적인 font설치가 필요하다.)

    - [kristijanhusak/vim-hybrid-material](https://github.com/kristijanhusak/vim-hybrid-material) Vim에서 쓸 수 있는 Material 테마.

    - [ryanoasis/vim-devicons](https://github.com/ryanoasis/vim-devicons) Nerdtree에 아이콘을 보여준다.

    - **[zhaocai/GoldenView.Vim](https://github.com/zhaocai/GoldenView.Vim)** 황금비에 맞춰서 분할창을 만들어주고 전환할 수 있도록 해준다.

    너무 많이 쓰는 것 아닌가 싶기도 한데, 나는 딱 최소한이라고 생각하고 씁니다.

- Markdown Editor: [Mou](http://25.io/mou/)Ⓒ / **[MacDown](http://macdown.uranusjr.com/)**Ⓒ / **[Typora](https://www.typora.io/)**Ⓒ

  - 마크다운 에디터를 따로 쓰는 편인데, 이 글을 쓰는 중에 Typora가 발표되서 지금 그걸로 작성하는데 꽤 편하다!

### Applications

- 개발
  - **[iTerm2](https://www.iterm2.com)**Ⓒ : Mac에서 주로 쓰는 Terminal
  - **[Filezilla](https://filezilla-project.org)**Ⓒ / [CyberDuck](https://cyberduck.io/)ⒶⒸ : FTP에 접속하기 위한 프로그램이고 나는 filezilla에 익숙해져있어서 이걸 주로 사용한다. cyberduck은 예뻐서 넣어놓는 편.
  - **[LaunchRocket](https://github.com/jimbojsb/launchrocket)**Ⓒ : System Preferences에서 Homebrew를 통해서 설치된 OS X 의 서비스 (launchd)를 관리할 수 있도록 해줍니다. (강추!!!!! 링크에서 스크린샷을 꼭 보세요!!!)
  - **[ngrok](https://ngrok.com/)**Ⓒ : 사설망에서 개발을 진행중일 때, 사설망 밖으로 포트를 열어주어야 할 경우 사용하는 외부서비스입니다.
  - **[Pusher](https://github.com/noodlewerk/NWPusher)**Ⓒ : 애플 푸시 서비스 (APNS)를 테스트할 때 씁니다.
  - **[GitKraken](https://www.gitkraken.com/)**Ⓒ : Git Branch를 예쁘게 보고싶을 때 씁니다.
  - **PyCharm**Ⓒ$ : JetBrains사의 Python 개발 IDE 입니다. 저는 JetBrains사를 신뢰합니다 <3
    - 학생라이센스를 지원해줘요.
  - [Fabric](https://fabrics.io) : Xcode과 붙어서 개발 Pipeline을 훌륭하게 해주는 Twitter의 SDK Platform입니다.
  - ~~[vagrant](https://www.vagrantup.com) / vagrant-manager Ⓒ~~ : Virtual Machine을 관리해주는 툴입니다. [VirtualBox](https://www.virtualbox.org/)를 쓰신다면 추천합니다만, 저는 개인적으로 docker로 다 해결하는걸 좋아합니다.
- 추가적인 보안
  - Indicator:
    - **[IP-in-menu-bar](https://www.monkeybreadsoftware.de/Software/IPinmenubar.shtml)**Ⓒ : 메뉴바에 IP를 띄워줍니다.
      - 가난한자의 [**iStat Menus**](https://bjango.com/mac/istatmenus)Ⓒ$
    - [**Security-Growler**](https://github.com/pirate/security-growler)Ⓒ : 보안 메세지가 생길 경우 Notification Center로 알려줍니다.
    - [**Little Snitch**](https://www.obdev.at/products/littlesnitch)Ⓒ$ : 누군가가 Network를 통해 접근을 시도할 경우, 이를 승인/거절 할 수 있는 팝업을 띄워줍니다.
    - [**Micro Snitch**](https://www.obdev.at/products/microsnitch)Ⓒ$ : 누군가가 Mic나 WebCam을 쓸 경우, 이를 경고로 알려줍니다.
  - Harden:
    - [**DNSCrypt**](https://dnscrypt.org/)Ⓒ : DNS요청을 암호화해서 처리해줍니다.
    - [Vallum](vallumfirewall.com)Ⓒ$ : OS X Application Firewall
    - [Murus](murusfirewall.com)Ⓒ$ : OS X Network Firewall
      - Murus Lite는 Free
    - [knockknock](https://objective-see.com/products/knockknock.html)Ⓒ
      - `"Who's there?" See what's persistently installed on your Mac.`
    - [blockblock](https://objective-see.com/products/blockblock.html)Ⓒ
      - `"please alert me anytime, anything is persistently installed"`
    - [taskexplorer](https://objective-see.com/products/taskexplorer.html)Ⓒ
      - `Explore all the tasks (processes) running on your Mac with TaskExplorer`
    - [ostiarius](https://objective-see.com/products/ostiarius.html)Ⓒ
      - ` is tool for El Capitan that blocks unsigned internet binaries from executing`
  - [keybase](https://keybase.io)Ⓒ* : 궁금하시면 https://keybase.io/minhoryang 여기에 들어와보세요.
    - 초대장 필요하신 분 연락주세요.
  - [munki](https://github.com/munki/munki)Ⓒ : OS X 용 사설 패키지 관리자와 App Store를 만들 수 있습니다. 많은 수의 맥을 관리하는 사람들에게 추천합니다!
- 생산성
  - Pomodoro Time
  - [**Bandizip-X**](http://www.bandisoft.co.kr/bandizip/x/)Ⓐ$
  - **Spectacle**
  - **cloud**
  - **macs-fan-control**
  - **flux**
  - **handbrake**
  - Irvue
  - keycastr
  - aerial
  - MovistⒶ$
  - Slack
- QuickLook
  - qlcolorcode
    qlimagesize
    qlstephen
    quicklook-json
  - **betterzipql**
  - cert-quicklook

### Command Line Tools

- 개발
  - [anyenv](https://github.com/riywo/anyenv):
    - [pyenv](https://github.com/yyuu/pyenv)

      [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)
      [pyenv-update](https://github.com/yyuu/pyenv-update)
      [pyenv-implict](https://github.com/concordusapps/pyenv-implict)

    - [ndenv](https://github.com/riywo/ndenv)
  - XCode + Swift:
    - [fastlane](https://fastlane.tools/)Ⓑ
    - [synx](https://github.com/venmo/synx)Ⓑ
    - [carthage](https://github.com/Carthage/Carthage)Ⓑ
    - [swiftlint](https://github.com/realm/SwiftLint)Ⓑ
    - [xctool](https://github.com/facebook/xctool)Ⓑ
    - [codeclimate](https://github.com/codeclimate/codeclimate)Ⓑ
  - 환경:
    - [docker]()Ⓑ
      [docker-machine]()Ⓑ
      [docker-compose]()Ⓑ
      - 이 세개를 [**Docker for Mac**]() 으로 설치하는게 더 좋다!
    - docker-rsync
    - **git**Ⓑ
      **git-lfs**Ⓑ
    - **vim**Ⓑ
- 보안
  - upgrade:
    - **openssh**Ⓑ
    - **openssl**Ⓑ
    - curlⒷ
    - **wget**Ⓑ
  - 개발을 위해:
    - **[mobile-shell](https://mosh.mit.edu/)**Ⓑ
    - [nload](http://www.roland-riegel.de/nload/)
    - **nmap**Ⓑ
    - mitmproxyⒷ
  - battle:
    - ipfsⒷ
    - torsocksⒷ
    - gpg-agentⒷ
- 생산성
  - treeⒷ
  - highlightⒷ
  - gistⒷ
  - jqⒷ
  - **htop-osx**Ⓑ
  - **[thefuck](https://github.com/nvbn/thefuck)**
  - **[trash](http://hasseg.org/trash/)**
  - **zsh**Ⓑ
  - **tmux**Ⓑ
  - **[reattach-to-user-namespace](https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard)**Ⓑ
  - https://github.com/aykamko/tagⒷ
    - https://github.com/ggreer/the_silver_searcher (ag)
  - linux-compatibility:
    - coreutils
    - findutils
    - grep
    - **gnu-which**
    - **gnu-sed**
    - **gnu-indent**
    - **gnu-time**
    - **gnu-tar**
    - moreutils
- ~/bin/
  - consul
  - scope
  - boom
  - caddy
  - ntfy



--- TO BE CONTINUE~~~
