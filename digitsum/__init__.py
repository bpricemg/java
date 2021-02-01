import check50
import check50.c

@check50.check()
def exists():
    """DigitSum.java exists"""
    check50.exists("DigitSum.java")

@check50.check(exists)
def test1():
    """Proper computation"""
    check50.run("java DigitSum.java").stdin("44").stdout("8\n").stdout(check50.EOF).exit(0)
