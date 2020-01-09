from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor


class DelInsExtension(Extension):
    def extendMarkdown(self, md):
        del_proc = SimpleTagInlineProcessor(r'(\~\~)(.+?)(\~\~)', 'del')
        md.inlinePatterns.register(del_proc, 'del', 200)

        ins_proc = SimpleTagInlineProcessor(r'(\+\+)(.+?)(\+\+)', 'ins')
        md.inlinePatterns.register(ins_proc, 'ins', 200)


def makeExtension(**kwargs):
    return DelInsExtension(**kwargs)


if __name__ == '__main__':
    import doctest
    doctest.testfile('README.md')
