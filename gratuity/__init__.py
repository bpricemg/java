import check50
import check50.c

@check50.check()
def exists():
    """Gratuity.java exists"""
    check50.exists("Gratuity.java")

@check50.check(exists)
def test1():
    """15% of $10"""
    check50.run("java Gratuity.java").stdin("10\n").stdin("15\n").stdout("1.5").stdout("11.5").exit(0)
    
@check50.check(exists)
def test2():
    """17% of $10"""
    check50.run("java Gratuity.java").stdin("10\n").stdin("17\n").stdout("1.7").stdout("11.7").exit(0)
