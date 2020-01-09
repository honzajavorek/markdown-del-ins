from setuptools import setup
from pathlib import Path


setup(
    name='markdown_del_ins',
    version='1.0.0',
    author='Honza Javorek',
    author_email='mail@honzajavorek.cz',
    description='Python-Markdown extension to support the <del> and <ins> tags',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/honzajavorek/markdown-del-ins',
    py_modules=['markdown_del_ins'],
    install_requires=['markdown>=2.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
