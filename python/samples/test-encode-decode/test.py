import json
import base64

def read():
  # BASE64を読み込み
  with open('./sample.json', mode='rb') as f:
      data = f.read()
      data = base64.b64decode(data)
      print(data)
      data = data.decode('utf-8')
      data = json.loads(data)
      print(data)

      print(data['StringField'])
      print(data['FloatField'])
      print(data['BooleanField'])

def save():
  import json
  import base64
  
  data = {"StringField":"test","FloatField":123,"BooleanField":False}
  
  # BASE64で保存
  with open('./sample.json', mode='wb') as f:
      data = json.dumps(data)
      data = data.encode('utf-8')
      data = base64.b64encode(data)
      f.write(data)

save()
read()