# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['surprisal']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.2,<4.0.0',
 'numpy>=1.23.1,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'plotext>=5.0.2,<6.0.0',
 'torch>=1.12.0,<2.0.0',
 'transformers>=4.20.1,<5.0.0']

setup_kwargs = {
    'name': 'surprisal',
    'version': '0.1.1',
    'description': 'A package to conveniently compute surprisals for text sequences and subsequences',
    'long_description': '# surprisal\nCompute surprisal from language models!\n\nThe snippet below computes per-token surprisals for a list of sentences\n```python\nfrom surprisal import AutoHuggingFaceModel\n\nsentences = [\n    "The cat is on the mat",\n    "The cat is on the hat",\n    "The cat is on the pizza",\n    "The pizza is on the mat",\n    "I told you that the cat is on the mat",\n    "I told you the cat is on the mat",\n]\n\nm = AutoHuggingFaceModel.from_pretrained(\'gpt2\')\nfor result in m.surprise(sentences):\n    print(result)\n```\nand outputs the following:\n```\n       The       Ġcat        Ġis        Ġon       Ġthe       Ġmat  \n     3.276      9.222      2.463      4.145      0.961      7.237  \n       The       Ġcat        Ġis        Ġon       Ġthe       Ġhat  \n     3.276      9.222      2.463      4.145      0.961      9.955  \n       The       Ġcat        Ġis        Ġon       Ġthe     Ġpizza  \n     3.276      9.222      2.463      4.145      0.961      8.212  \n       The     Ġpizza        Ġis        Ġon       Ġthe       Ġmat  \n     3.276     10.860      3.212      4.910      0.985      8.379  \n         I      Ġtold       Ġyou      Ġthat       Ġthe       Ġcat        Ġis        Ġon       Ġthe       Ġmat \n     3.998      6.856      0.619      2.443      2.711      7.955      2.596      4.804      1.139      6.946 \n         I      Ġtold       Ġyou       Ġthe       Ġcat        Ġis        Ġon       Ġthe       Ġmat  \n     3.998      6.856      0.619      4.115      7.612      3.031      4.817      1.233      7.033 \n```\n\nA surprisal object can be aggregated over a subset of tokens that best match a span of words or characters. \nWord boundaries are inherited from the model\'s standard tokenizer, and may not be consistent across models,\nso using character spans is the default and recommended option.\nSurprisals are in log space, and therefore added over tokens during aggregation.  For example:\n```python\n>>> [s] = m.surprise("The cat is on the mat")\n>>> s[3:6, "word"] \n12.343366384506226\nĠon Ġthe Ġmat\n>>> s[3:6, "char"]\n9.222099304199219\nĠcat\n>>> s[3:6]\n9.222099304199219\nĠcat\n>>> s[1, "word"]\n9.222099304199219\nĠcat\n```\n\nYou can also call `Surprisal.lineplot()` to visualize the surprisals:\n\n```python\nfrom matplotlib import pyplot as plt\n\nf, a = None, None\nfor result in m.surprise(sentences):\n    f, a = result.lineplot(f, a)\n\nplt.show()\n```\n\n![](https://i.imgur.com/HusVOUq.png)\n\n\n`surprisal` also has a minimal CLI:\n```python\npython -m surprisal -m distilgpt2 "I went to the train station today."\n      I      Ġwent        Ġto       Ġthe     Ġtrain   Ġstation     Ġtoday          . \n  4.984      5.729      0.812      1.723      7.317      0.497      4.600      2.528 \n\npython -m surprisal -m distilgpt2 "I went to the space station today."\n      I      Ġwent        Ġto       Ġthe     Ġspace   Ġstation     Ġtoday          . \n  4.984      5.729      0.812      1.723      8.425      0.707      5.182      2.574\n```\n\n\n## installing\n`pip install surprisal`\n\n\n## acknowledgments\n\nInspired from the now-inactive [`lm-scorer`](https://github.com/simonepri/lm-scorer); thanks to\nfolks from [CPLlab](http://cpl.mit.edu/) (particularly, Peng Qian) for comments and help.\n\n\n## license \n[MIT License](./LICENSE).\n(C) 2022, Aalok S.',
    'author': 'aalok-sathe',
    'author_email': 'asathe@mit.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aalok-sathe/surprisal',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
