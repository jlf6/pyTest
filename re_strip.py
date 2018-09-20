import re

def re_strip(s, t=r'\s'):
    t_format = r'^%s*|%s*$' % (t, t)
    s_re = re.compile(t_format)
    s = s_re.sub('',s)
    return s

print(re_strip('aadasdfsaaa','a'))
print(re_strip('  dafsdfa sadfasd  '))