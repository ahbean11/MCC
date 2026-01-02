[app]

# --- CẤU HÌNH BẮT BUỘC (ĐỂ KHÔNG BỊ LỖI) ---
# Đặt dòng này ngay dưới [app] để chắc chắn buildozer đọc được
ios.codesign.allowed = false

# Thông tin cơ bản
title = Tool Cham Cong
package.name = chamcong
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 1.0

# Thư viện
requirements = python3,kivy,pyzk

# Cấu hình màn hình
orientation = portrait
fullscreen = 0

# Cấu hình iOS (Nằm trong section app nhưng có tiền tố ios.)
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.branch = master
ios.ouput_dir = bin

# Quyền mạng LAN (Quan trọng cho App chấm công)
ios.plist_key_NSLocalNetworkUsageDescription = "App can truy cap mang LAN de ket noi may cham cong"
ios.plist_key_NSBonjourServices = _http._tcp.

# Cấu hình chứng chỉ ảo (để bypass lỗi)
ios.codesign.debug = "iPhone Developer"
ios.codesign.release = "iPhone Distribution"

[buildozer]
log_level = 2
warn_on_root = 1
