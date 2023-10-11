from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import sqlite3

Window.size = (350, 600)

class MyApp(MDApp):
    def build(self):
        con = sqlite3.connect("btel.db")
        c = con.cursor()
        c.execute("CREATE TABLE if not exists users(fname text, lname text, contact text)")
        con.commit()
        con.close()
        db_display = Builder.load_file("btel_db.kv")
        return db_display

    def submit_user(self):
        con = sqlite3.connect("btel.db")
        c = con.cursor()
        c.execute("INSERT INTO users (fname, lname, contact) VALUES (:fname, :lname, :contact)",
                  {
                      "fname": self.root.ids.fname.text,
                      "lname": self.root.ids.lname.text,
                      "contact": self.root.ids.contact.text,
                  }
                  )
        self.root.ids.item.text = f'{self.root.ids.fname.text} has been added'
        self.root.ids.fname.text = ""
        self.root.ids.lname.text = ""
        self.root.ids.contact.text = ""
        con.commit()
        con.close()

    def show_users(self):
        con = sqlite3.connect("btel.db")
        c = con.cursor()
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        data = ""
        for user in users:
            data += f'{user[0]} {user[1]} - Contact: {user[2]}\n'
        self.root.ids.item.text = data
        con.commit()
        con.close()


if __name__ == "__main__":
    MyApp().run()
