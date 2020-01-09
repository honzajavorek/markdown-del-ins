# markdown-del-ins

Allows the [Markdown](https://python-markdown.github.io/) package to interpret ``~~text~~`` as ``<del>text</del>`` and ``++text++`` as ``<ins>text</ins>``.

## Installation

    $ pip install markdown-del-ins

## Usage

    >>> from markdown import Markdown
    >>> md = Markdown(extensions=['markdown_del_ins'])
    >>> src = 'This is ++added content++ and this is ~~deleted **strong** content~~'
    >>> html = md.convert(src)
    >>> print(html)
    <p>This is <ins>added content</ins> and this is <del>deleted <strong>strong</strong> content</del></p>

## License & Credits

This software is released under the modified BSD License. See [LICENSE](LICENSE) for details. The project is a fork of [aleray/mdx_del_ins](https://github.com/aleray/mdx_del_ins).
