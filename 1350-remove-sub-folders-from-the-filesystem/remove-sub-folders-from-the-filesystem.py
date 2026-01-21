class Solution(object):
    def removeSubfolders(self, folder):
        folder.sort()
        res = []
        prev = ""

        for f in folder:
            if not prev or not f.startswith(prev + "/"):
                res.append(f)
                prev = f

        return res
