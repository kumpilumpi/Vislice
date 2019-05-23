import Bottle
import model

Bottle.TEMPLATE_PATH.insert(0, 'C:\\Users\\jakak\\Desktop\\Git\\Vislice\\datoteke\\views')

vislice = model.Vislice()

@Bottle.get('/')

def index():
    return Bottle.template('index.tpl')

Bottle.run(reloader = True, debug = True)


