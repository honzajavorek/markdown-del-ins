# Contributing

As of now, this document is rather maintainer notes.

## Testing

Tests are implemented as doctests. Run

```
$ python markdown_del_ins.py
```

With every push, the code is tested by [GitHub Actions](https://github.com/honzajavorek/markdown-del-ins/actions).

## Publishing

To publish the library,

1. update the version number in `setup.py`,
2. commit the version change by `git commit -am "vX.Y.Z"`
3. add a release tag by `git tag vX.Y.Z`
4. push everything to GitHub by `git push origin master --tags`
5. see if [GitHub Actions](https://github.com/honzajavorek/markdown-del-ins/actions) pass and correctly publish a new version to the PyPI

Done!
