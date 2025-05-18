# Appium Configuration
APPIUM_SERVER = 'http://localhost:4723/wd/hub'

# Android Configuration
ANDROID_CAPABILITIES = {
    'platformName': 'Android',
    'platformVersion': '11.0',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.example.bugslayer',
    'appActivity': 'com.example.bugslayer.MainActivity',
    'automationName': 'UiAutomator2',
    'noReset': True
}

# iOS Configuration
IOS_CAPABILITIES = {
    'platformName': 'iOS',
    'platformVersion': '14.0',
    'deviceName': 'iPhone Simulator',
    'bundleId': 'com.example.bugslayer',
    'automationName': 'XCUITest',
    'noReset': True
}

# Test Configuration
WAIT_TIMEOUT = 10
RETRY_COUNT = 3
SCREENSHOT_DIR = 'test_screenshots' 