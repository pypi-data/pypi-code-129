import os
import sys
import json

if "TRUSTY_PATH" in os.environ:
    TRUSTY_PATH = os.path.join(
        os.path.expandvars(os.environ.get("TRUSTY_PATH", None)),
        ".trusty",
    )
else:
    TRUSTY_PATH = os.path.join(
        os.environ["HOME"],
        ".trusty",
    )


def get(identifier, *args, **kwargs):
    return TrustyDictionary(identifier, *args, **kwargs)


class TrustyDictionary(dict):
    def __init__(self, identifier, *args, **kwargs):
        super(TrustyDictionary, self).__init__(*args, **kwargs)
        self.identifier = identifier
        self.load()

    def load(self):
        if os.path.exists(self.location()):
            with open(self.location(), "r") as f:
                self.update(json.load(f))

    def save(self):
        if not os.path.exists(TRUSTY_PATH):
            os.makedirs(TRUSTY_PATH)
        try:
            data = json.dumps(
                self,
                indent=4,
            )

        except BaseException:
            raise Exception("Trusty Dictionary data could not be encoded to JSON")

        with open(self.location(), "w") as f:
            f.write(data)

    def location(self):
        return os.path.join(
            TRUSTY_PATH,
            "%s" % (self.identifier,),
        )
