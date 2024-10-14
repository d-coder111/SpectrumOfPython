from abc import ABC, abstractmethod

class UIInterface(ABC):
    @abstractmethod
    def print_board(self, board: list) -> None:
        pass

    @abstractmethod
    def get_user_input(self) -> str:
        pass

    @abstractmethod
    def update_board(self, board: list, move: str) -> None:
        pass
