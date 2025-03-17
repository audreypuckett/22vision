from model.Person import Person
from model.KingsEnum import KingsEnum
from model.StatusEnum import StatusEnum  # ✅ Import StatusEnum
from typing import Optional

class King(Person):
    def __init__(
            self,
            name: str,
            reign_start: str,
            reign_end: Optional[str],
            age_kinged: int,
            years_reigned: int,
            months_reigned: Optional[int] = 0,
            kingship: KingsEnum = KingsEnum.UNITED,
            gods_eyes: StatusEnum = StatusEnum.DID_NOT_DO_RIGHT,  # ✅ Default to neutral
            father: Optional[Person] = None,
            mother: Optional[Person] = None,
            predecessor: Optional[int] = None,
            id: Optional[int] = None
    ):
        super().__init__(name, "King", id)
        self.reign_start = reign_start
        self.reign_end = reign_end
        self.age_kinged = age_kinged
        self.years_reigned = years_reigned
        self.months_reigned = months_reigned
        self.kingship = kingship
        self.gods_eyes = gods_eyes  # ✅ New attribute
        self.father = father
        self.mother = mother
        self.predecessor_id = predecessor

    # Getters
    def get_gods_eyes(self) -> StatusEnum:
        return self.gods_eyes

    # Setters
    def set_gods_eyes(self, status: StatusEnum):
        """Sets the king's status in God's eyes."""
        if not isinstance(status, StatusEnum):
            raise ValueError("gods_eyes must be a valid StatusEnum value")
        self.gods_eyes = status

    # __str__ method
    def __str__(self) -> str:
        id_str = f"ID: {self._id}, " if self._id else ""
        return f"King {self._name} ({id_str}Reigned: {self.reign_start} - {self.reign_end if self.reign_end else 'Present'}, Kingdom: {self.kingship.value}, God's Eyes: {self.gods_eyes.value})"

    # to_dict method
    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict.update({
            "gods_eyes": self.gods_eyes.value,
            "reign_start": self.reign_start,
            "reign_end": self.reign_end,
            "age_kinged": self.age_kinged,
            "years_reigned": self.years_reigned,
            "months_reigned": self.months_reigned,
            "kingship": self.kingship.value,
            "father": self.father.get_name() if self.father else None,
            "mother": self.mother.get_name() if self.mother else "Unnamed",
            "predecessor_id": self.predecessor_id
        })
        return base_dict