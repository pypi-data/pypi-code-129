from pydantic.dataclasses import dataclass
import inflection as inflex


# Dataclass that represents what I'll hold the format for common files, folders, tables, classes, and services.
# Class name is Prose
@dataclass
class Prose:
    folder_format: str
    repo_format: str
    file_format: str
    table_format: str
    class_format: str
    service_format: str


@dataclass
class Inflector:
    name: str

    @property
    def capital(self) -> str:
        return self.name.capitalize()

    @property
    def camel(self) -> str:
        return inflex.camelize(self.name)

    @property
    def plural(self) -> str:
        return inflex.pluralize(self.name)

    @property
    def snake_case(self) -> str:
        return inflex.underscore(self.name)

    @property
    def class_name(self) -> str:
        return inflex.camelize(self.name, uppercase_first_letter=True)

    @property
    def fn_name(self) -> str:
        return inflex.singularize(self.snake_case)

    @property
    def table_name(self) -> str:
        return inflex.tableize(self.name)

    @property
    def repo_class(self) -> str:
        return inflex.camelize(inflex.pluralize(self.class_name))

    @property
    def service_name(self):
        return inflex.singularize(self.class_name)

    @property
    def lower(self) -> str:
        return self.name.lower()
