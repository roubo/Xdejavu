#!/usr/bin/env python
# encoding: utf-8

from dejavu import Dejavu
from dejavu.recognize import MicrophoneRecognizer
from dejavu.recognize import FileRecognizer

"configure setting"
config = {
  "database" : {
    "host"   : "127.0.0.1",
    "user"   : "root",
    "passwd" : "",
    "db"     : "dejavu",
  }
}

djv = Dejavu(config)
djv.fingerprint_directory("roubotest", [".mp3"], 3)
print djv.db.get_num_fingerprints()
print djv.recognize(MicrophoneRecognizer, seconds=10)
#print djv.recognize(FileRecognizer, "roubotest/艾怡良-我不知道爱是什么.m4a.mp3")
