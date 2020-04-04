from odps.udf import annotate


@annotate("bigint,bigint->bigint")
class testss(object):

    def evaluate(self, arg0, arg1):
        return arg0 + arg1


if __name__ == '__main__':
    a = 1
    b = 2

    print(testss.evaluate(None, a, b))
