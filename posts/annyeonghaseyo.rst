.. title: 안녕하세요
.. slug: annyeonghaseyo
.. date: 2015-10-11 19:04:37 UTC+09:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

내가 잘 할 수 있겠지? 에구구구.


* 새 환경으로 옮긴다면:

        Initialize the environment:

                $ pyenv install 3.4.2

                $ pyenv virtualenv 3.4.2 3.4.2-blog

                $ pyenv local 3.4.2-blog

                $ pip install --upgrade -r requirement.txt
                
                $ pip install --upgrade -r requirement-dev.txt  # for live-reloading.

        After branching 'source' and 'master',

                $ git push origin `git subtree split --prefix output master`:master --force 

        new post:

                $ nikola new_post -f misaka  # misaka: Markdown Module

                $ nikola auto

                $ nikola deploy
