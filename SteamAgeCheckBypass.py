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

def insert_cookie():
    """Insert the 'wants_mature_content' cookie into Steam's cookies SQLite database."""
    cookies_db_path = get_steam_cookie_path()
    
    query = """
    INSERT OR REPLACE INTO "main"."cookies" (
        "creation_utc", "host_key", "top_frame_site_key", "name", "value", 
        "encrypted_value", "path", "expires_utc", "is_secure", "is_httponly", 
        "last_access_utc", "has_expires", "is_persistent", "priority", "samesite", 
        "source_scheme", "source_port", "last_update_utc", "source_type", 
        "has_cross_site_ancestor"
    ) VALUES (
        13369518193533818, 'store.steampowered.com', '', 'wants_mature_content', '', 
        X'763130e83b5a9b1fad604ba8910b17fe98952393ed7a70c240fd544159fd96a2', '/app/379430', 
        13401054193000000, 0, 0, 13369518193533818, 1, 1, 1, -1, 2, 443, 
        13369518193533818, 0, 1
    );
    """
    
    try:
        # Connect to the SQLite database and execute the query
        conn = sqlite3.connect(cookies_db_path)
        conn.execute(query)
        conn.commit()
        conn.close()
        show_message("Success", "Successfully added the 'wants_mature_content' cookie.")
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
    show_message("Notice", "The script will close Steam if it's running, and then add the 'wants_mature_content' cookie.")
    close_steam()  # Attempt to close Steam before proceeding
    insert_cookie()
