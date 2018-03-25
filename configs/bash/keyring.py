#!/usr/bin/env/ python3
import os

#Get archive key and get rid of strange apt behavior
def fetch():
    os.system("wget -q -O - https://archive.kali.org/archive-key.asc  | apt-key add && apt-get update >> bootstrap_log.md")
