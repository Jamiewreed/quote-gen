rom flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  s = sched.scheduler(time.time, time.sleep)

def quote_gen_exe(sc):

    folder="D:\\Jamie\\Python Projects\\Quote Gen\\Image quote gen\\Images"

    a=random.choice(os.listdir(folder))
    print(a)

    file=folder + '\\' + a
    Image.open(file).show()

    s.enter(15, 1, quote_gen_exe, (sc,))

s.enter(15, 1, quote_gen_exe, (s,))
s.run()
