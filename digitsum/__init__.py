import check50

@check50.check()
def exists():
    """DigitSum.java exists"""
    check50.exists("DigitSum.java")

@check50.check()
def test1():
    """Digit sum of 932 is 14"""
    check50.run("java DigitSum.java").stdin("932").stdout("14").exit(0)
