import database as db

db = db.Database("python_mvc")
db.setLocalhost("localhost")
db.setUsername("root")
db.setPassword("")
db.createDatabase()

db.setTableName("customers")
db.createTable()
