from database.DB_connect import DBConnect
from model.Airport import Airport
from model.FlightObject import FlightObject
from model.Tratta import Tratta


class DAO():

    @staticmethod
    def getAllNodes(n,idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res=[]

        query = """select t.IATA_CODE,t.ID, count(*) as N
                from (select f.AIRLINE_ID ,a.IATA_CODE, a.ID
                from flights f, airports a 
                where a.ID  = f.DESTINATION_AIRPORT_ID  or f.ORIGIN_AIRPORT_ID =a.ID 
                group by f.AIRLINE_ID ,a.IATA_CODE, a.ID) t
                group by t.IATA_CODE,t.ID 
                having N >= %s"""

        cursor.execute(query,(n,))
        for row in cursor:
            res.append(idMap[row["ID"]])


        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getAllEdges(idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """select f.DESTINATION_AIRPORT_ID ,f.ORIGIN_AIRPORT_ID, count(*) as peso
                from  flights f 
                group by f.DESTINATION_AIRPORT_ID ,f.ORIGIN_AIRPORT_ID 
                order by f.DESTINATION_AIRPORT_ID ,f.ORIGIN_AIRPORT_ID"""

        cursor.execute(query)
        for row in cursor:
            res.append(Tratta(idMap[row["ORIGIN_AIRPORT_ID"]],
                              idMap[row["DESTINATION_AIRPORT_ID"]],
                              row["peso"]))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * from airports a order by a.AIRPORT asc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result









