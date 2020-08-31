from sqlalchemy import create_engine, MetaData, Table, insert, func, select
from sqlalchemy.sql import and_, or_
from core import app

engine = create_engine(app.config['DATABASE_URI'])

#creating a class Mos_user_details for the table mos_user_details 
class Mos_mem_details():
    def __init__(self):
        try:
            self.meta = MetaData()
            self.mos_user_details = Table("mos_user_details", self.meta, autoload=True, autoload_with=engine)
            self.mos_user_address = Table("mos_user_address", self.meta, autoload=True, autoload_with=engine)
            self.mos_qualifications = Table("mos_qualifications", self.meta, autoload=True, autoload_with=engine)
            self.mos_prof_att = Table("mos_prof_att", self.meta, autoload=True, autoload_with=engine)
            self.mos_awards = Table("mos_awards", self.meta, autoload=True, autoload_with=engine)
        except Exception as e:
            print(e)

    #operations on Personalia page..
    def insert_personalia(self, data):
        print('inside model insert personalia')
        result = engine.execute(self.mos_user_details.insert(), data)
        return result

    def get_user_id(self):
        print('inside get user id')
        result = engine.execute(select([func.max(self.mos_user_details.c.User_id)]))
        results = [dict(r) for r in result] if result else None
        print(results)
        return(results[0]['max_1'])

    def get_personalia(self,user_id):
        print('inside get_personalia')
        stmt = select([self.mos_user_details]).where(self.mos_user_details.c.User_id.in_([user_id]))
        result = engine.execute(stmt)
        results = [dict(r) for r in result] if result else None
        print(results[0])
        return results[0]
    
    def update_personalia(self,id,data):
        print('inside update personalia model')
        stmt = self.mos_user_details.update().where(self.mos_user_details.c.User_id.in_([id]))
        result = engine.execute(stmt,data)

    #operations on Communication page..    
    def insert_communication(self, data):
        print('inside model insert communication')
        result = engine.execute(self.mos_user_address.insert(), data)
        return result

    def get_address(self,user_id):
        print('inside get_address')
        stmt = select([self.mos_user_address]).where(self.mos_user_address.c.User_id.in_([user_id]))
        result = engine.execute(stmt)
        results = [dict(r) for r in result] if result else None
        if results:
            print(results[0])
            return results[0]
        else:
            return results

    def update_communication(self,id,data):
        print('inside update communication model')
        stmt = self.mos_user_address.update().where(self.mos_user_address.c.User_id.in_([id]))
        result = engine.execute(stmt,data)
    
    #operations on Qualifications page..
    def insert_qualifications(self, data):
        print('inside model insert qualifications')
        result = engine.execute(self.mos_qualifications.insert(), data)
        return result

    def get_qualifications(self,user_id):
        print('inside get_qualifications')
        stmt = select([self.mos_qualifications]).where(self.mos_qualifications.c.User_id.in_([user_id]))
        result = engine.execute(stmt)
        results = [dict(r) for r in result] if result else None
        print(results)
        if results:
            return results
        else:
            return None

    def update_qualifications(self,data,id=0):
        print(id)
        print('inside update qualifications model')
        stmt = self.mos_qualifications.update().where(self.mos_qualifications.c.Qual_id.in_([id]))
        result = engine.execute(stmt,data)
        print(result.rowcount)

    def delete_qualifications(self,id):
        print('inside delete')
        stmt = self.mos_qualifications.delete().where(self.mos_qualifications.c.Qual_id.in_([id]))
        result = engine.execute(stmt)

    #operations on Professional attachment page..
    def insert_prof_att(self,data):
        print('inside model insert prof att')
        result = engine.execute(self.mos_prof_att.insert(),data)
        return result

    def insert_awards(self, data):
        print('inside model insert awards')
        result = engine.execute(self.mos_awards.insert(), data)
        return result

    
