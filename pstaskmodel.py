import sqlite3


class TaskModel:
    def __init__(self):
        self.conn = sqlite3.connect('sep30.sqlite')
        self.cur = self.conn.cursor()

    def dump_tasks(self, tasks):
        """create task"""
        query = 'insert into tasks (title, description, done) values (?, ?, ?)'
        self.cur.executemany(query, tasks)
        self.conn.commit()

    def get_task(self, task_id):
        query = f'select * from tasks where id = {task_id}'
        self.cur.execute(query)
        headers = [column_info[0] for column_info in self.cur.description]
        return dict(zip(headers, self.cur.fetchone()))

    def get_tasks(self):
        query = 'select * from tasks'
        self.cur.execute(query)
        headers = [column_info[0] for column_info in self.cur.description]
        tasks = [dict(zip(headers, task)) for task in self.cur.fetchall()]
        return tasks

    def delete_task(self, task_id):
        query = f'delete from tasks where id = {task_id}'
        self.cur.execute(query)
        self.conn.commit()
        return 'Success'

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    tasks = [['learn Python', 'learning Python', False],
             ['groceries list', 'milk,bread,cheese,butter,slat', False],
             ['buy stationery', 'envelope,bands,pens', False]]
    from pprint import pprint as pp

    model = TaskModel()
    model.dump_tasks(tasks)
    pp(model.get_tasks())
    print()
    pp(model.get_task(1))
