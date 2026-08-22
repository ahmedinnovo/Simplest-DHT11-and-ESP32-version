from machine import Pin
import dht
import time

# تعريف طرف البيانات على GPIO 4
sensor = dht.DHT11(Pin(4))

while True:
    try:
        # أخذ القراءة الحديثة
        sensor.measure()
        
        # استخراج الحرارة والرطوبة
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        print(f"درجة الحرارة: {temp}°C | الرطوبة: {hum}%")
        
    except OSError as e:
        print("حدث خطأ في القراءة، جاري إعادة المحاولة...")
        
    # يحتاج DHT11 من ثانية إلى ثانتين بين كل قراءة وأخرى
    time.sleep(2)
