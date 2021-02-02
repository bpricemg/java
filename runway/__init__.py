import check50
import check50.c

@check50.check()
def exists():
    """Runway.java exists"""
    check50.exists("Runway.java")

@check50.check(exists)
def test1():
    """Speed of 60 and acceleration on 3.5 yields 514.2857142857143"""
    check50.run("java Runway.java").stdin("60\n", prompt=False).stdin("3.5\n", prompt=False).stdout("514.2857142857143").exit(0)    
