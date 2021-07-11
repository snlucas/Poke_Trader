class Pokemon():
    def __init__(self, name, base_experience) -> None:
        self._name = name
        self._base_experience = base_experience


    @property
    def name(self) -> str:
        return self._name


    @property
    def base_experience(self) -> int:
        return self._base_experience
