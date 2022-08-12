from setuptools import find_packages, setup


setup(
    name='tksss',
    version='1.0.0',
    packages=find_packages(exclude=('test',)),

    author='uchida1512',
    author_email='uchida1512@gmail.com',

    description='This is a test package for uchida',

    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',

    python_requires='~=3.8',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],

    install_requires=[
        'Click~=7.0',
        'Pillow~=6.2.1',
        'requests~=2.28.1'
    ],
    # entry_points では、console_scripts キーを使って、スクリプトインタフェースの
    # 登録を行っている。
    # console_scripts キーにスクリプトインタフェースを登録すると、そのインタフェースを
    # 呼び出すためのスクリプトがインストール中に自動で作成される。
    entry_points={
        'console_scripts': [
            'tksss=tksss.core:cli'
        ]
    }
)