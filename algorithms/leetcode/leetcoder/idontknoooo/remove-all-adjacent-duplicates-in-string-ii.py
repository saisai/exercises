
class S:

    def removeDuplicates(self, s, k):

        stack = [] # [char, count]

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if stack[-1][1] == k:
                stack.pop()

        res =""
        for char, count in stack:
            res += (char * count)
        return res

s = "deeedbbcccbdaa"
k = 3
print(S().removeDuplicates(s, k))
