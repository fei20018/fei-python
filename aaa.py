xpin=commands.getoutput("ping -c5 60.28.9.1")
ms='time=\d+.\d+'
print xpin
print ms
mstime=re.search(ms,xpin)
print mstime
if not mstime:
        MS='timeout'
        print 'timeout'
else:
        MS=mstime.group().split('=')[1]
        print 'ss'
