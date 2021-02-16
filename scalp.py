import os
import time
#Executing a shell command
os.system('ipfs add -r Documents > docs.scalp')

time.sleep(120)
os.system('ipfs add -r Downloads > down.scalp')