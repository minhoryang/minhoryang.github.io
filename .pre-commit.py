#!/usr/bin/env python
# brought to you by https://github.com/sebdah/git-pylint-commit-hook/blob/master/git_pylint_commit_hook/commit_hook.py

import collections
import subprocess
import re


ExecutionResult = collections.namedtuple(
    'ExecutionResult',
    'status, stdout, stderr',
)


def _futurize_str(obj):
    if isinstance(obj, bytes):
        obj = obj.decode('utf-8')
    return obj


def _execute(cmd):
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    status = process.poll()
    return ExecutionResult(status, stdout, stderr)


def _current_commit():
    if _execute('git rev-parse --verify HEAD'.split()).status:
        return '4b825dc642cb6eb9a060e54bf8d69288fbee4904'
    else:
        return 'HEAD'


def _get_list_of_committed_files():
    """ Returns a list of files about to be commited. """
    files = []
    # pylint: disable=E1103
    diff_index_cmd = 'git diff-index --cached %s' % _current_commit()
    output = subprocess.check_output(
        diff_index_cmd.split()
    )
    for result in _futurize_str(output).split('\n'):
        if result != '':
            result = result.split()
            if result[4] in ['A', 'M']:
                files.append(result[5])

    return files


def _is_markdown_file(filename):
    for ext in (
        '.md',
        '.markdown',
    ):
        if filename.endswith(ext):
            return True
    return False


def _replace_url_string(content):
    after, changes = re.subn(
        r'http://0.0.0.0:8000/',
        r'https://minhoryang.github.io/',
        content)
    return after if changes else None


def _git_add(filename):
    _execute(('git add %s' % (filename,)).split())


if __name__ == "__main__":
    for filename in _get_list_of_committed_files():
        try:
            if _is_markdown_file(filename):
                replaced = None
                with open(filename, 'r') as fp:
                    replaced = _replace_url_string(fp.read())
                if replaced:
                    with open(filename, 'w') as fp:
                        fp.write(replaced)
                    _git_add(filename)
        except IOError:
            pass  # XXX(Expected) : Maybe deleted by `git rm`.
