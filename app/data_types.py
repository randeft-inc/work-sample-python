from typing import TypedDict


class ExtractedData(TypedDict):
    """Structure for data after extraction phase.

    Attributes:
        basename: The base filename without extension
        content: The raw content extracted from the source
    """

    basename: str
    content: str


class TransformedData(TypedDict):
    """Structure for data after transformation phase.

    Attributes:
        filename: The target filename including extension
        content: The transformed content as bytes
    """

    filename: str
    content: bytes
