import check50
import check50.c

@check50.check()
def exists():
    """DigitSum.java exists"""
    check50.exists("DigitSum.java")

@check50.check()
def test1():
    """Sum of digits 932 is 14"""
    check50.run("java DigitSum").stdin("932").stdout("The sum of the digits is 14\n").exit(0)

@check50.check()
def test2():
    """Sum of digits 23 is 5"""
    check50.run("java DigitSum.java").stdin("23").stdout("The sum of the digits is 5\n").exit(0)

@check50.check()
def test3():
    """Sum of digits -932 is -14"""
    check50.run("java DigitSum.java").stdin("-932").stdout("The sum of the digits is -14\n").exit(0)
    
@check50.check()
def test4():
    """Sum of digits 0 is 0"""
    check50.run("java DigitSum.java").stdin("0").stdout("The sum of the digits is 0\n").exit(0)
