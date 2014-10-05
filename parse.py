import sqlite3 as lite
import sys
import re
import mmap

try:
  con=lite.connect("test.sqlite")
  cur=con.cursor()
  cur.execute("select sqlite_version()")
  data=cur.fetchone()
  print("sqlite version: ",data)

  cur.execute("drop table if exists 'spanish-english'")
  cur.execute("create table 'spanish-english'(spanish text, english text, type text)")

  cur.execute("insert into 'spanish-english' values('a','b','c')")

  dictionary=open("spanish_dictionary_new.dict")
  frequency=open("most_used_words.txt")

  #mmap is a special package that supports memory-mapped files.
  #by creating this mmapped object, we don't need to load the
  #file into memory
  freq=mmap.mmap(frequency.fileno(),0,access=mmap.ACCESS_READ)

  for line in dictionary:

    m=re.match(r"([a-z]*)\s*([a-z]*):\s*([a-z,\s]*)",line)

    if m:
      spanish=m.group(1)
      vocab_type=m.group(2)
      english=m.group(3)

      if freq.find(spanish)!=-1:
        print("found a common word")
        cur.execute("insert into 'spanish-english' values(?,?,?)",(spanish,vocab_type,english))

except lite.Error, e:
  print("error: ",e)
  sys.exit(1)

finally:
  if con:
    con.commit()
    con.close()

  if dictionary:
    dictionary.close()
