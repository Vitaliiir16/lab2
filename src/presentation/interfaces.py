from abc import ABC, abstractmethod
from src.domain.models import ImportReport

class IImportPresenter(ABC):
    @abstractmethod
    def present(self, report: ImportReport) -> None:
        raise NotImplementedError
