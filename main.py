import threading
import random
from datetime import datetime, timedelta
from zk import ZK

# Kivy Imports
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock

class MCCApp(App):
    def build(self):
        self.title = "ZKTeco Time Manager"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # 1. Cấu hình IP
        self.ip_input = TextInput(text='10.33.2.199', multiline=False, size_hint=(1, 0.15), font_size=20)
        self.port_input = TextInput(text='4370', multiline=False, size_hint=(1, 0.15), font_size=20)
        
        # 2. Hiển thị trạng thái
        self.status_lbl = Label(text="Sẵn sàng", size_hint=(1, 0.2), color=(1, 1, 0, 1))

        # 3. Các nút chức năng
        btn_sync_now = Button(text="Đồng bộ giờ điện thoại", background_color=(0.2, 0.6, 1, 1))
        btn_sync_now.bind(on_press=lambda x: self.run_action("sync_phone"))

        btn_rand_sang = Button(text="Random Sáng (07:45 - 07:59)", background_color=(0, 1, 0.5, 1))
        btn_rand_sang.bind(on_press=lambda x: self.run_action("morning"))

        btn_rand_toi = Button(text="Random Tối (21:31 - 21:45)", background_color=(1, 0.5, 0, 1))
        btn_rand_toi.bind(on_press=lambda x: self.run_action("night"))

        # Add widget vào layout
        layout.add_widget(Label(text="IP Máy chấm công:", size_hint=(1, 0.1)))
        layout.add_widget(self.ip_input)
        layout.add_widget(self.status_lbl)
        layout.add_widget(btn_sync_now)
        layout.add_widget(btn_rand_sang)
        layout.add_widget(btn_rand_toi)

        return layout

    def update_status(self, message):
        # Cập nhật giao diện từ luồng khác
        Clock.schedule_once(lambda dt: setattr(self.status_lbl, 'text', message))

    def run_action(self, action_type):
        # Chạy trong luồng riêng để không đơ app
        threading.Thread(target=self._process_action, args=(action_type,)).start()

    def _process_action(self, action_type):
        ip = self.ip_input.text
        port = int(self.port_input.text)
        zk = ZK(ip, port=port, timeout=5)

        try:
            self.update_status(f"Đang kết nối đến {ip}...")
            conn = zk.connect()
            if not conn:
                self.update_status("Kết nối thất bại!")
                return

            # Xử lý logic thời gian
            now = datetime.now()
            target_time = now

            if action_type == "morning":
                # Random 07:45:00 - 07:59:59
                start = now.replace(hour=7, minute=45, second=0)
                seconds = random.randint(0, 899) # 15 phút * 60 giây - 1
                target_time = start + timedelta(seconds=seconds)
                
            elif action_type == "night":
                # Random 21:31:00 - 21:45:59
                start = now.replace(hour=21, minute=31, second=0)
                seconds = random.randint(0, 899)
                target_time = start + timedelta(seconds=seconds)
            
            elif action_type == "sync_phone":
                target_time = now

            # Thực hiện set time
            conn.set_time(target_time)
            str_time = target_time.strftime('%H:%M:%S %d/%m')
            self.update_status(f"Thành công!\nĐã set: {str_time}")

            # Đợi 5s rồi trả về giờ chuẩn (như code cũ của bạn yêu cầu)
            # Nếu không muốn tính năng này thì xóa đoạn dưới
            # import time
            # time.sleep(5)
            # conn.set_time(datetime.now()) 

            conn.enable_device()
            conn.disconnect()

        except Exception as e:
            self.update_status(f"Lỗi: {str(e)}")

if __name__ == '__main__':
    MCCApp().run()
