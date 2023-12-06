class Stairs:
    def __init__(self, step: int) -> None:
        self.step = step

    def up(self):
        self.step += 1

    def down(self):
        self.step -= 1

    def show_step(self):
        print(self.step)


stairs = Stairs(0)
stairs.up()
stairs.up()
stairs.up()
stairs.up()
stairs.up()
stairs.show_step()
stairs.down()
stairs.down()
stairs.show_step()
