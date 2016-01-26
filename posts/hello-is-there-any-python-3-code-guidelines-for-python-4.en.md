<!-- 
.. title: Hello Is there any Python 3.5+ code guidelines for Python 4
.. slug: hello-is-there-any-python-3-code-guidelines-for-python-4
.. date: 2016-01-27 00:20:53 UTC+09:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

## tl;dr
0. Write 3 only
1. It will be broken at 2.7
2. then Duct-taping it

## [STOP WRITING PYTHON 4 INCOMPATIBLE CODE](http://astrofrog.github.io/blog/2016/01/12/stop-writing-python-4-incompatible-code/)
Just before I need to write some python project, I saw this at [Hacker News](https://news.ycombinator.com/item?id=10888061). It shows the reason why shouldn't use Six library. But I couldn't find guidelines for Python 4. So I started to write it.

### [Six: Python 2 and 3 Compatibility Library](https://pythonhosted.org/six/)
```
Six provides simple utilities for wrapping over differences between Python 2 and Python 3. It is intended to support codebases that work on both Python 2 and 3 without modification. six consists of only one Python file, so it is painless to copy into a project.
The name, “six”, comes from the fact that 2*3 equals 6.
```

## Now, we need `TwentyFour`.
### Really? why not `Twelve`?
I hope that there are some people who wanna throw Python 2 away. (me too) In my case, particular meaningful libraries block this. (such as Twisted).

### So, check first
Some helpful sites for finding a reason to use Python 2.

- https://caniusepython3.com/
- https://python3wos.appspot.com/
- http://py3readiness.org/

#### I don't always use Python 2, but when I do, only 2.7.11+

## Python 4?
- [Why Python 4.0 won't be like Python 3.0](http://www.curiousefficiency.org/posts/2014/08/python-4000.html)
`My current expectation is that Python 4.0 will merely be "the release that comes after Python 3.9". That's it.`

### So, code for Python 3.5+ first
### Break it at Python 2.7.11+
### Fix it with
- flake8
- py.test
- tox
- travis CI

## Then, What differences exist between Python 3.5+ and Python 2.7.11+?
- New features: https://docs.python.org/dev/whatsnew/index.html
	- 3.5: typing, ...
	- 3.4: asyncio, enum, ...
	- 3.3: u'unicode' (again), venv, ...
	- 3.2: concurrent.futures, PEP-3333, ...
- [The key differences between Python 2.7.x and Python 3.x with examples](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html)

### For 3 users, just follow those rules, then It will be okay:
- Manage Python Versions with [pyenv](https://github.com/yyuu/pyenv)
- Manage Python Project Environments with [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)
- [Shebang](http://stackoverflow.com/questions/17846908/proper-shebang-for-python-script): `#!/usr/bin/env python`
- `print()` as a function.
- `u'Everything'` and `b''`
- `class Base(object):` (object)
- `except Exception as e:` (as)
- `2/3.0` (think your C/C++ experiences)
- Dictionary Iteration: [Use .items(), .keys(), .values()](https://docs.python.org/dev/whatsnew/2.7.html#pep-3106-dictionary-views)
- String Manipulation: [Use .format()](https://docs.python.org/dev/library/stdtypes.html#str.format)
- Typing (3.5+): [Comment it](https://www.python.org/dev/peps/pep-0484/#suggested-syntax-for-python-2-7-and-straddling-code)
- Use latest 3rd-party packages
- Python 2 only requirements.txt?!
	- [Future](https://pypi.python.org/pypi/future)
	- Enum (3.4+): [enum34 at 2.7](https://pypi.python.org/pypi/enum34)
	- what about requirements.txt?! do we divide it?

### When additional problems happened to you, check those:
- [Porting Python 2 Code to Python 3](https://docs.python.org/dev/howto/pyporting.html)
- [Cheat Sheet: Writing Python 2-3 compatible code](http://python-future.org/compatible_idioms.html)
- [Using Python 2-only dependencies on Python 3](http://python-future.org/translation.html)
- [Nine: Python 2 / 3 compatibility, like six, but favouring Python 3](https://pypi.python.org/pypi/nine)

##### More links
- [Python 3 is killing Python](http://blog.thezerobit.com/2014/05/25/python-3-is-killing-python.html) and [HN comments](https://news.ycombinator.com/item?id=7799524)
- [Variable sixpy3 is time bomb](https://bitbucket.org/gutworth/six/issues/22/variable-sixpy3-is-time-bomb)

#### DISCLAIMER:
Maybe it's not, but I'll update those asap.
So, please ping to me (twt@angryonhim).
Thanks.


<!--
## flake8 + importorder
https://github.com/hpk42/pluggy/blob/master/.travis.yml
https://github.com/hpk42/pluggy/blob/master/tox.ini
https://github.com/spoqa/import-order/blob/master/tox.ini
https://github.com/spoqa/sqlalchemy-enum34/blob/master/.coveragerc
https://github.com/spoqa/geofront/blob/master/tox.ini
-->