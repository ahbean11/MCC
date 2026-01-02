[app]

# Tên ứng dụng
title = Tool Cham Cong
package.name = chamcong
package.domain = org.test

# Source code
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 1.0

# Các thư viện cần thiết
requirements = python3,kivy,pyzk

# Cấu hình hiển thị
orientation = portrait
fullscreen = 0

# --- CẤU HÌNH IOS QUAN TRỌNG (ĐÃ SỬA) ---
[buildozer]
log_level = 2
warn_on_root = 1

[app:ios]
# Quyền truy cập mạng LAN (Bắt buộc)
ios.plist_key_NSLocalNetworkUsageDescription = "Ứng dụng cần truy cập mạng nội bộ để kết nối máy chấm công"
ios.plist_key_NSBonjourServices = _http._tcp.

# --- PHẦN SỬA LỖI CHÍNH Ở ĐÂY ---
# Báo cho Buildozer biết không cần kiểm tra chứng chỉ Code Sign xịn
ios.codesign.allowed = false
ios.codesign.debug = "iPhone Developer"
ios.codesign.release = "iPhone Distribution"

# Các đường dẫn Github (giữ nguyên)
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.branch = master
ios.ouput_dir = bin
