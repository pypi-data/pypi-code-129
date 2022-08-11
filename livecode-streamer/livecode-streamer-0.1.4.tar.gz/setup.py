# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['livecode_streamer',
 'livecode_streamer.renderers',
 'livecode_streamer.uploaders']

package_data = \
{'': ['*']}

install_requires = \
['Pygments>=2.12.0,<3.0.0', 'keyring>=23.6.0,<24.0.0', 'watchdog>=2.1.9,<3.0.0']

extras_require = \
{'aws': ['boto3>=1.24.23,<2.0.0'],
 'azure': ['azure-storage-blob>=12.12.0,<13.0.0'],
 'git': ['dulwich>=0.20.44,<0.21.0'],
 'jupyter': ['nbformat>=5.4.0,<6.0.0', 'nbconvert>=6.5.0,<7.0.0'],
 'localhost': ['pyngrok>=5.1.0,<6.0.0']}

entry_points = \
{'console_scripts': ['livecode-streamer = livecode_streamer.stream:main']}

setup_kwargs = {
    'name': 'livecode-streamer',
    'version': '0.1.4',
    'description': 'Tool for educators running "live coding" sessions to make their source files and terminal sessions viewable as read-only webpages, so that students can refer back to off-screen commands as reference.',
    'long_description': '# livecode-streamer\n\nTool for educators running "live coding" sessions to make their source files and terminal sessions viewable as read-only webpages, so that students can refer back to off-screen commands as reference.\n\nThis project was originally developed within the context of holding [Carpentries workshops](https://carpentries.org/) to teach UNIX shells, git, Python, and R, though it should be generalizable to other programming environments and teaching contexts.\n\nFor a captioned video overview of the tool, see our [lightning talk from CarpentryCon 2022](https://www.youtube.com/watch?v=a3uJj7Eqwzg).\n\n## Usage\n\nRun the `livecode-streamer` command in a background terminal window during your lesson:\n\n```\nlivecode-streamer [options] WATCH_DIR REMOTE_URI\n```\n\n`WATCH_DIR` is a local directory containing the source files you are working on, and `REMOTE_URI` is a remote webserver to reflect those documents to. Whenever you save your source files, the script will upload HTML versions of them to the remote server. Students can view these files in their browser, and refresh the page as needed to recieve new content.\n\nTo stream a shell session, you must use a terminal emulator that supports automatic logging to HTML. This repository contains plugins to do so with [Terminator](https://github.com/naclomi/terminator-html-log) (Linux/MacOS) and [Hyper](https://github.com/naclomi/hyper-html-log) (Windows/MacOS/Linux) (see the subdirectories in this repo\'s `external-plugins/` folder). On starting a new terminal session, just use one of these plugins to log your session to the `WATCH_DIR`.\n\n### Hosting and remote URIs\n\nThe most ideal way to host the output of this tool is on a personal web hosting account that allows access over SSH. Most universities provide this service to their faculty and staff, a la [UW\'s shared web hosting](https://itconnect.uw.edu/connect/web-publishing/shared-hosting/). The instructions for setting this account up, unfortunately, vary from institution to institution. Once you have access, though, the value to put in `REMOTE_URI` would be the remote destination you would normally put in the second half of an `scp` command (eg: `username@servername:remote_path`).\n\nIf suitable institutionally provided web hosting isn\'t available, there are a few other options:\n\n- **Amazon AWS** or **Microsoft Azure** object storage: this script can directly upload contents to an AWS S3 bucket or Azure Blob Storage contianer, both of which can be configured to serve static webpages. The downside of these services is that they are not free\n- **GitHub Pages**: You can create a repo on GitHub and have this script automatically push updates to it. This repo can then be served as a website through GitHub\'s "Pages" feature. This option is free, though GitHub has a soft limit of 10 page updates per hour.\n\n\nIn all cases, access credentials are securely stored in your operating system\'s keychain.\n\n## Installataion and dependencies\n\nInstall with `pip install livecode-streamer[jupyter]`,\nwhich includes all dependencies needed for basic syntax highlighting, rendering jupyter notebooks, and uploading via `scp`/`rsync`.\n\nTo install with dependencies for _all_ plugins:\n`pip install livecode-streamer[jupyter,git,azure,aws,localhost]`\n\nCore requirements:\n* Python 3.7+\n* [watchdog](https://pypi.org/project/watchdog/)\n* [keyring](https://pypi.org/project/keyring/)\n* [pygments](https://pygments.org/)\n\nFor Jupyter notebooks:\n* [nbformat](https://pypi.org/project/nbformat/)\n* [nbconvert](https://pypi.org/project/nbconvert)\n\nFor shell sessions, one of the following terminal emulators:\n* [Hyper](https://hyper.is/) with the [hyper-html-log plugin](https://github.com/naclomi/hyper-html-log) (Windows/MacOS/Linux)\n* [Terminator](https://terminator-gtk3.readthedocs.io/en/latest/) with the [terminator-html-log plugin](https://github.com/naclomi/terminator-html-log) (Linux/MacOS)\n\nFor generic webspace hosting:\n* rsync (optional)\n* ssh/scp\n\nFor hosting on Github Pages:\n* [dulwich](https://pypi.org/project/dulwich/)\n\nFor hosting on Azure blob storage:\n* [azure-storage-blob](https://pypi.org/project/azure-storage-blob/)\n\nFor hosting on AWS S3 buckets:\n* [boto3](https://pypi.org/project/boto3/)\n\nFor hosting locally over an ngrok tunnel:\n* [pyngrok](https://pypi.org/project/pyngrok/)\n\n## Contributing\n\nContributions of bugs, new plugins, or feature suggestions are all welcome. For more information, see [CONTRIBUTING.md](https://github.com/naclomi/livecode-streamer/blob/main/CONTRIBUTING.md).',
    'author': 'Naomi Alterman',
    'author_email': 'naomila@uw.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/naclomi/livecode-streamer',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
