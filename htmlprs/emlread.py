# -*- encoding: gb2312 -*-
import email

with open('�����������루�յ���ظ���.eml', "r") as fp:
    msg = email.message_from_file(fp)

    subject = msg.get("subject")  # ȡ�ż�ͷ���subject,��Ҳ��������
    # ��������д���ֻ��Ϊ�˽�����=?gbk?Q?=CF=E0=C6=AC?=������subject
    h = email.Header.Header(subject)
    dh = email.Header.decode_header(h)
    subject = dh[0][0]
    print("subject:", subject)
    print("from: ", email.utils.parseaddr(msg.get("from"))[1])  # ȡfrom
    print("to: ", email.utils.parseaddr(msg.get("to"))[1])  # ȡto

# ѭ���ż��е�ÿһ��mime�����ݿ�
for par in msg.walk():
    if not par.is_multipart():
        name = par.get_param("name")
        if name:
            #�и���,�����������
            h = email.Header.Header(name)
            dh = email.Header.decode_header(h)
            fname = dh[0][0]
            print('������:', fname)

            # data = par.get_payload(decode=True)  # ������������ݣ�Ȼ��洢���ļ���
            # try:
            #     f = open(fname, 'wb')  # ע��һ��Ҫ��wb�����ļ�����Ϊ����һ�㶼�Ƕ������ļ�
            # except:
            #     print '�������зǷ��ַ����Զ���һ��'
            # f = open('aaaa', 'wb')
            # f.write(data)
            # f.close()
        else:
            #���,�ʼ�����
            print(par.get_payload(decode=True))  # ������ı����ݣ�ֱ��������Ϳ����ˡ�

    print('+' * 60)  # ��������������ֵ����
