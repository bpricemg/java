import check50
import check50.c

@check50.check()
def exists():
    """DigitSum.java exists"""
    check50.exists("DigitSum.java")

@check50.check()
def test1():
    """Digit sum of 932 is 14"""
    check50.run("java DigitSum.java").stdin("932").stdout("14").stdout(check50.EOF).exit(0)

@check50.check()
def test2():
    """Digit sum of 93 is 12"""
    check50.run("java DigitSum.java").stdin("93").stdout("12").exit(0)
