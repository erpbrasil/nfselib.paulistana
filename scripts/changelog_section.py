#!/usr/bin/env python3
"""Imprime a seção de uma versão do CHANGELOG.rst, em Markdown.

Uso: python scripts/changelog_section.py 0.5.0 [CHANGELOG.rst]

Sai com código 1 se a versão não tiver seção no changelog. O workflow de
publicação usa isso para barrar o release de uma versão sem changelog e para
montar as notas do release no GitHub.
"""
import re
import sys


def section(text, version):
    lines = text.splitlines()
    start = None
    for i in range(len(lines) - 1):
        is_heading = re.fullmatch(r"~{3,}", lines[i + 1].strip() or "x")
        if not is_heading:
            continue
        if start is None:
            if re.match(r"%s(\s|$)" % re.escape(version), lines[i].strip()):
                start = i + 2
        else:
            return "\n".join(lines[start:i]).strip()
    if start is None:
        return None
    return "\n".join(lines[start:]).strip()


def main():
    version = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else "CHANGELOG.rst"
    with open(path, encoding="utf-8") as fh:
        body = section(fh.read(), version)
    if not body:
        sys.stderr.write("CHANGELOG sem seção para a versão %s\n" % version)
        return 1
    print(body.replace("``", "`"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
