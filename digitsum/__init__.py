import check50
import check50.c

@check50.check()
def exists():
    """DigitSum.java exists"""
    check50.exists("DigitSum.java")

@check50.check(exists)
def test1():
    """Digit sum of 932 is 14"""
    check50.run("java DigitSum.java").stdin("932").stdout("14").exit(0)
