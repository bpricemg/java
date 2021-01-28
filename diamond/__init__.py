import check50
import check50.c

@check50.check()
def exists():
    """Diamond.java exists"""
    check50.exists("Diamond.c")

@check50.check(exists)
def test1():
    """Displays a Diamond"""
    check50.run("java Diamond.java").stdout("   D\n  I I\n A   A\nM     M\n O   O\n  N N\n   D\n").stdout(check50.EOF).exit(0)
