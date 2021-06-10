"""
https://leetcode.com/problems/accounts-merge/solution/
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts.
Note that even if two accounts have the same name, they may belong to different people as people could have the same name. 
A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. 
The accounts themselves can be returned in any order.
"""

class Solution:
    def accountsMerge(self, accounts):
        email_account_map = {}

        # initialize graph/ maps
        for id, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                email_account_map.setdefault(email, []).append(id)

        # traverse nodes and neighbors and update email groups
        def traverse(id, allEmails):
            if seen[id]:
                return
            seen[id] = True
            account = accounts[id]
            name = account[0]
            emails = account[1:]
            allEmails.update(emails)
            for email in emails:
                neighbours  = [neighbour for neighbour in email_account_map[email]]
                for neighbour in neighbours:
                    traverse(neighbour, allEmails)

        result = []
        seen = [False] * len(accounts)
        for id, account in enumerate(accounts):
            if seen[id]:
                continue
            name = account[0]
            allEmails = set()
            traverse(id, allEmails)
            result.append([name,] + sorted(allEmails))
        return result

    def test_accountsMerge(self):
        testcases = [[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]], [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]]
        for testcase in testcases:
            print(testcase)
            print(self.accountsMerge(testcase))