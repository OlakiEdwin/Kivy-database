from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import sqlite3

Window.size = (350, 600)

class MyApp(MDApp):
    def build(self):
        con = sqlite3.connect("btel.db")
        c = con.cursor()
        c.execute("CREATE TABLE if not exists Items(item_name text)")
        con.commit()
        con.close()
        db_display = Builder.load_file("btel_db.kv")
        return db_display

    def submit(self):
        con = sqlite3.connect("btel.db")
        c = con.cursor()
        c.execute("INSERT INTO Items VALUES (:item_name)",
                  {
                      "item_name": self.root.ids.item_name.text,
                  }
                  )
        self.root.ids.item.text = f'{self.root.ids.item_name.text} has been added'
        # self.root.ids.item.text = "item successfully inserted into db"
        self.root.ids.item_name.text = ""
        con.commit()
        con.close()

    def show_items(self):
        con = sqlite3.connect("btel.db")
        c = con.cursor()
        c.execute("SELECT * FROM Items")
        items = c.fetchall()
        data = ""
        for item in items:
            data = f'{data}\n {item[0]}'
            self.root.ids.item.text = f'{data}'
        con.commit()
        con.close()


if __name__ == "__main__":
    MyApp().run()