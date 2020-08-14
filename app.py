
from flask import Flask
import os
import redis

app = Flask(__name__)
r = redis.Redis(host="redis-server")
r.mset({"visit-count":"0"})

@app.route("/")
def hello():
    visit_count = int(r.get("visit-count"))
    visit_count = visit_count + 1
    r.mset({"visit-count":str(visit_count)})
    return "New Version 2 !! Visit Count is :"+str(visit_count)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
