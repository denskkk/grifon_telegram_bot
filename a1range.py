from dataclasses import dataclass


@dataclass
class A1Range:
    sheet_name: str
    start_row: int
    start_col: int
    end_row: int
    end_col: int

    def format(self) -> str:
        start = f"{self.col_number_to_letter(self.start_col)}{self.start_row}"
        end = f"{self.col_number_to_letter(self.end_col)}{self.end_row}"
        return f"{self.sheet_name}!{start}:{end}"

    def iter_rows(self):
        return range(self.start_row, self.end_row + 1)

    def iter_cols(self):
        return range(self.start_col, self.end_col + 1)

    @staticmethod
    def col_number_to_letter(j: int) -> str:
        if 1 <= j <= 26:
            return chr(ord('A') + j - 1)
        elif 27 <= j <= 26 * 26:
            first_letter = chr(ord('A') - 1 + (j - 1) // 26)
            second_letter = chr(ord('A') + (j - 1) % 26)
            return first_letter + second_letter
        else:
            raise ValueError(f"Col number is out of range: {j!r}")

    @staticmethod
    def col_letter_to_number(letters: str) -> int:
        letters = letters.upper()
        if len(letters) == 1 and (ord(letters) < ord('A') or ord(letters) > ord('Z')):
            raise ValueError(f"Col letter is out of range: {letters!r}")

        if len(letters) == 2 and (ord(letters[1]) < ord('A') or ord(letters[1]) > ord('Z')):
            raise ValueError(
                f"The second Col letter is out of range: {letters!r}")

        if len(letters) == 1:
            return ord(letters) - ord('A') + 1
        elif len(letters) == 2:
            return (ord(letters[0]) - ord('A') + 1) * 26 + ord(letters[1]) - ord('A') + 1

    @staticmethod
    def extract_letters(text) -> str:
        only_letters = ''
        for t in text:
            if t.isalpha():
                only_letters += t
        return only_letters

    @staticmethod
    def extract_digits(text) -> str:
        only_digits = ''
        for t in text:
            if t.isdigit():
                only_digits += t
        return only_digits

    @classmethod
    def parse_a1_range(cls, a1: str):
        if "!" in a1 and ":" in a1:
            sheet_name, cell_range = a1.split('!')
            range_start, range_end = cell_range.split(':')
            start_col, start_row = cls.extract_letters(
                range_start), cls.extract_digits(range_start)
            end_col, end_row = cls.extract_letters(
                range_end), cls.extract_digits(range_end)
            return cls(
                sheet_name=sheet_name,
                start_col=cls.col_letter_to_number(start_col),
                start_row=int(start_row),
                end_col=cls.col_letter_to_number(end_col),
                end_row=int(end_row),
            )
        else:
            raise ValueError(
                f'Error! For method "parse_a1_range()" must be full address!')

    @classmethod
    def create_a1range_from_list(cls, sheet_name, from_row, from_col, array):
        """
        The method find coordinates in format A1Notation for a list with data for inserting into a Google Sheet
        :param sheet_name: sheet name in Google Sheet
        :param from_col: the column coordinate of the upper left corner
        :param from_row: the row coordinate of the upper left corner
        :param array: a list with data for inserting in Google Sheet
        :return: coordinates for Google Sheet in format A1Notation
        """
        count_rows = len(array)
        count_cols = 0
        for row in array:
            if len(row) > count_cols:
                count_cols = len(row)
        return cls(
            sheet_name=sheet_name,
            start_col=from_col,
            start_row=from_row,
            end_col=from_col+count_cols-1,
            end_row=from_row+count_rows-1,
        )
