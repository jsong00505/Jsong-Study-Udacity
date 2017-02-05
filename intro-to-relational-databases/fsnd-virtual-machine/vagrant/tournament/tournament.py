#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("delete from matches")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("delete from players")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    query = "select count(*) from players"
    c.execute(query)
    res = c.fetchone()
    db.close()

    return res[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute("insert into players (name) values (%s)", (name,))
    db.commit()

    c.execute("select id from players where name = %s", (name,))
    id = c.fetchone()

    c.execute("insert into matches (id, wins, matches) values (%s, %s, %s)", (id, 0, 0,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    query = "select players.id, players.name, COALESCE(matches.wins,0), COALESCE(matches.matches,0) from players left join matches on players.id = matches.id order by matches.wins desc"
    c.execute(query)
    res = c.fetchall()
    db.close()

    return res

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()

    query = "select id, wins, matches from matches where id = %s"
    c.execute(query, (winner, ))
    winner_info = c.fetchone()

    query = "select id, wins, matches from matches where id = %s"
    c.execute(query, (loser,))
    loser_info = c.fetchone()

    query = "update matches set wins = %s, matches = %s where id = %s"
    c.execute(query, (winner_info[1]+1, winner_info[2]+1, winner))

    query = "update matches set matches = %s where id = %s"
    c.execute(query, (loser_info[2]+1, loser))

    db.commit()
    db.close()

 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    req = playerStandings()
    pairing = []
    i = 0

    for reqInfo1, reqInfo2 in zip(req[0::2], req[1::2]):
        pairingInfo = (reqInfo1[0], reqInfo1[1], reqInfo2[0], reqInfo2[1])
        pairing.append(pairingInfo)
    return pairing


