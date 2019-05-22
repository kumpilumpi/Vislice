import Bottle
import model

vislice = model.Vislice()

@Bottle.get('/')
def index():
    return Bottle.template('index.tpl')

Bottle.run(reloader = True, debug = True)


