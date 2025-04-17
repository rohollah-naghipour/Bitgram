# gunicorn.conf.py
bind = "0.0.0.0:8000"  # یا پورت مورد نظر
workers = 3  # تعداد workerها (معمولاً 2 * تعداد coreهای CPU + 1)
timeout = 120  # زمان انتظار برای هر درخواست (ثانیه)
accesslog = "-"  # لاگ دسترسی (می‌توانید مسیر فایل را مشخص کنید)
errorlog = "-"   # لاگ خطاها
worker_tmp_dir = "/dev/shm"  # برای performance بهتر