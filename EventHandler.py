import cv2

class EventHandler:
    class Square:
        def __init__(self, x1=-1, y1=-1, x2=-1, y2=-1):
            self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

        def set_starting_point(self, x, y):
            self.x1, self.y1 = x, y

        def set_end_point(self, x, y):
            self.x2, self.y2 = x, y

        def starting_point(self):
            return self.x1, self.y1

        def end_point(self):
            return self.x2, self.y2

    def __init__(self, cap, win_name):
        self.x0, self.y0, self.is_drawing, self.frame = -1, -1, False, None
        self.list_of_square = []
        self.current = self.Square()
        self.cap, self.window_name = cap, win_name

    def click_down(self, x, y):
        self.is_drawing = True
        self.x0, self.y0 = x, y
        self.current.set_starting_point(x, y)
        self.current.set_end_point(x,y)

    def mouse_move(self, x, y):
        if self.is_drawing:
            self.current.set_end_point(x, y)

    def click_up(self, x, y):
        self.is_drawing = False
        self.list_of_square.append(self.Square(self.x0, self.y0, x, y))

    def result(self):
        return [(x.x1, x.y1, abs(x.x2-x.x1), abs(x.y2-x.y1)) for x in self.list_of_square]

    def running(self):
        while True:
            ret, self.frame = self.cap.read()
            for square in self.list_of_square:
                cv2.rectangle(self.frame, square.starting_point(), square.end_point(), (255, 255, 0), 2)
            if self.is_drawing:
                cv2.rectangle(self.frame, self.current.starting_point(), self.current.end_point(), (255, 0, 0), 2)
            cv2.imshow(self.window_name, self.frame)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            elif k == 8:
                if len(self.list_of_square) != 0:
                    self.list_of_square.pop(-1)

    def roi(self, number_of_machines):
        while True:
            self.running()
            if len(self.list_of_square) == number_of_machines:
                break

