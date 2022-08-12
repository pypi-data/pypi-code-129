from cityfront.client import ClientBase


class AppwriteSDK(ClientBase):
    def __init__(
        self,
        base_url: str = "https://appwrite.autoworkz.org/v1",
        project: str | None = None,
    ):
        super().__init__(base_url)
        if project:
            self.project = project

    def account(self):
        return Account(self)
