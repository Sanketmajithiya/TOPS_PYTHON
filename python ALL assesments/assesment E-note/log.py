from datetime import datetime

def log_file(Details):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file = open('log.txt','a')
    file.write(f"{current_datetime}:{Details}\n") 
    
message = "hello world"




