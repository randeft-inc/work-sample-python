from dataclasses import dataclass
from typing import Any, Dict, Iterator, List


@dataclass
class Records:
    """Container for data flowing through the ETL pipeline."""

    records: List[Dict[str, Any]]

    def __len__(self) -> int:
        return len(self.records)

    def __getitem__(self, index: int) -> Dict[str, Any]:
        return self.records[index]

    def __iter__(self) -> Iterator[Dict[str, Any]]:
        return iter(self.records)
