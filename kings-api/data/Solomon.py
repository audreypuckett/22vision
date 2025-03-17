from model.Highlight import Highlight
from model.King import King
from model.KingsEnum import KingsEnum
from model.BookEnum import BookEnum
from model.StatusEnum import StatusEnum

SOLOMON = King(
    "Solomon",
    "970 BC",
    "931 BC",
    20,
    40,
    0,
    KingsEnum.UNITED,
)

SOLOMON.set_gods_eyes(StatusEnum.DID_NOT_DO_RIGHT)
SOLOMON.set_alt_names(["Jedidiah"])

highlights = [
    Highlight(
        "Loved by the LORD and given the name Jedidiah",
        BookEnum.SECOND_SAMUEL,
        12,
        "24-25"
    ),
    Highlight(
        "God granted him wisdom",
        BookEnum.FIRST_KINGS,
        1,
        "4-15"
    ),
    Highlight(
        "Led astray from God by Lust, wanting to please his wives",
        BookEnum.FIRST_KINGS,
        11,
        "7-8"
    ),
    Highlight(
        "Put foreigners in chains",
        BookEnum.SECOND_CHRONICLES,
        8,
        "8"
    ),

]

SOLOMON.set_highlights(highlights)