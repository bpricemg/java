import check50
import check50.c

@check50.check()
def exists():
    """DigitSum.java exists"""
    check50.exists("DigitSum.java")

@check50.check(exists)
def test1():
    """-102 yields -3"""
    check50.run("java DigitSum.java").stdin("-102\n", prompt=False).stdout("-3").exit(0)

@check50.check(exists)
def test2():
    """402 yields 6"""
    check50.run("java DigitSum.java").stdin("402\n", prompt=False).stdout("6").exit(0)  
