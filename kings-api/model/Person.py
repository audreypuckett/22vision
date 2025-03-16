from typing import List
import Highlight

class Person:
    def __init__(self, name: str, role: str):
        self._name = name
        self._role = role
        self._alternative_names: List[str] = []
        self._highlights: List[Highlight] = []  # Now storing Highlight objects

    # Getters
    def get_name(self) -> str:
        """Returns their name."""
        return self._name

    def get_role(self) -> str:
        """Returns their role."""
        return self._role

    def get_alt_names(self) -> List[str]:
        """Returns a list of alternative names."""
        return self._alternative_names

    def get_highlights(self) -> List[Highlight]:
        """Returns a list of Highlight objects."""
        return self._highlights

    # Setters
    def set_alt_names(self, alt_names: List[str]):
        """Sets a list of alternative names."""
        self._alternative_names = alt_names

    def set_highlights(self, highlights: List[Highlight]):
        """Sets the highlights list with Highlight objects."""
        self._highlights = highlights

    # Methods to manage alternative names
    def add_alt_name(self, alt_name: str):
        """Adds an alternative name if it's not already in the list."""
        if alt_name not in self._alternative_names:
            self._alternative_names.append(alt_name)

    def remove_alt_name(self, alt_name: str):
        """Removes an alternative name if it exists."""
        if alt_name in self._alternative_names:
            self._alternative_names.remove(alt_name)

    # Methods to manage highlights
    def add_highlight(self, highlight: Highlight):
        """Adds a Highlight object if it's not already in the list."""
        if highlight not in self._highlights:
            self._highlights.append(highlight)

    def remove_highlight(self, highlight: Highlight):
        """Removes a Highlight object if it exists."""
        if highlight in self._highlights:
            self._highlights.remove(highlight)

    # __str__ method
    def __str__(self) -> str:
        alt_names_part = f" (also known as {', '.join(self._alternative_names)})" if self._alternative_names else ""
        highlights_part = f" | Highlights: {', '.join(str(h) for h in self._highlights)}" if self._highlights else ""
        return f"Person: {self._name}{alt_names_part}, Role: {self._role}{highlights_part}"

    # to_dict method
    def to_dict(self) -> dict:
        """Converts the object to a dictionary format."""
        return {
            "name": self._name,
            "role": self._role,
            "alternative_names": self._alternative_names,
            "highlights": [highlight.to_dict() for highlight in self._highlights]
        }