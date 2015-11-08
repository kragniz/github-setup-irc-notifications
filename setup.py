import setuptools

setuptools.setup(
    name="github-setup-irc-notifications",
    version="0.1.0",
    url="https://github.com/kragniz/github-setup-irc-notifications",

    author="Louis Taylor",
    author_email="louis@kragniz.eu",

    description="Configure all repositories in an organization with irc notifications",
    long_description=open('README.rst').read(),

    py_modules=['githubsetupircnotifications'],
    entry_points={'console_scripts':
        ['github-setup-irc-notifications = githubsetupircnotifications:main',]
    ,},

    install_requires=[
        'github3.py'
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
