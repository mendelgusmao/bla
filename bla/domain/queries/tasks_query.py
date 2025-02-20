from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any


@dataclass
class TasksQuery:
    status: str | None
    due_at: datetime | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(
            self,
            dict_factory=lambda i: {k: v for (k, v) in i if v is not None},
        )
