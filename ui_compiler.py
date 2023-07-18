import os

if __name__ == '__main__':
    os.system('pyuic5 ui/game_room.ui -o ui/ui_game_room.py')
    os.system('pyuic5 ui/log_in.ui -o ui/ui_log_in.py')
    os.system('pyuic5 ui/opening.ui -o ui/ui_opening.py')
    os.system('pyuic5 ui/sign_up.ui -o ui/ui_sign_up.py')
    os.system('pyuic5 ui/start_page.ui -o ui/ui_start_page.py')
    os.system('pyuic5 ui/result.ui -o ui/ui_result.py')

# import os
# import sys
#
# if __name__ == '__main__':
#     os.system(f"pyrcc5 ../src_img/my_qrc.qrc -o my_qrc_rc.py")
#
#     uis = ['game_room', 'log_in', 'opening', 'result', 'sign_up', 'start_page']
#     for ui in uis:
#         # os.system(f'python  -m PyQt5.uic.pyuic --from-imports -x {ui}.ui -o ui_class_{ui}.py')
#         os.system(f'python  -m PyQt5.uic.pyuic --import-from=Source.front.ui -x {ui}.ui -o ui_class_{ui}.py')