from odps.udf import annotate


@annotate("bigint,bigint->bigint")
class pyudf_avt1(object):
    def evaluate(self, arg0):
        if arg0 is None or len(arg0.strip()) == 0:
            return None
        v_no_l = arg0.split('.')
        a1 = v_no_l[0]
        a2 = ('000' + v_no_l[1])[-3:]
        if len(v_no_l) == 3:
            a3 = ('000' + v_no_l[2])[-3:]
        # elif len(v_no_l) > 3:
        # 有四位版本号，第四版本号有字母
        #     a4 = v_no_l[3]
        else:
            a3 = '000'
        return int('{0}{1}{2}'.format(a1, a2, a3))

        # input        output
        # 6.14.2       6014002
        # 6.7.1        6007001
        # 10.2.1      10002001
        # 10.2.13     10002013
        # 9.2          90