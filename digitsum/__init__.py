import check50
import check50.c

@check50.check()
def exists():
    """DigitSum.java exists"""
    check50.exists("DigitSum.java")

@check50.check()
def test1():
    """-102 yields -3"""
    check50.run("java DigitSum.java").stdin("-102\n", prompt=False).stdout("-3").exit(0)
    
@check50.check()
def test2():
    """-10 yields -1"""
    check50.run("java DigitSum.java").stdin("-10\n", prompt=False).stdout("-1").exit(0)
