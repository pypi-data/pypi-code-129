from auve import AutoVersionNumber


def demo_use_without_file():
    av = AutoVersionNumber()
    print(av)
    print(av.version)
    print(av.build)
    print(av.release)
    print(av.full_version)
    print(av.update())
    print("^ is 'False' because no file is provided")
    print(AutoVersionNumber())
    print(AutoVersionNumber(update=True))


def demo_use_with_file():
    fn = "DEMO_VERSION"
    av = AutoVersionNumber(fn)
    print(av)
    print(av.version)
    print(av.build)
    print(av.release)
    print(av.full_version)
    print(av.update())
    print(AutoVersionNumber(filename=fn))
    print(AutoVersionNumber(filename=fn, update=True))


def demo():
    demo_use_without_file()
    print()
    demo_use_with_file()


if __name__ == "__main__":
    demo()
