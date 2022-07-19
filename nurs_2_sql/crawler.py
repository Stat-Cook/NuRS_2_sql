import os

def crawler(path = ".", func = None):

    func = func or (lambda root, dir, files: 0)

    w = os.walk(path)

    for root, dirs, files in w:
        func(root, dirs, files)

    return 0
