class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {}
        for i in range(65, 91):
            for j in range(1, rows + 1):
                self.sheet[chr(i) + str(j)] = 0

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[cell] = 0


    def getValue(self, formula: str) -> int:
        if formula[0] == "=":
            formula = formula[1:]
            num = ""
            tokens = []
            for ch in formula:
                if ch.isalnum():
                    num += ch
                else:
                    if num:
                        tokens.append(num)
                        num = ""
                    tokens.append(ch)
            if num:
                tokens.append(num)
            result = 0
            operator = "+"
            for token in tokens:
                if token in "+-":
                    operator = token
                elif token.isalnum():
                    if token in self.sheet:
                        value = self.sheet[token]
                    else:
                        value = int(token)
                    if operator == "+":
                        result += value
                    else:
                        result -= value
        return result



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)