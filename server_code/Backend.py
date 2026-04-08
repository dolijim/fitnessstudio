import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_Kurs():
  with sqlite3.connect(data_files['Bitschnau_Chiara_fitnessstudio.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
      SELECT 
        k.bezeichnung,
        k.wochentag,
        k.uhrzeit,
        t.vorname || ' ' || t.nachname AS trainer,
        COUNT(b.mitgliedid) AS teilnehmer,
        k.maxteilnehmer
      FROM Kurs k
      LEFT JOIN Trainer t ON k.trainerid = t.trainerid
      LEFT JOIN besucht b ON k.kursid = b.kursid
      GROUP BY k.kursid
    """).fetchall()
    return [dict(row) for row in result]

@anvil.server.callable
def get_Mitglied():
  with sqlite3.connect(data_files['Bitschnau_Chiara_fitnessstudio.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
      SELECT 
        m.vorname || ' ' || m.nachname AS mitglied FROM Mitglied m
    """).fetchall()
    return [dict(row) for row in result]