# pyscript module to access DOM // importo el módulo de pyscript que permite la manipulación del DOM
import pyscript as ps
# that class will be instanced // esta clase será la encargada de instanciar la app
class App():
    def __init__(self):
        self.DOM = ps.Element('MainBox')
    # that method will be called in main.py file // este método será llamado
    def run(self):
        self.DOM.write("Hello World!")