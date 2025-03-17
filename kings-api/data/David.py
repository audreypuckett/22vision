from model.Highlight import Highlight
from model.Person import Person
from model.King import King
from model.KingsEnum import KingsEnum
from model.BookEnum import BookEnum
from model.StatusEnum import StatusEnum

jesse = Person("Jesse", "Shephard, Servant of the LORD")

DAVID = King(
    "David",
    "1010 BC",
    "970 BC",
    30 ,
    40,
    0,
    KingsEnum.UNITED,
    father=jesse
)

DAVID.set_gods_eyes(StatusEnum.DID_RIGHT)

highlights = [
    Highlight(
        "Went against the Commands of God and committed adultery and murder",
        BookEnum.SECOND_SAMUEL,
        11,
        "2-16"
    ),
    Highlight(
        "David humbled himself at the LORD's rebuke through Nathan and is forgiven",
        BookEnum.SECOND_SAMUEL,
        12,
        "7-14"
    ),
    Highlight(
        "Satan incited against Israel, prompting David to take a census. "
        "God promised to make them as numerous as the stars (not to be counted). "
        "This was evil in the eyes of the LORD",
        BookEnum.FIRST_CHRONICLES,
        21,
        "1-7"
    ),

]

DAVID.set_highlights(highlights)