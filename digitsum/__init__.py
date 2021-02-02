import check50
import check50.c

@check50.check()
def exists():
    """DigitSum.java exists"""
    check50.exists("DigitSum.java")

@check50.check(exists)
def test1():
    """6.25% of $9.25"""
    check50.run("java DigitSum.java").stdin("-102\n", prompt=False)stdout("-3").exit(0)    
