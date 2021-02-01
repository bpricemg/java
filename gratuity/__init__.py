import check50
import check50.c

@check50.check()
def exists():
    """Gratuity.java exists"""
    check50.exists("Gratuity.java")

@check50.check(exists)
def test1():
    """15% of $10"""
    check50.run("java Gratuity.java").stdin("10\n").stdin("15\n").stdout("The gratuity is $1.5 and the total is $11.5\n").stdout(check50.EOF).exit(0)
