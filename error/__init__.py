import check50
import check50.c

@check50.check()
def exists():
    """Error.java exists"""
    check50.exists("Error.java")

@check50.check(exists)
def test1():
    """Error Fixed"""
    check50.run("java Error.java").stdout("Radius: 907.46\n").stdout(check50.EOF).exit(0)
