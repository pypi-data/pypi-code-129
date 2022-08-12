#!/usr/bin/env python3
from __future__ import annotations
import argparse
import datetime
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import pathlib

import pydndc

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--gui', action='store_true')
    parser.add_argument('--open-only', action='store_true', help='Only open the journal html in a browser')
    args = parser.parse_args()
    return run(**vars(args))

def openit(OPEN:str|None, JOURNALHTML:str) -> None:
    if not OPEN: return
    if sys.platform == 'win32':
        cmd = OPEN+' '+pathlib.Path(JOURNALHTML).as_uri()
        os.system(cmd)
    else:
        subprocess.check_call([OPEN, JOURNALHTML])


def run(gui:bool, open_only:bool) -> int:
    GIT = shutil.which('git')
    if not GIT:
        print("git not found, aborting", file=sys.stderr)
        return 1
    if sys.platform == 'darwin':
        OPEN = shutil.which('open')
        GUI = '/Applications/MacVim.app/Contents/bin/mvim', '-f', '-c', 'au VimLeave * maca hide:'
        JOURNALFOLDER = os.path.expanduser('~/Documents/Journals')
    elif sys.platform == 'linux':
        OPEN = shutil.which('xdg-open')
        GUI = shutil.which('gvim'),  '-f'
        JOURNALFOLDER = os.path.expanduser('~/Journals')
    else:
        assert sys.platform == 'win32'
        OPEN = 'start'
        GUI = shutil.which('gvim'),  '-f'
        import ctypes.wintypes
        CSIDL_PERSONAL = 5       # My Documents
        SHGFP_TYPE_CURRENT = 0   # Get current, not default value

        buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
        JOURNALFOLDER = os.path.join(buf.value, 'Journals')
    if gui and not GUI[0]:
        print('gvim not found, aborting', file=sys.stderr)
        return 1


    NOW = datetime.datetime.now()
    LASTMONTH = NOW.replace(day=1) - datetime.timedelta(days=1)
    NEXTMONTH = NOW.replace(day=28) + datetime.timedelta(days=7)

    YEARMONTH = NOW.strftime('%Y-%m')
    JOURNALFILE = os.path.join(JOURNALFOLDER, YEARMONTH) + '.dnd'
    JOURNALHTML = os.path.join(JOURNALFOLDER, YEARMONTH) + '.html'
    PREVIOUSFILE = LASTMONTH.strftime('%Y-%m') + '.html'
    NEXTFILE = NEXTMONTH.strftime('%Y-%m') + '.html'
    if open_only:
        openit(OPEN, JOURNALHTML)
        return 0

    if not os.path.isdir(JOURNALFOLDER):
        os.makedirs(JOURNALFOLDER, exist_ok=True)
        subprocess.check_call([GIT, 'init'], cwd=JOURNALFOLDER)


    F = pydndc.Flags
    ctx = pydndc.Context(flags=F.DONT_INLINE_IMAGES)
    ctx.logger = pydndc.stderr_logger
    if os.path.isfile(JOURNALFILE):
        ctx.root.parse_file(JOURNALFILE)
    else:
        ctx.root.parse(textwrap.dedent('''
        ::nav #id(toc)
        ::css
          * {
              box-sizing: border-box;
          }
          body {
              display: grid;
              grid-template-columns: 12em auto;
              grid-template-rows: max-content auto;
              grid-column-gap: 4em;
              height: 100vh;
              margin: 0;
          }
          #top {
              grid-column: 1/3;
              grid-row: 1;
              padding: 8px;
          }
          #content {
              grid-column: 2;
              grid-row: 2;
              overflow-y: auto;
              padding: 8px;
          }
          #toc {
              grid-column: 1;
              grid-row: 2;
              overflow-y: auto;
              padding: 8px;
              max-width: 12em;
              overflow-x: hidden;
          }
          .day {
              width: 40em;
              padding-left: 4em;
          }
          #top {
              display: flex;
              justify-content: space-between;
          }

          @media only screen and (max-width: 800px){
            #toc {
              display: none;
            }
            body {
              grid-template-columns: 0em auto;
              grid-column-gap: 0em;
              height: auto;
            }
            .day {
                width: auto;
                padding: 1em;
            }
          }
          /*endcss*/
        ::div #id(top)
          [Last Month]
          ''' f'''
          {NOW.strftime("%B %Y")}::title
          [Next Month]
        ::div #id(content)
        ::links
            Last Month = {PREVIOUSFILE}
            Next Month = {NEXTFILE}
        '''
        ))
    content = ctx.node_by_id('content')
    assert content is not None
    today = NOW.strftime('%A %B %d')
    today_node = ctx.node_by_id(today)
    if today_node is None:
        today_node = content.make_child(pydndc.NodeType.MD, today)
        today_node.classes.add('day')
    else:
        today_node.make_child(pydndc.NodeType.PARA).append_child('<hr>')
    today_node.make_child(pydndc.NodeType.PARA).append_child(NOW.strftime('<i>written at %I:%M%p</i>').lower())

    fd, tmp = tempfile.mkstemp(suffix='.dnd', text=True)
    os.close(fd)
    command = [*GUI, tmp] if gui else ['vim', tmp]
    subprocess.check_call(command)
    try:
        with open(tmp) as fp:
            text = fp.read()
    except FileNotFoundError:
        print('Not found, aborting.', file=sys.stderr)
        return 1
    if not text.strip():
        print('Aborting due to empty input file.', file=sys.stderr)
        return 1
    os.unlink(tmp)
    today_node.parse(text)
    output = ctx.format_tree().rstrip()
    with open(JOURNALFILE, 'w') as fp:
        print(output, file=fp)
    ctx.resolve_imports()
    ctx.execute_js()
    ctx.resolve_links()
    ctx.build_toc()
    html = ctx.render()

    with open(JOURNALHTML, 'w') as fp:
        print(html.rstrip(), file=fp)

    openit(OPEN, JOURNALHTML)
    subprocess.check_call([GIT, 'add', JOURNALFILE], cwd=JOURNALFOLDER)
    subprocess.check_call([GIT, 'commit', '--allow-empty-message', '-q', '-m', ''], cwd=JOURNALFOLDER)
    return 0

if __name__ == '__main__':
    ret = main()
    sys.exit(ret)
