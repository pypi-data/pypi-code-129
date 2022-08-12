# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyobsidianmd']

package_data = \
{'': ['*']}

install_requires = \
['python-frontmatter>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'py-obsidianmd',
    'version': '0.1.1',
    'description': 'python library for ObsidianMD',
    'long_description': "Python utilities for the personal knowledge management tool [Obsidian](https://obsidian.md/)\n\n\n## Motivation\n\nI wanted to modify my notes' metadata in batch and couldn't find an existing plugin to do so.\nIf some of the functionalities you see here are already available in a plugin, please let me know.\nOpen for contributions.\n\n## Current features\n\n* Create a Note object from a file path, that has a 'frontmatter', 'metadata', and 'tags' attributes\n* Add / remove tags from the note\n* Write back the updated note to disk\n\n## Warnings\n\n* **This code hasn't been much tested yet**, use at your own peril\n* **This code only handles tags present in the frontmatter**, not the note body\n\n## Basic usage\n\n\n```{python}\npath = Path('path/to/file')\nnote = Note(path)\n\n## print frontmatter\nprint(note.frontmatter)\n\n## get the note's metadata (from frontmatter) as a dict\nnote.metadata\n\n## get list of tags\nprint(note.tags)\n\n## add a tag\nnote.add_tag('tag_name')\n\n## remove a tag\nnote.remove_tag('tag_name')\n\n## write the note with the updated metadata\nnote.write()\n```\n\nOriginal motivation: add a tag to all files in a folder\n\n```{python}\nimport os\nfrom pathlib import Path\nfrom source.note import Note\n\npath_dir = Path('path/to/dir')\n\nfor r,d,fls in os.walk(path_dir):\n    for f in fls:\n        pth = Path(r)/f\n        note = Note(pth)\n        note.add_tag('tag_name')\n        note.write()\n```\n",
    'author': 'Selim Raboudi',
    'author_email': 'selim.raboudi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/selimrbd/py-obsidianmd',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
