from mongobox import MongoBox
import subprocess
import subprocess
normalized_meta_box = MongoBox()
normalized_asset_box = MongoBox()
volatile_box = MongoBox()
permanent_box = MongoBox()

normalized_meta_box.start()
normalized_asset_box.start()
volatile_box.start()
permanent_box.start()

client = normalized_meta_box.client()
proc = subprocess.Popen(['mongorestore', '--gzip', '--archive', '~/2019-04-09--06-26-21.tar.gz', 
    '--host', client.address[0],
    '--port', str(client.address[1]),
    '--numInsertionWorkersPerCollection', '88'])

while proc.poll() is None:
    print('Working...')


print('end', proc.poll())
print('end')
