#!/usr/bin/env python3
import keyring

def bootstrap():
    keyring.fetch() 

if __name__ == '__main__':
    bootstrap()         
