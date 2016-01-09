<!-- 
.. title: AWS EC2 Instance Creation for Python-Dev
.. slug: aws-ec2-instance-creation-for-python-dev
.. date: 2016-01-09 12:14:53 UTC+09:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

# Instance 생성
1. **AWS** 사이트에 접속한다
2. **Tokyo**에 접속된 것을 확인한다. 아니면 **Tokyo**로 바꿔준다.
3. **EC2**를 누른다
4. **Instances 탭에서 자신의 Name을 가진 Instance가 있는지 확인한다.**
5. 없으면 생성시작 **`Launch Instance`**
6. 운영체제는 **`Ubuntu Server 14.04 LTS (HVM), SSD Volume Type`**을 선택.
7. Instance 타입(사양)은 **`t2.micro`**를 선택.
8. Details 부분과 Storage 부분은 다음버튼으로 넘어가고
9. **`Tag Instance` 부분의 `Name`에 자신의 이름을 기재한다.**
10. **`Security Group`** 항목에 **`Security Group Name`**을 자신의 이름을 이용해 적절히 바꾸고, **`Add Rule`을 통해 `5000`포트를 `Anywhere`로 이용할 수 있도록 설정**한다.
11. `Launch`
12. **`Key Pair`는 기존에 생성해 둔 파일을 사용하던지, 여기서 새로 만들어서 사용한다.**

# Instance에 Pyenv+Python 설정
1. 다운 받은 **Key Pair (.pem) 파일**과 EC2의 Instances탭에서 보이는 **Public DNS**를 이용하여 Instance에 접속!

	```bash
	ssh -i DOWNLOADED.pem ubuntu@MY_PUBLIC_DNS
	```
2. 다양한 Python Version을 문제없이 사용하기 위한 Pyenv 설치:

	[pyenv-installer](https://github.com/yyuu/pyenv-installer)의 명령줄 사용
	
	```bash
	sudo apt-get update
	sudo apt-get install git
	curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
	```
	
	설치 후  아래의 부분을 `~/.bash_profile` 에 추가
	
	```bash
	export PATH="/home/ubuntu/.pyenv/bin:$PATH"
	eval "$(pyenv init -)"
	eval "$(pyenv virtualenv-init -)"
	```
	~/.bash_profile 실행
	
	```bash
	. ~/.bash_profile
	```
3. Pyenv를 통해 Python 버전 설치!

	- [파이선을 빌드하기 위한 패키지들을 설치](https://github.com/yyuu/pyenv/wiki/Common-build-problems)
	
		```bash
		sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev
		```
	- 원하는 Python 버전 설치
		
		```bash
		pyenv install 3.5.1
		```
	- 프로젝트 별 패키지 분리를 위해 `Virtualenv`를 적용

		```bash
		pyenv virtualenv 3.5.1 3.5.1-flask
		```
	- 원하는 프로젝트 폴더에서 특정 Python 환경을 사용하도록 설정

		```bash
		mkdir MY_SWEET_NEW_PROJECT_HOME
		pyenv local 3.5.1-flask
		```
	- 필요한 Python 패키지 설치

		```bash
		pip install flask
		```

4. [부록] Python 개발을 위한 **`~/.vimrc`** 간단 설정

	```vim
	syntax on
	filetype indent plugin on
	set tabstop=8
	set expandtab
	set shiftwidth=4
	set softtabstop=4
	```

(이 글은 선린인터넷고 학생들의 Flask 교육을 위해 쓰여졌습니다.)