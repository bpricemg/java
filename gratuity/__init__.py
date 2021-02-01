import check50
import check50.c

@check50.check()
def exists():
    """Gratuity.java exists"""
    check50.exists("Gratuity.java")

@check50.check(exists)
def test1():
    """15% of $10"""
    check50.run("java Gratuity.java").stdin("10\\n15", prompt=False).stdout("1.5z\\n11.5", regex=False).exit(0)
    
@check50.check(exists)
def test2():
    """17% of $10"""
    check50.run("java Gratuity.java").stdin("10\n", prompt=False).stdin("17\n", prompt=False).stdout("1.7").stdout("11.7").exit(0)
   
@check50.check(exists)
def test3():
    """6.25% of $10"""
    check50.run("java Gratuity.java").stdin("10\n", prompt=False).stdin("6.25\n", prompt=False).stdout("0.63").stdout("10.63").exit(0)

@check50.check(exists)
def test4():
    """6.25% of $9.25"""
    check50.run("java Gratuity.java").stdin("9.25\n", prompt=False).stdin("6.25\n", prompt=False).stdout("0.58").stdout("9.83").exit(0)    
