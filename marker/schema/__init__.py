from enum import auto, IntEnum


class BlockTypes(IntEnum):
    Line = auto()
    Span = auto()
    FigureGroup = auto()
    TableGroup = auto()
    ListGroup = auto()
    PictureGroup = auto()
    Page = auto()
    Caption = auto()
    Code = auto()
    Figure = auto()
    Footnote = auto()
    Form = auto()
    Equation = auto()
    Handwriting = auto()
    TextInlineMath = auto()
    ListItem = auto()
    PageFooter = auto()
    PageHeader = auto()
    Picture = auto()
    SectionHeader = auto()
    Table = auto()
    Text = auto()
    TableOfContents = auto()
    Document = auto()

    def __str__(self):
        return self.name
