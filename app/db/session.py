from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import subprocess

def get_windows_host_ip():
    try:
        # Chạy lệnh shell để lấy dòng default route
        output = subprocess.check_output(['ip', 'route'], text=True)
        for line in output.splitlines():
            if line.startswith('default via'):
                parts = line.split()
                return parts[2]  # IP nằm ở vị trí thứ 3
    except Exception as e:
        print(f"Lỗi: {e}")
        return None


# Dùng file .env để bảo mật sau nhé, tạm thời dùng trực tiếp:
WINDOW_HOST = get_windows_host_ip()
DATABASE_URL = f"postgresql://postgres:tuantt@{WINDOW_HOST}:5432/onlineStore"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dùng để inject vào route
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()