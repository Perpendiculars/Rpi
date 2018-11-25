from button_class import buttonRpi

def new_callback_btn(channel):
    print("new callback!\n")

# You can set event
btn = buttonRpi(37, new_callback_btn)
btn.set_event()

# Or you can work with button in cycle
try:
    while(1):
        if btn.get_state():
            print("Key pushed!\n")
except KeyboardInterrupt:
    pass

print("\nProgram terminated...\n")

# Clean GPIO
btn.clean()
