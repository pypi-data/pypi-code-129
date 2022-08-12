# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mac_cleanup']

package_data = \
{'': ['*']}

install_requires = \
['inquirer>=2.10.0,<3.0.0', 'rich>=12.2.0,<13.0.0', 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['mac-cleanup = mac_cleanup.cli:main']}

setup_kwargs = {
    'name': 'mac-cleanup',
    'version': '2.2.2',
    'description': 'Python cleanup script for macOS',
    'long_description': "# mac-cleanup-py\n\n### 👨\u200d💻 Python cleanup script for macOS \n\n#### [mac-cleanup-sh](https://github.com/mac-cleanup/mac-cleanup-sh) rewritten in Python\n\n\n### What does script do?\n\n1. Cleans Trash\n2. Deletes unnecessary logs & files\n3. Removes cache\n\n![mac-cleanup_v2_X_X](https://user-images.githubusercontent.com/44712637/183507992-03466528-ddb1-4370-852c-9ef8dc008a11.gif)\n\n<details>\n   <summary>\n   Default modules\n   </summary>\n\n  </br>\n\n  - `adobe` - Clears **Adobe** cache files\n  - `android` - Clears **Android** caches\n  - `brew` - Clears **Homebrew** cache\n  - `cacher` - Clears **Cacher** logs\n  - `chrome` - Clears Google Chrome cache\n  - `composer` - Clears composer cache\n  - `dns_cache` - Clears DNS cache\n  - `docker` - Cleanup dangling **Docker Images** and stopped **containers**\n  - `dropbox` - Clears **Dropbox** cache\n  - `gem` - Cleanup any old versions of **Gems**\n  - `go` - Clears **Go** cache\n  - `google_drive` - Clears **Google Drive** caches\n  - `gradle` - Clears **Gradle** caches\n  - `inactive_memory` - Purge Inactive Memory\n  - `ios_apps` - Cleanup **iOS Applications**\n  - `ios_backups` - Removes **iOS Device Backups**\n  - `java_cache` - Removes **Java head dumps** from home directory\n  - `jetbrains` - Removes logs from **PhpStorm**, **PyCharm**  etc\n  - `kite` - Deletes **Kite** logs\n  - `lunarclient` - Removes **Lunar Client** logs and cache\n  - `microsoft_teams` - Remove **Microsoft Teams** logs and cache\n  - `minecraft` - Remove **Minecraft** logs and cache\n  - `npm` - Cleanup **npm** Cache\n  - `pod` - Cleanup **CocoaPods** Cache Files\n  - `poetry` - Clears **Poetry** cache\n  - `pyenv` - Cleanup **Pyenv-VirtualEnv** Cache\n  - `steam` - Remove **Steam** logs and cache\n  - `system_caches` - Clear **System cache**\n  - `system_log` - Clear **System Log** Files\n  - `trash` - Empty the **Trash** on All Mounted Volumes and the Main HDD\n  - `wget_logs` - Remove **Wget** logs and hosts\n  - `xcode` - Cleanup **Xcode Derived Data** and **Archives**\n  - `xcode_simulators` - Reset **iOS simulators**\n  - `yarn` - Cleanup **yarn** Cache\n\n\n</details>\n\n\n\n## Install Automatically\n\n### Using homebrew\n\n```bash\nbrew tap mac-cleanup/mac-cleanup-py\nbrew install mac-cleanup-py\n```\n\n### Using pip\n\n```bash\npip3 install rich toml inquirer \npip3 install mac-cleanup\n```\n\n## Uninstall\n\n### Using homebrew\n\n```bash\nbrew uninstall mac-cleanup-py\nbrew untap mac-cleanup/mac-cleanup-py\n```\n\n### Using pip\n\n```bash\npip3 uninstall rich toml inquirer \npip3 uninstall mac-cleanup\n```\n\n## Usage Options\n\nHelp menu:\n\n```\n$ mac-cleanup -h\n\nusage: mac-cleanup [-h] [-d] [-u] [-c] [-m]\n\n    A Mac Cleanup Utility in Python\n    v2.2.2\n    https://github.com/mac-cleanup/mac-cleanup-py\n\noptional arguments:\n  -h, --help       show this help message and exit\n  -d, --dry-run    Shows approx space to be cleaned\n  -u, --update     Script will update brew while cleaning\n  -c, --configure  Launch modules configuration\n  -m, --modules    Specify custom modules' path\n```\n",
    'author': 'Drugsosos',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mac-cleanup/mac-cleanup-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.12',
}


setup(**setup_kwargs)
