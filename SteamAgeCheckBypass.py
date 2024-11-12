import sqlite3
import os
import sys
import tkinter as tk
from tkinter import messagebox
import psutil
import time

def get_steam_cookie_path():
    """Get the path to the Steam cookies database."""
    user_profile_path = os.path.join(os.environ.get('USERPROFILE', ''), 'AppData', 'Local', 'Steam', 'htmlcache', 'Network', 'Cookies')
    if os.path.exists(user_profile_path):
        return user_profile_path
    else:
        show_message("Error", "Steam cookies file not found. Please make sure Steam is installed and you're on a Windows machine.", "error")
        sys.exit(1)

def close_steam():
    """Force close Steam if it's running."""
    for proc in psutil.process_iter(['pid', 'name']):
        if 'steam.exe' in proc.info['name'].lower():
            try:
                proc.terminate()  # Try to close the Steam process
                time.sleep(2)  # Give Steam some time to close
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue  # If there's an issue, just skip and continue
            break  # Stop once Steam is found and terminated

def insert_cookies():
    """Insert cookies into the Steam's cookies SQLite database."""
    cookies_db_path = get_steam_cookie_path()

    cookies_data = [
        (
            13370000000000000, 'store.steampowered.com', '', 'wants_mature_content', 1,
            bytes.fromhex(''),
            '/', 20000000000000000, 0, 0, 13370000000000000, 1, 1, 1, -1, 2, 443, 13370000000000000, 1, 1
        ),
        (
            13370000000000000, 'store.steampowered.com', '', 'lastagecheckage', '1-January-1995',
            bytes.fromhex(''),
            '/', 20000000000000000, 0, 0, 13370000000000000, 1, 1, 1, -1, 2, 443, 13370000000000000, 1, 1
        ),
        (
            13370000000000000, 'store.steampowered.com', '', 'birthtime', 788914801,
            bytes.fromhex(''),
            '/', 20000000000000000, 0, 0, 13370000000000000, 1, 1, 1, -1, 2, 443, 13370000000000000, 1, 1
        )
    ]

    try:
        # Connect to the SQLite database and execute the queries
        conn = sqlite3.connect(cookies_db_path)
        cursor = conn.cursor()
        for cookie in cookies_data:
            cursor.execute("""
                INSERT OR REPLACE INTO "main"."cookies" (
                    "creation_utc", "host_key", "top_frame_site_key", "name", "value", 
                    "encrypted_value", "path", "expires_utc", "is_secure", "is_httponly", 
                    "last_access_utc", "has_expires", "is_persistent", "priority", "samesite", 
                    "source_scheme", "source_port", "last_update_utc", "source_type", 
                    "has_cross_site_ancestor"
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, cookie)
        conn.commit()
        conn.close()
        show_message("Success", "Successfully added the Age Check Bypass.")
    except sqlite3.Error as e:
        show_message("Error", f"Unable to update the cookies database: {e}", "error")

def show_message(title, message, msg_type="info"):
    """Show a message box with a title, message, and type."""
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    if msg_type == "info":
        messagebox.showinfo(title, message)
    elif msg_type == "error":
        messagebox.showerror(title, message)
    root.quit()

if __name__ == "__main__":
    show_message("Notice", "The script will close Steam if it's running, and then activate the Age Check Bypass.")
    close_steam()  # Attempt to close Steam before proceeding
    insert_cookies()
