import fire
from chafic.storage import Storage


class Chafic(object):
    """Data management tool for chaFic dataset."""

    def __init__(self):
        self.storage = Storage()

    def download(self, directory="", kind="F", year="", force=False):
        return self.storage.download(directory, kind, year, force)


def main():
    fire.Fire(Chafic)


if __name__ == '__main__':
    main()
