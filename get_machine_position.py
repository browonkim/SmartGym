import cv2
from EventHandler import EventHandler

global event_var
event_var: EventHandler

def mouse_handler(event, x, y, flags, param):
    global event_var
    if event == cv2.EVENT_LBUTTONDOWN:
        event_var.click_down(x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        event_var.click_up(x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        event_var.mouse_move(x, y)

def get_machine_position(number_of_machines: int, cam_num: int):
    global event_var
    cap = cv2.VideoCapture(cam_num, cv2.CAP_DSHOW)
    assert cap.isOpened(), "니 카메라 꺼져있음!!!"
    w_name = 'set positions of machines'
    cv2.namedWindow(w_name)
    event_var = EventHandler(win_name=w_name, cap=cap)
    cv2.setMouseCallback(w_name, mouse_handler)
    event_var.roi(number_of_machines)
    cv2.destroyWindow(w_name)
    cap.release()
    return event_var.result()


if __name__ == "__main__":
    print(get_machine_position(3, 0))
