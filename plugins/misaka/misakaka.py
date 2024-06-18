# -*- coding: utf-8 -*-

# Copyright © 2013-2014 Chris Lee and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Implementation of compile_html based on misaka."""

from __future__ import unicode_literals

import codecs
import os

import misaka
try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict  # NOQA

    gist_extension = None
    podcast_extension = None

from nikola import shortcodes as sc
from nikola.plugin_categories import PageCompiler
from nikola.utils import makedirs, req_missing, write_metadata


# XXX(minhoryang): Code Highlighter!
def CodeHighlighter(data, extensions):
    # XXX: COPIED from http://misaka.61924.nl/
    import houdini as h
    import misaka
    from pygments import highlight
    from pygments.formatters import HtmlFormatter, ClassNotFound
    from pygments.lexers import get_lexer_by_name

    class HighlighterRenderer(misaka.HtmlRenderer):
        def blockcode(self, text, lang):
            try:
                lexer = get_lexer_by_name(lang, stripall=True)
            except ClassNotFound:
                lexer = None

            if lexer:
                formatter = HtmlFormatter()
                return highlight(text, lexer, formatter)
            # default
            return '\n<pre><code>{}</code></pre>\n'.format(
                                h.escape_html(text.strip()))

    renderer = HighlighterRenderer()
    # XXX: END
    md = misaka.Markdown(renderer, extensions=extensions)
    return md(data)


class CompileMisaka(PageCompiler):
    """Compile Misaka into HTML."""

    name = "misaka"
    demote_headers = True

    def __init__(self, *args, **kwargs):
        super(CompileMisaka, self).__init__(*args, **kwargs)
        if misaka is not None:
            self.ext = misaka.EXT_FENCED_CODE | misaka.EXT_STRIKETHROUGH | \
                misaka.EXT_AUTOLINK | misaka.EXT_NO_INTRA_EMPHASIS

    def compile_string(self, data, source_path=None, is_two_file=True, post=None, lang=None):
        """Compile the source file into HTML strings (with shortcode support).

        Returns a tuple of at least two elements: HTML string [0] and shortcode dependencies [last].
        """
        if misaka is None:
            req_missing(['misaka'], 'build this site (compile with misaka)')
        if not is_two_file:
            _, data = self.split_metadata(data, post, lang)
        new_data, shortcodes = sc.extract_shortcodes(data)
        # XXX(minhoryang): before CodeHighlighter
        # output = misaka.html(new_data, extensions=self.ext)
        output = CodeHighlighter(new_data, extensions=self.ext)
        output, shortcode_deps = self.site.apply_shortcodes_uuid(output, shortcodes, filename=source_path, extra_context={'post': post})
        return output, shortcode_deps

    def compile(self, source, dest, is_two_file=True, post=None, lang=None):
        """Compile the source file into HTML and save as dest."""
        if misaka is None:
            req_missing(['misaka'], 'build this site (compile with misaka)')
        makedirs(os.path.dirname(dest))
        with codecs.open(dest, "w+", "utf8") as out_file:
            with codecs.open(source, "r", "utf8") as in_file:
                data = in_file.read()
            output, shortcode_deps = self.compile_string(data, source, is_two_file, post, lang)
            out_file.write(output)
        if post is None:
            if shortcode_deps:
                self.logger.error(
                    "Cannot save dependencies for post {0} (post unknown)",
                    source)
        else:
            post._depfile[dest] += shortcode_deps

    def create_post(self, path, content=None, onefile=False, is_page=False, **kw):
        """Create post file with optional metadata."""
        metadata = OrderedDict()
        metadata.update(self.default_metadata)
        metadata.update(kw)
        makedirs(os.path.dirname(path))
        if not content.endswith('\n'):
            content += '\n'
        with codecs.open(path, "wb+", "utf8") as fd:
            if onefile:
                fd.write('<!-- \n')
                fd.write(write_metadata(metadata))
                fd.write('-->\n\n')
            fd.write(content)
