import sqlite3 as lite
import sys
import re

try:
  con=lite.connect("test.sqlite")
  cur=con.cursor()
  cur.execute("select sqlite_version()")
  data=cur.fetchone()
  print("sqlite version: ",data)

  cur.execute("drop table if exists 'spanish-english'")
  cur.execute("create table 'spanish-english'(spanish text, english text, type text)")

  cur.execute("insert into 'spanish-english' values('a','b','c')")

  file=open("spanish_dictionary_new.dict")

  for line in file:

    m=re.match(r"([a-z]*)\s*([a-z]*):\s*([a-z,\s]*)",line)

    if m:
      spanish=m.group(1)
      vocab_type=m.group(2)
      english=m.group(3)

      cur.execute("insert into 'spanish-english' values(?,?,?)",(spanish,vocab_type,english))

except lite.Error, e:
  print("error: ",e)
  sys.exit(1)

finally:
  if con:
    con.commit()
    con.close()
