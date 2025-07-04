from setuptools import setup

APP = ['main.py']
OPTIONS = {
    'packages': ['tkinter'],
    'includes': ['_tkinter'],
    'plist': {
        'CFBundleName': 'End of Epoch',
        'CFBundleDisplayName': 'End of Epoch',
        'CFBundleIdentifier': 'us.xevio.epochleft',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
        'LSMinimumSystemVersion': '10.13.0',
    }
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
)