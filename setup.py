from setuptools import setup, find_packages

REQ = [
'appnope',
'asttokens',
'backcall',
'beautifulsoup4',
'certifi',
'charset-normalizer',
'coverage',
'decorator',
'exceptiongroup',
'executing',
'gunicorn',
'idna',
'iniconfig',
'ipython',
'jedi',
'Jinja2',
'MarkupSafe',
'matplotlib-inline',
'packaging',
'parse',
'parso',
'pexpect',
'pickleshare',
'pluggy',
'prompt-toolkit',
'ptyprocess',
'pure-eval',
'Pygments',
'pytest',
'pytest-cov',
'requests',
'requests-wsgi-adapter',
'six',
'soupsieve',
'stack-data',
'tomli',
'traitlets',
'urllib3',
'waitress',
'wcwidth',
'WebOb',
'WebTest'
]



setup(
    name='salt',
    version='0.1',
    packages=find_packages(),
    install_requires=REQ,
    entry_points={
        'console_scripts': [
            'salt-cli = salt.cli:main',
            # add any other console scripts here
        ]
    },
    # Add the following lines to create a wheel distribution
    setup_requires=['wheel'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
)