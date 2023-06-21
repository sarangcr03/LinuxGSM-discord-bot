from setuptools import setup, find_packages

setup(
    name='DGSbot',
    version='2.5',
    packages=['DGSbot'],
    install_requires=[
        'discord.py',
        'discord-py-slash-command',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'DGSbot=DGSbot.__main__:main',
            'DGSbot-setup=DGSbot.setup_script:setup',
        ]
    }
)
