import check50
import check50.c

@check50.check()
def exists():
    """Gratuity.java exists"""
    check50.exists("Gratuity.java")

@check50.check(exists)
def test1():
    """6.25% of $9.25"""
    check50.run("java Gratuity.java").stdin("9.25\n", prompt=False).stdin("6.25\n", prompt=False).stdout("0.58").stdout("9.83").exit(0)    
