# Steam Age Check Bypass
![GitHub Release](https://img.shields.io/github/v/release/Will6855/Steam-Age-Check-Bypass)
![Github Releases](https://img.shields.io/github/downloads/Will6855/Steam-Age-Check-Bypass/latest/total.svg)

A Python script to bypass the Steam age check.

## About

This script is designed to bypass the Steam age check, allowing users to access content that would otherwise be restricted due to their age. Please note that using this script may be against Steam's terms of service.

## Installation

To install the script, you will need to have Python 3.9 or later installed on your system. You can download the latest version of Python from the official Python website.

Once you have Python installed, you can install the required dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```	

If you do not want to use the script and prefer a simpler method, you can skip the installation steps below and use the browser method.

## Usage
### Method 1: Using the Script/Executable (For Steam Desktop Client)

If you are using the Steam desktop client and need to bypass the age check, you will need to use the Python script or the pre-compiled executable. This method will bypass the check within the Steam client.

1. Using the Python Script: Run the following command in your terminal:
    ```python
    python SteamAgeCheckBypass.py
    ```

1. Using the Pre-compiled Executable: Alternatively, you can download the pre-compiled executable for Windows from the Releases section and run the .exe file. This will allow you to bypass the age check without needing Python or any dependencies installed.

### Method 2: Manual Cookie Injection (For Browser Only)

If you are only using your browser to access the Steam store and want to bypass the age check without using the script or executable, you can set specific cookies directly in the browser’s developer console. This method is ideal for bypassing the age check in the browser only.

1. Open your browser (preferably Chrome or Edge).
2. Go to the Steam store (store.steampowered.com).
3. Open the developer console by pressing F12 or Ctrl+Shift+I.
4. Switch to the Console tab.
5. Paste the following commands into the console and press Enter:

    ```javascript
    document.cookie = "wants_mature_content=1; domain=store.steampowered.com; path=/; expires=Fri, 01 Jan 9999 00:00:00 UTC; secure";
    document.cookie = "lastagecheckage=1-January-1995; domain=store.steampowered.com; path=/; expires=Fri, 01 Jan 9999 00:00:00 UTC; secure";
    document.cookie = "birthtime=788914801; domain=store.steampowered.com; path=/; expires=Fri, 01 Jan 9999 00:00:00 UTC; secure";
    ```

These cookies will simulate a valid Steam age, allowing you to bypass the age verification directly in the browser.

Note: If you are using the browser method, you can skip the Python installation and script usage altogether.

## Releases
You can find pre-compiled executables for Windows in the [Releases](https://github.com/Will6855/SteamAgeCheckBypass/releases) section. Simply download the latest .exe file and run it to use the script without needing to install Python or any dependencies.

Note: Make sure to only download executables from trusted sources, such as the official GitHub releases page.
