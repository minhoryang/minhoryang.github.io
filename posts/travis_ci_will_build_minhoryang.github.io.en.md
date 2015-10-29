<!-- 
.. title: Travis CI will build minhoryang.github.io
.. slug: travis-ci-will-build-minhoryang-github-io
.. date: 2015-10-29 19:28:12 UTC+09:00
.. tags:  
.. category: DesignDoc
.. link: 
.. description: 
.. type: text
-->

## Current Status
minhoryang.github.io have 3 branches: **master**, **source**, **ama**

- **master** branch has **\*.html** files for exposing by Github Pages
- **source** branch has **\*.md** manuscripts and [Nikola]()'s **conf.py**
- ignores **ama** branch, it just has README.md only

With `nikola build` and `nikola deploy`, output/* at the source branch pushes to master branch.

Dependencies are well preserved at requirements.txt.
External dependencies are included on **source** branch's `plugins/` and `themes/` directory.

## I want
- to update my blogs at Github web page
- even with iPhone

## Let's resolve it.

### Conditionally Selecting the build-wanted commits by commit msg
At the client side: iPhone Github client may not support pre-post hook.

At the server side: post-receive hook will deny the commit which not fit the commit message rules, but Github doesn't supported it but supported the web hook.
but web hook can't reject the commit.

[Travis CI can skip the build.](http://docs.travis-ci.com/user/customizing-the-build/#Skipping-a-build)
but by [ci skip] will be located with every my normal environment pushes.

From now on, I need to write `[ci skip]` at every commits when I pushed with usual workspaces.

(Really?! `# TODO : What a useless byte!`)

I really want to bypass it. but Travis ci will triggering only by push/pull requests.

(TO BE CONTINUE)
