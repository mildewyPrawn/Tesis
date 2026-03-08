class Button:
    def __init__(self, x, y, w, h, label, callback):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.label = label
        self.callback = callback

    def display(self):
        if self.is_over():
            fill(180)
        else:
            fill(240)

        rect(self.x, self.y, self.w, self.h, 8)
        fill(0)
        textAlign(CENTER, CENTER)
        text(self.label, self.x + self.w/2, self.y + self.h/2)

    def is_over(self):
        return self.x < mouseX < self.x + self.w and \
               self.y < mouseY < self.y + self.h

    def click(self):
        if self.is_over():
            self.callback()
