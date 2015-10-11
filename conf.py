from __future__ import unicode_literals
import time

BLOG_AUTHOR = {"ko": "양민호", "en": "Min-Ho Ryang"}
BLOG_TITLE = "minhoryang.github.io"
SITE_URL = "https://minhoryang.github.io/"
BLOG_EMAIL = "minho.ryang+github@gmail.com"
BLOG_DESCRIPTION = "knock knock knock, is anybody there?"

DEFAULT_LANG = "ko"
TRANSLATIONS = {
    DEFAULT_LANG: "./ko",
    "en": "./en",
}
TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"
SHOW_UNTRANSLATED_POSTS = False
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/ko/", "Korean", "icon-home"),
        ("/en/", "English", "icon-globe"),
        ("/ko/archive.html", "저장소", 'icon-folder-open-alt'),
        ("/ko/categories/", "태그", 'icon-tags'),
        ("https://github.com/minhoryang/minhoryang.github.com/issues#ASK_ME_ANYTHING_HERE", "Ask Me Anything", "icon-question-sign"),
        ("https://facebook.com/minhoryang", "Facebook", "icon-facebook-sign"),
        ("https://github.com/minhoryang", "Github", "icon-github"),
    ),
    "en": (
        ("/en/", "English", "icon-home"),
        ("/ko/", "Korean", "icon-globe"),
        ("/en/archive.html", "Archive", "icon-folder-open-alt"),
        ("/en/categories/", "Tags", "icon-tags"),
        ("https://github.com/minhoryang/minhoryang.github.com/issues#ASK_ME_ANYTHING_HERE", "Ask Me Anything", "icon-question-sign"),
        ("https://facebook.com/minhoryang", "Facebook", "icon-facebook-sign"),
        ("https://github.com/minhoryang", "Github", "icon-github"),
    ),
}

THEME = "zen-jinja"

POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
)
PAGES = (
    ("stories/*.rst", "stories", "story.tmpl"),
    ("stories/*.txt", "stories", "story.tmpl"),
)

TIMEZONE = "Asia/Seoul"

COMPILERS = {
    "rest": ('.rst', '.txt'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "html": ('.html', '.htm'),
}

SHOW_BLOG_TITLE = False
WRITE_TAG_CLOUD = True
POSTS_SECTIONS = True
CATEGORY_ALLOW_HIERARCHIES = False
CATEGORY_OUTPUT_FLAT_HIERARCHY = False
# CATEGORY_PAGES_ARE_INDEXES = False
HIDDEN_CATEGORIES = []
HIDDEN_AUTHORS = ['Guest']
# INDEX_PATH = ""

REDIRECTIONS = []

# Presets of commands to execute to deploy. Can be anything, for
# example, you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola plugin -i ping`).  Or run `nikola check -l`.
# You may also want to use github_deploy (see below).
# You can define multiple presets and specify them as arguments
# to `nikola deploy`.  If no arguments are specified, a preset
# named `default` will be executed.  You can use as many presets
# in a `nikola deploy` command as you like.
DEPLOY_COMMANDS = {
    'default': [
        "git push origin source",
        "git subtree push --prefix output origin master",
    ]
}

# For user.github.io OR organization.github.io pages, the DEPLOY branch
# MUST be 'master', and 'gh-pages' for other repositories.
#GITHUB_SOURCE_BRANCH = 'master'
#GITHUB_DEPLOY_BRANCH = 'gh-pages'

# The name of the remote where you wish to push to, using github_deploy.
#GITHUB_REMOTE_NAME = 'origin'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, only .php files uses filters to inject PHP into
# Nikola’s templates. All other filters must be enabled through FILTERS.
#
# Many filters are shipped with Nikola. A list is available in the manual:
# <https://getnikola.com/handbook.html#post-processing-filters>
#
# from nikola import filters
# FILTERS = {
#    ".html": [filters.typogrify],
#    ".js": [filters.closure_compiler],
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

IMAGE_FOLDERS = {'images': 'images'}

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of:
# algol
# algol_nu
# arduino
# autumn
# borland
# bw
# colorful
# default
# emacs
# friendly
# fruity
# igor
# lovelace
# manni
# monokai
# murphy
# native
# paraiso_dark
# paraiso_light
# pastie
# perldoc
# rrt
# tango
# trac
# vim
# vs
# xcode
# This list MAY be incomplete since pygments adds styles every now and then.
# CODE_COLOR_SCHEME = 'default'

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONFIG_SUBTHEME = 'sky'
# You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions
# between the slides
# THEME_REVEAL_CONFIG_TRANSITION = 'cube'
# You can also use: page/concave/linear/none/default

# FAVICONS contains (name, file, size) tuples.
# Used to create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# FAVICONS = (
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# )

# Show teasers (instead of full posts) in indexes? Defaults to False.
# INDEX_TEASERS = False

# HTML fragments with the Read more... links.
# The following tags exist and are replaced for you:
# {link}                        A link to the full post page.
# {read_more}                   The string “Read more” in the current language.
# {reading_time}                An estimate of how long it will take to read the post.
# {remaining_reading_time}      An estimate of how long it will take to read the post, sans the teaser.
# {min_remaining_read}          The string “{remaining_reading_time} min remaining to read” in the current language.
# {paragraph_count}             The amount of paragraphs in the post.
# {remaining_paragraph_count}   The amount of paragraphs in the post, sans the teaser.
# {{                            A literal { (U+007B LEFT CURLY BRACKET)
# }}                            A literal } (U+007D RIGHT CURLY BRACKET)

# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = ""
# I recommend using the Creative Commons' wizard:
# https://creativecommons.org/choose/
# LICENSE = """
# <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
# <img alt="Creative Commons License BY-NC-SA"
# style="border-width:0; margin-bottom:12px;"
# src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="https://getnikola.com" rel="nofollow">Nikola</a>         {license}'

CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

COMMENT_SYSTEM = ""
COMMENT_SYSTEM_ID = ""

ANNOTATIONS = False

# Create index.html for page (story) folders?
# WARNING: if a page would conflict with the index file (usually
#          caused by setting slug to `index`), the STORY_INDEX
#          will not be generated for that directory.
# STORY_INDEX = False
STRIP_INDEXES = True

SITEMAP_INCLUDE_FILELESS_DIRS = False

# List of files relative to the server root (!) that will be asked to be excluded
# from indexing and other robotic spidering. * is supported. Will only be effective
# if SITE_URL points to server root. The list is used to exclude resources from
# /robots.txt and /sitemap.xml, and to inform search engines about /sitemapindex.xml.
# ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

# Instead of putting files in <slug>.html, put them in <slug>/index.html.
# No web server configuration is required. Also enables STRIP_INDEXES.
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata.
PRETTY_URLS = True

MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite', 'extra']

SHOW_SOURCELINK = False
COPY_SOURCES = False

# INDEX_DISPLAY_POST_COUNT = 10

GENERATE_RSS = False

# USE_CDN = False
# USE_CDN_WARNING = True

# EXTRA_HEAD_DATA = ""
# BODY_END = ""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

UNSLUGIFY_TITLES = True
# ADDITIONAL_METADATA = {}
# USE_OPEN_GRAPH = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]
# EXTRA_PLUGINS_DIRS = []

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
# DEMOTE_HEADERS = 1

# If you don’t like slugified file names ([a-z0-9] and a literal dash),
# and would prefer to use all the characters your file system allows.
# USE WITH CARE!  This is also not guaranteed to be perfect, and may
# sometimes crash Nikola, your web server, or eat your cat.
# USE_SLUGIFY = True

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

# Add functions here and they will be called with template
# GLOBAL_CONTEXT as parameter when the template is about to be
# rendered
GLOBAL_CONTEXT_FILLER = []
