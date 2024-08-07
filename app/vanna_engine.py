import os
import uuid

from dotenv import load_dotenv
from vanna.remote import VannaDefault
import vanna

# api_key = vanna.get_api_key('cicitan@hotmail.com')
class MyVanna:
    def __init__(self):
        self.vn = VannaDefault(model='zju_test2', api_key=os.environ.get("VANNA_API_KEY"))
        self.vn.connect_to_mysql(
            host=os.environ.get("MYSQL_HOST"),
            dbname=os.environ.get("MYSQL_DATABASE"),
            user=os.environ.get("MYSQL_USER"),
            password=os.environ.get("MYSQL_PASSWORD"),
            port=int(os.environ.get("MYSQL_PORT")))

    def trainning_plan(self):
        # trainning plan of RAG model for understanding metadata
        df_information_schema = self.vn.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'dim_crawl_policy'")
        plan = self.vn.get_training_plan_generic(df_information_schema)
        self.vn.train(plan=plan)

    def train_doc(self, docs):
        # docs about your data
        self.vn.train(documentation=docs)

    def get_sql_response(self, query):
        """
        Get the response of the query
        :param query: the query asked by user
        :return: the response [sql_query, df, plot_figure]
        """
        res = self.vn.ask(query)
        if not res:
            return None
        fig_id = str(uuid.uuid1())
        fig_path = f"./ui/images/tmp/{fig_id}.png"
        res[2].write_image(fig_path)
        return [res[1], fig_path.split('ui/')[1]]

    def get_summary_response(self, query, df):
        summary = self.vn.generate_summary(query, df)
        return summary

if __name__ == '__main__':
    load_dotenv()
    vn = MyVanna()
    res = vn.get_sql_response("每个城市的政策分别有多少")
    print('------------',res)