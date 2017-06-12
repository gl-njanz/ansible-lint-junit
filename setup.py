from setuptools import setup

setup(
    name='ansible-lint-junit',
    packages=['ansible-lint-junit'],
    version='0.7',
    description='ansible-lint to JUnit converter.',
    author='wasil',
    author_email='piotr.m.wasilewski@gmail.com',
    url='https://github.com/wasilak/ansible-lint-junit',
    download_url='https://github.com/wasilak/ansible-lint-junit/archive/0.7.tar.gz',
    keywords=['ansible', 'junit'],
    classifiers=[],
    scripts=['bin/ansible-lint-junit'],
    install_requires=[
        'ansible-lint',
    ],
)
