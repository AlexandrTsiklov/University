lst = list(map(int, input().split()))
m_in = 10 ** 10
for i in lst:
    if i % 2 != 0 and i < m_in:
        m_in = i
if m_in == 10 ** 10:
    print(0)
else:
    print(m_in)