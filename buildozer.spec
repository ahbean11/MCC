[app]

# Tên ứng dụng hiển thị
title = Tool Cham Cong
package.name = chamcong
package.domain = org.test

# Source code ở đâu (dấu chấm là thư mục hiện tại)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 1.0

# Các thư viện cần thiết (Quan trọng: phải có pyzk)
requirements = python3,kivy,pyzk

# Cấu hình iOS
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.branch = master
ios.ouput_dir = bin

# QUAN TRỌNG: Quyền truy cập mạng LAN để kết nối máy chấm công
# Nếu thiếu dòng này app sẽ crash khi bấm kết nối
ios.plist_key_NSLocalNetworkUsageDescription = "Ứng dụng cần truy cập mạng nội bộ để kết nối máy chấm công"
ios.plist_key_NSBonjourServices = _http._tcp.

[buildozer]
# Mức độ log (2 = debug)
log_level = 2
warn_on_root = 1
