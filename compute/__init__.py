import check50
import check50.c

@check50.check()
def exists():
    """Compute.java exists"""
    check50.exists("Compute.java")
    
@check50.check(exists)
def compiles():
    """caesar.c compiles."""
    check50.java.compile("Compute.java")

@check50.check(exists)
def test1():
    """Proper computation"""
    check50.run("java Compute.java").stdout("0.8392857142857143\n").stdout(check50.EOF).exit(0)
