class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op.lstrip("-").isdigit():
                record.append(int(op))
            elif op == "+":
                record.append(record[-1] + record[-2])
            elif op == "D":
                record.append(record[-1] * 2)
            else:
                record.pop()
        return sum(record)