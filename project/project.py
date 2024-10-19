import argparse
import sys   
import ArgsManager
import csv
from AppCsv import Csv , Csv
import base64
from cryptography.fernet import Fernet
def main():
    args = ArgsManager.ArgsManager(argparse.ArgumentParser())
    try:
        input_file = Csv(args.input_file)
        output_file = Csv(args.output_file)
    except:
        sys.exit()        
    do = encrypt if args.what_to_do == 'e' else decrypt
    key = args.code
    manag(input_file,output_file,do,key)

def generate_key(code, n):
    for i in range(n):
        k = i % len(code)
        yield to_b_64ecode(code[k])
def to_b_64ecode(key):
    key_bytes = key.encode()
    key_bytes = key_bytes + b'\0' * (32 - len(key_bytes))
    return base64.urlsafe_b64encode(key_bytes)

def encrypt(data,generate_key):
    for field in data:
        key = next(generate_key)
        enc = Fernet(key)
        data[field] = enc.encrypt(data[field].encode()).decode()
    return data
        

def decrypt(data,generate_key):
    for field in data:
        key = next(generate_key)
        dec = Fernet(key)
        data[field] = dec.decrypt(data[field].encode()).decode()
    return data

def manag(input_file,output_file,do,key):
    with open(input_file.file) as input_f:
        with open(output_file.file,'w') as output_f:
            inp = csv.DictReader(input_f)
            out = csv.DictWriter(output_f,fieldnames=inp.fieldnames)
            out.writeheader()
            for row in inp:
                generate = generate_key(key,len(row))
                out.writerow(do(row,generate))

                    

if __name__ == '__main__':
    main()
    