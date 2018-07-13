import datetime
import time
import os

class Migration:
    def generate(self, args):
        if args.g == None:
            return os.system('bast_cli -h')

        if args.g[0] == 'create:migration' and type(args.g[1]) == str:
            filename = args.g[1] + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")
            self.migration_creator(filename, args.g[1])
            print("\033[1;35;40m >> Bast Framework <<")
            print("\033[1;32;40m [OK] migrations/" + filename + " Migration generated successfully")
        else:
            print("\033[1;31;40m Command not found ")
            os.system("bast_cli -h")

    def migration_creator(self, filename, realname):
        file_name = str(filename+'.py')
        migration_dir = 'bast/migrations/'
        if os.path.isdir(migration_dir):
            file_migrate = open(migration_dir+file_name, 'w+')
            compose = "from app.database.flask_migrate import execute\n\n"
            compose += "class "+realname+"(db.Model):\n\t"
            compose += "id = db.Column(db.Integer, primary_key=True)"
            file_migrate.write(compose)
            file_migrate.close()
        else:
            print "Directory 'migrations' missing or deleted"