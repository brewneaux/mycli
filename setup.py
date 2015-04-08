import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('mysql_cli/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

description = 'CLI for MySQL Database. With auto-completion and syntax highlighting.'


setup(
        name='mysql_cli',
        author='Amjith Ramanujam',
        author_email='amjith[dot]r[at]gmail.com',
        version=version,
        license='LICENSE.txt',
        url='http://mysql-cli.com',
        packages=find_packages(),
        package_data={'mysql_cli': ['mysql-clirc']},
        description=description,
        long_description=open('README.rst').read(),
        install_requires=[
            'click >= 3.2',
            'Pygments >= 2.0',  # Pygments has to be Capitalcased. WTF?
            'jedi == 0.8.1',    # Temporary fix for installation woes.
            'prompt_toolkit==0.26',
            'pymysql',
            'sqlparse >= 0.1.14',
            ],
        entry_points='''
            [console_scripts]
            mysql-cli=mysql_cli.main:cli
        ''',
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: Unix',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: SQL',
            'Topic :: Database',
            'Topic :: Database :: Front-Ends',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
        )