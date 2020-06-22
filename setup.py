from setuptools import setup, find_packages
setup(
    name="benkyo",
    version="0.1",
    py_modules=['benkyo', 'benkyo.commands', 'benkyo.utils', 'benkyo.model', 'benkyo.view', 'benkyo.view.model', 'benkyo.view.widget', 'benkyo.consts'],
    #scripts=["install/installed.py"],
    install_requires=[ "click>=7.1.2", "numpy>=1.18.5", "peewee>=3.13.3", "prompt-toolkit>=3.0.5"],
    entry_points={
        'console_scripts': [
            "benkyo=benkyo.benkyo:cli"
        ],
    },

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst", "*.md"]
    },

    author="Jonathan S. Santos",
    author_email="silva.santos.jonathan@gmail.com",
    description="benkyo is a learning tool based on flashcards that is originally proposed just to run in terminal.",
    keywords="flashcards learning memory review learn",
    url="https://github.com/jonathandasilvasantos/2020-benkyo-cli-flashcards"   # project home page, if any
    ,
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ]

    # could also include long_description, download_url, etc.
)
