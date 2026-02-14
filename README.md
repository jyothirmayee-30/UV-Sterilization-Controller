# 🧼 UV Sterilization Box Controller

A safety-first IoT controller for UVC sterilization chambers. It manages germicidal lamp exposure times while ensuring user safety through hardware interlocks.

## 🚀 Features
- **Precision Exposure Timer:** Ensures 99.9% pathogen elimination through calibrated UVC cycles.
- **Safety Interlock System:** Automatically cuts power to UVC lamps if the chamber door is opened.
- **Lamp Life Analytics:** Tracks total "Burn Hours" to notify users when UVC bulbs need replacement.
- **Sterilization Logging:** Sends completion reports to a Python dashboard for audit trails.

## ⚙️ Engineering Logic
- **Hardware:** Arduino Micro manages a 5V relay for the high-voltage UVC lamps and monitors a magnetic reed switch for door safety.
- **Software:** Python logs each successful cycle and calculates lamp degradation based on cumulative runtime.
