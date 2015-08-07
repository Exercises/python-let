#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb

def main():
    db = MySQLdb.connect(host="localhost",
                    user="root",
                    passwd="pgd",
                    db="demo")
    db.set_character_set("utf8")
    cursor = db.cursor()
    #first = True
    first = False
    if(first):
        create_table(cursor)
    else:
        insert_into(cursor, 1, "1sdfjlsdkjfls")
        insert_into(cursor, 1, u" å¥ä¹ˆ")
        insert_into(cursor, 1, u"å½¼æ­¤'"
        insert_into(cursor, 1, u"ä½ å¥½ä¹ˆ")
        insert_into(cursor, 1, u"ä½ å¥½ä¹ˆ")
    db.commit()
    db.close()

def create_table(cursor):
    cursor.execute(
    """
    create table table_demo(
    intVal int,
    charVal varchar(255)
    )
    """
    )

def insert_into(cursor, intValue, charValue):
    sql = "insert into table_demo (intVal, charVal) values(%d, '%s')" \
          %(intValue, charValue)
    count = cursor.execute(sql)
    print "affected count " , count, "  sql : ", sql

if __name__ == "__main__":
    main()   
