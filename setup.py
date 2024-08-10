from setuptools import setup, find_packages

APP = ['BinarY.py']
DATA_FILES = []
OPTIONS = {
	'py2app': {
		'packages': find_packages(),
		'iconfile': '',
		'plist': {
			'CFBundleDevelopmentRegion': 'English',
			'CFBundleIdentifier': 'com.CrazyFlyKite.BinarY',
			'CFBundleVersion': '1.0',
			'HSHumanReadableCopyright': 'Copyright ©, CrazyFlyKite, All Rights Reserved'
		}
	}
}
SETUP_REQUIRES = ['py2app']
INSTALL_REQUIRES = [line.strip() for line in open('requirements.txt').readlines()]

if __name__ == '__main__':
	setup(app=APP, options=OPTIONS, setup_requires=SETUP_REQUIRES, install_requires=INSTALL_REQUIRES)
