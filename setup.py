from setuptools import setup

APP = ['timezone.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'tz.icns',
    # 'plist': {
    #     'CFBundleShortVersionString': '0.2.0',
    #     'LSUIElement': True,
    # },
    'packages': ['rumps'],
}

setup(
    app=APP,
    name='TimeZone',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],install_requires=['rumps']
)