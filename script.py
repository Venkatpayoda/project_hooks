import commands

result = commands.getstatusoutput("python test.py")

if result[0] == 0 and "FAIL:"not in result[1]:
    print "Test Pass"
else:
    print "Test Fails"
