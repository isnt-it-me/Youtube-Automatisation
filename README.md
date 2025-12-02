# 📺 YouTube Automation Tool

A Python-based automation bot that interacts with the YouTube interface (Like, Subscribe, Shorts) using visual recognition and mouse control.

## 🚨 EMERGENCY STOP (FAILSAFE)
**READ THIS BEFORE RUNNING:**
If you need to stop the bot immediately, **quickly drag your mouse cursor to any of the four corners of the screen.**
* This triggers the built-in PyAutoGUI failsafe.
* The script will crash and stop controlling your mouse instantly.

## ⚠️ Prerequisites & Installation

### 1. Install Libraries
Open your terminal and run the following command (`opencv-python` is required for image recognition confidence):

```bash
pip install pyautogui opencv-python pillow
