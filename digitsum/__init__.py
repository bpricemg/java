import check50
import check50.c

@check50.check()
def exists():
    """DigitSum.java exists"""
    check50.exists("DigitSum.java")

@check50.check(exists)
def test1():
    """Sum of digits 932 is 14"""
    check50.run("java DigitSum").stdin("932").stdout("The sum of the digits is 14\n").exit(0)
