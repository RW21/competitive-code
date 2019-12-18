from typing import List


def treat(string):
    try:
        index = string.index('+')
        string = string[:index]

    except ValueError:
        pass

    string = string.replace('.', '')

    return string


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        proper = set()

        for email in emails:
            local, domain = email.split('@')

            proper.add(treat(local) + '@' + domain)

        return len(proper)
