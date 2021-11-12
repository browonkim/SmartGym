class BoundingBox:
    def __init__(self, box: list):
        self.x1, self.y1, self.width, self.height = box[0], box[1], box[2], box[3]
        self.x2, self.y2 = (self.x1 + self.width), (self.y1 + self.height)

    def __str__(self):
        return "LeftTop = " + str((self.x1, self.y1)) + "RightDown = " + str((self.x2, self.y2))

def check_available(human_box: BoundingBox, machine_box: BoundingBox):
    x, x2, y, y2 = human_box.x1, human_box.x2, human_box.y1, human_box.y2
    tx, ty, th, tw = machine_box.x1, machine_box.y1, machine_box.height, machine_box.width
    if x > x2:
        x, x2 = x2, x
    if y > y2:
        y, y2 = y2, y
    if x < tx + tw and x2 > tx and y < ty + th and y2 > ty:
        a = max(x, tx)
        b = max(y, ty)
        a2 = min(x2, tx + tw)
        b2 = min(y2, ty + th)
        area = (a2 - a) * (b2 - b)
        if area > tw * th / 2:
            return True
        else:
            return False
    else:
        return False
    