import Person
from typing import Optional

class King(Person):
    def __init__(
            self,
            name: str,
            reign_start: int,
            reign_end: Optional[int],
            age_kinged: int,
            years_reigned: int,
            months_reigned: Optional[int] = 0,
            father: Optional[Person] = None,
            mother: Optional[Person] = None,
            predecessor: Optional["King"] = None
    ):
        super().__init__(name, "King")
        self._reign_start = reign_start
        self._reign_end = reign_end
        self._age_kinged = age_kinged
        self._years_reigned = years_reigned
        self._months_reigned = months_reigned
        self._father = father
        self._mother = mother
        self._predecessor = predecessor

    # Getters
    def get_reign_start(self) -> int:
        return self._reign_start

    def get_reign_end(self) -> Optional[int]:
        return self._reign_end

    def get_age_kinged(self) -> int:
        return self._age_kinged

    def get_years_reigned(self) -> int:
        return self._years_reigned

    def get_months_reigned(self) -> int:
        return self._months_reigned

    def get_father(self) -> Optional[Person]:
        return self._father

    def get_mother(self) -> Optional[Person]:
        return self._mother

    def get_predecessor(self) -> Optional["King"]:
        return self._predecessor

    # Setters
    def set_reign_end(self, reign_end: int):
        """Updates the reign end year."""
        self._reign_end = reign_end

    def set_years_reigned(self, years_reigned: int, months_reigned: int = 0):
        """Updates the years reigned and optionally the months."""
        self._years_reigned = years_reigned
        self._months_reigned = months_reigned

    def set_predecessor(self, predecessor: "King"):
        """Updates the predecessor."""
        self._predecessor = predecessor

    # __str__ method
    def __str__(self) -> str:
        reign_period = f"{self._reign_start} - {self._reign_end if self._reign_end else 'Present'}"
        years_reigned_str = (
            f"{self._years_reigned} years"
            if self._years_reigned > 0
            else f"{self._months_reigned} months"
        )
        father_str = f", Father: {self._father.get_name()}" if self._father else ""
        mother_str = f", Mother: {self._mother.get_name()}" if self._mother else ""
        predecessor_str = f", Predecessor: {self._predecessor.get_name()}" if self._predecessor else ""

        return f"King {self._name} (Reigned: {reign_period}, Age Kinged: {self._age_kinged}, {years_reigned_str}{father_str}{mother_str}{predecessor_str})"

    # to_dict method
    def to_dict(self) -> dict:
        """Converts the object to a dictionary format."""
        return {
            "name": self._name,
            "role": self._role,
            "reign_start": self._reign_start,
            "reign_end": self._reign_end,
            "age_kinged": self._age_kinged,
            "years_reigned": self._years_reigned,
            "months_reigned": self._months_reigned,
            "father": self._father.get_name() if self._father else None,
            "mother": self._mother.get_name() if self._mother else None,
            "predecessor": self._predecessor.get_name() if self._predecessor else None
        }