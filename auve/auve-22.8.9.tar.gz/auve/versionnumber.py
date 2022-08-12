import os

from dataclasses import dataclass
from pathlib import Path

from . import helper


@dataclass
class VersionNumber:
    __date: str = helper.get_date_string()
    __ydy: int = helper.get_day_of_year()
    __time: str = helper.get_time_string()

    pri: int = int(__date[2:4])
    sec: int = int(__date[5:7])
    mic: int = 0

    build: int = f"{pri}.{__ydy:03d}.{__time}"
    release: str = f"{__date}"

    @property
    def full_version(self) -> str:
        return f"version: {self.version_string}, build_{self.build}, release {self.release}"

    @property
    def version_string(self) -> str:
        return f"{self.pri}.{self.sec}.{self.mic}"

    def __str__(self) -> str:
        return self.version_string


@dataclass
class FileContents:
    version: str = VersionNumber().version_string
    build: str = VersionNumber().build
    release: str = VersionNumber().release

    @property
    def content(self):
        return (self.version, self.build, self.release)


class AutoVersionNumber:
    def __init__(
        self,
        filename: str = None,
        update: bool = False,
    ):
        self.__file = filename
        self.__version_number = VersionNumber()
        self.__root_path = Path(os.getcwd())

        if filename:
            self.__file = self.__root_path.joinpath(filename)
            if not self.__file.is_file():
                self.__write_version_file(self.__file, FileContents())
            else:
                with open(self.__file, "r") as f:
                    lines = f.readlines()

                self.__build_version_number_from_file(lines)

        if update:
            self.update()

    def __build_version_number_from_file(self, content):
        lines = [line.rstrip() for line in content]

        pri, sec, mic = lines[0].split(".")

        self.__version_number.pri = int(pri)
        self.__version_number.sec = int(sec)
        self.__version_number.mic = int(mic)
        self.__version_number.build = lines[1]
        self.__version_number.release = lines[2]

    def __update_version(self):
        new = VersionNumber()
        actual = self.__version_number

        if (new.pri == actual.pri) and (new.sec == actual.sec):
            self.__version_number.mic += 1
        else:
            self.__version_number.mic = 0
            self.__version_number.pri = new.pri
            self.__version_number.sec = new.sec

        return FileContents(
            version=self.__version_number.version_string,
            build=new.build,
            release=new.release,
        )

    def __str__(self):
        return self.__version_number.version_string

    def __write_version_file(self, file: str, data: FileContents()):
        if not Path(Path(file).parent).exists():
            Path(Path(file).parent).mkdir(parents=True)
        with open(file, "w") as f:
            f.write("\n".join(data.content))

    @property
    def version(self):
        return self.__version_number.version_string

    @property
    def full_version(self):
        return self.__version_number.full_version

    @property
    def build(self):
        return self.__version_number.build

    @property
    def release(self):
        return self.__version_number.release

    def update(self):
        if self.__file:
            updated = self.__update_version()
            self.__write_version_file(self.__file, updated)
            return True
        else:
            return False
