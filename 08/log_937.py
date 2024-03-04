from functools import cmp_to_key


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        """time 30 / space 78"""

        let_logs = []
        dig_logs = []

        for log in logs:
            delim = log.find(" ")
            if log[delim + 1].isdigit():
                dig_logs.append(log)
            else:
                let_logs.append(log)

        return sorted(let_logs, key=cmp_to_key(compare_let_logs)) + dig_logs


def compare_let_logs(log1: str, log2: str) -> int:
    delim1 = log1.find(" ")
    delim2 = log2.find(" ")

    cont1 = log1[delim1 + 1 :]
    cont2 = log2[delim2 + 1 :]
    if cont1 < cont2:
        return -1
    elif cont1 > cont2:
        return 1

    id1 = log1[:delim1]
    id2 = log2[:delim2]
    if id1 < id2:
        return -1
    elif id1 > id2:
        return 1
    else:
        return 0
