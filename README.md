# 🌡️ Simplest DHT11 and ESP32 version

مشروع بسيط بلغة **MicroPython** يقرأ درجة الحرارة ونسبة الرطوبة باستخدام حساس **DHT11** ولوحة **ESP32**.

---

## 🛠️ المكونات (Hardware)

* ESP32 Board
* DHT11 Sensor
* Jumper Wires

---

## 🔌 التوصيل (Wiring)

| DHT11 Pin | ESP32 Pin |
| :--- | :--- |
| **VCC** | **3.3V** |
| **Data** | **GPIO 4** |
| **GND** | **GND** |

---

## 🚀 التشغيل (Usage)

ارفع ملف `main.py` على الـ ESP32 وافتح الـ Serial Monitor لرؤية القراءات كل ثانيتين.
