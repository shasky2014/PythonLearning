# 344. 反转字符串

class Solution(object):
    def reverseString(self, s):
        """
        :param self:
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s:
            return []
        return self.reverseString(s[1:]) + [s[0]]


if __name__ == '__main__':
    solut_1 = Solution()

    s = ['h', 'e', 'l', 'l', 'o']
    print('递归解：\t\t', solut_1.reverseString(s))
    print('源列表：\t\t', s)
    ans = s.reverse()
    print('reverse：\t', s)
