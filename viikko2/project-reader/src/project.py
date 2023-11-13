class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_list_items(self, dependencies):
        return "- "+"\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:\n{self._stringify_list_items(self.authors)}"
            f"\n\nDependencies:\n{self._stringify_list_items(self.dependencies)}"
            f"\n\nDevelopment dependencies:\n{self._stringify_list_items(self.dev_dependencies)}"
        )
