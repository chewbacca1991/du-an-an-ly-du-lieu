from django.db import models

# Định nghĩa mô hình dữ liệu bất động sản
class BatDongSan(models.Model):
    ten_du_an = models.CharField(max_length=200)
    gia = models.DecimalField(max_digits=10, decimal_places=2)
    dia_chi = models.CharField(max_length=255)
    ngay_tao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ten_du_an
