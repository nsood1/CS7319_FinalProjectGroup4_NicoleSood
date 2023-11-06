import sqlite3
conn = sqlite3.connect('therapy.db')
cursor = conn.cursor()

def generaterecent():
    cursor.execute('SELECT WORD, RESPONSE FROM RESPONSE')
    rows = cursor.fetchall()
    with open('data.txt', 'w') as file:
        for row in rows:
            word, response = row
            file.write(f"{word}\n{response}\n")

def restore():
    conn = sqlite3.connect('therapy.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(WORD) FROM RESPONSE')
    count = cursor.fetchone()[0]
    if count == 0:
        with open('tempdata.txt', 'r') as file:
            lines = file.readlines()
        for i in range(0, len(lines), 2):
            phases = lines[i].strip()
            response = lines[i+1].strip()
            cursor.execute('INSERT INTO RESPONSE (WORD, RESPONSE) VALUES (?, ?)', (phases, response))
    conn.commit()
    conn.close()


def add():
    conn = sqlite3.connect('therapy.db')
    cursor = conn.cursor()
    prompt = input("Prompt: ")
    resp = input("Response: ")
    cursor.execute('INSERT INTO RESPONSE (WORD, RESPONSE) VALUES (?, ?)', (prompt, resp))
    conn.commit()

conn.commit()
#conn.close()