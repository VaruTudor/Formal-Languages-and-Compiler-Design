from domain.HashTable import HashTable


def testBasic():
    st = HashTable(5)

    print(st.add("a"))
    print(st.add("b"))
    print(st.add("ab"))
    print(st.add("ba"))

    print(st.contains("ba"))

    print(st.getPosition("ba"))
    print(st.getPosition("ab"))
