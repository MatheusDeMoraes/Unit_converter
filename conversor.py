import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def on_destroy(self, *args):
        Gtk.main_quit()

    def on_bl_pressed(self, button):
        print("Hello World")

builder = Gtk.Builder()
builder.add_from_file("Conversor1.glade")

# conexão dos sinais
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

options = [['ID1,''Volume'], ['ID2','Energia']]

for option in options:
    self.liststore.append(option)



energy = [
         ["joule (J)", 1],
         ["kilojoule (kJ)", 1000],
         ['kilowatt-hora (kWh)', 3.6e+06],
         ["caloria (cal)", 4.184],
         ['kilocaloria (kcal)', 4184],
         ['elétron-volt (eV)', 1.60218e-19],
         ["BTU", 1055.06]
         ]

volume = [
         ['litro (L)', 1],
         ['metro cúbico (m³)', 1000],
         ['centímetro cúbico (cm³)', 0.001],
         ['galão (gal)', 3.78541],
         ['onça fluida (fl oz)', 0.0295735]
         ]




Gtk.main()
