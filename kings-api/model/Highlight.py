
from model.BookEnum import BookEnum

class Highlight:
    def __init__(self, note: str, book: BookEnum, chapter: int, verse: str = None):
        self._note = note
        self._book = book
        self._chapter = chapter
        self._verse = verse

    def get_note(self) -> str:
        """Returns the note."""
        return self._note

    def get_book(self) -> BookEnum:
        """Returns the book."""
        return self._book

    def get_chapter(self) -> int:
        """Returns the chapter number."""
        return self._chapter

    def get_verse(self) -> str:
        """Returns the verse or verse range (if any)."""
        return self._verse

    def __str__(self):
        reference = f"{self._book.value} {self._chapter}"
        if self._verse:
            reference += f":{self._verse}"
        return f'Highlight: "{self._note}" - {reference}'

    def to_dict(self):
        """Converts highlight to a dictionary format"""
        return {
            "note": self._note,
            "book": self._book.value,
            "chapter": self._chapter,
            "verse": self._verse
        }