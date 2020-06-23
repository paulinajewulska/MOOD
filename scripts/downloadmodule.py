import os
import ssl

import nltk

def main():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download()

    nltk.download('popular')

    os.system("pip install --ignore-installed --upgrade " + "URL")


if __name__ == '__main__':
    main()