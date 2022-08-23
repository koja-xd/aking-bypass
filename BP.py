# Author Mr MJ

# Github : https://github.com/Koja-xd

 #!/usr/bin/python2

# -*- coding: utf-8

import os,sys,time

def psb(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.02)

def po(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.003)        

def main():

    time.sleep(1)

    os.system ('clear')

    print """
 \033[1;97m##    ##  #######        ##    ###    
 \033[1;97m##   ##  ##     ##       ##   ## ##   
 \033[1;97m##  ##   ##     ##       ##  ##   ##  
 \033[1;97m#####    ##     ##       ## ##     ## 
 \033[1;97m##  ##   ##     ## ##    ## ######### 
 \033[1;97m##   ##  ##     ## ##    ## ##     ## 
 \033[1;97m##    ##  #######   ######  ##     ## 
 \033[1;97m___________________________________________
 \033[1;91m[ ] FUCK YOU ALL
\033[1;92m [ ] ENTER KOJA XD
\033[1;91m [ ] WE ARE NOT SAME BRO
\033[1;92m [ ] MR.KOJA ON FIRE'
 \033[1;97m___________________________________________
"""
    psb ('\n\x1b[1;91m\n [1] FILE AKING  \033[96;5m[BYPASS]')
    psb ('\n\x1b[1;93m [0] Exit ')
    gans = raw_input ('\n\n[91m Choice : [93m ')

    if gans in ['1']:
        time.sleep(1)
        os.system('python AKING.py')
        exit()

    if gans in ['0']:
        time.sleep(2)
        exit()
    else:
        time.sleep(1)
        psb('\t\t\n              WRONG NUMBER')
        time.sleep(3)
        main()

main()



