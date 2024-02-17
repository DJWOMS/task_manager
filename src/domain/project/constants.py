import enum


class StatusProject(enum.Enum):
    ACTIVE = "В разработке"
    CLOSED = "Закрыт"
    DISCUSSION = "В обсуждении"
    MAINTENANCE = "Поддержка"
