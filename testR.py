import subprocess as sub

try:
    p = sub.Popen(["dir"], shell=True, stdout=sub.PIPE)
    for x in p.stdout:
        print(x)
except:
    print("kurwa")