from dataclasses import dataclass


@dataclass
class PaginationQuery:
    page: int
    amount: int
