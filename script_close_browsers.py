import sqlite3
import time
import win32gui
import win32con

def search_history_contains(keywords, profile_dir, table_name, column_names):
    with sqlite3.connect(f"{profile_dir}") as conn:
        cursor = conn.cursor()

        for keyword in keywords:
            query = f"SELECT * FROM {table_name} WHERE {' OR '.join([f'{col} LIKE ?' for col in column_names])}"
            cursor.execute(query, tuple(['%' + keyword + '%' for _ in column_names]))
            rows = cursor.fetchall()
            if len(rows) > 0:
                return True
    
    return False

def close_windows_with_keyword(windows, keywords, app_name):
    for hwnd in windows:
        title = win32gui.GetWindowText(hwnd)
        if app_name.lower() in title.lower():
            for keyword in keywords:
                if keyword.lower() in title.lower():
                    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                    print(f"Closed {app_name} window with '{keyword}' in the title.")
                    break
                else:
                    hwnd_url = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
                    while hwnd_url:
                        buf = win32gui.GetWindowText(hwnd_url)
                        if keyword.lower() in buf.lower():
                            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                            print(f"Closed {app_name} window with URL containing '{keyword}'.")
                            break
                        hwnd_url = win32gui.GetWindow(hwnd_url, win32con.GW_HWNDNEXT)

def close_firefox_and_chrome_windows(keywords):
    firefox_profile_dir = 'C:/Users/<User>/AppData/Roaming/Mozilla/Firefox/Profiles/<Firefox-current-profile>/places.sqlite'
    chrome_profile_dir = 'C:/Users/<User>/AppData/Local/Google/Chrome/User Data/Default/History'
    
    while True:
        if search_history_contains(keywords, firefox_profile_dir, "moz_places", ["url"]):
            windows = []
            win32gui.EnumWindows(lambda hwnd, window_list: window_list.append(hwnd), windows)
            close_windows_with_keyword(windows, keywords, 'firefox')

        if search_history_contains(keywords, chrome_profile_dir, "urls", ["url", "title"]):
            windows = []
            win32gui.EnumWindows(lambda hwnd, window_list: window_list.append(hwnd), windows)
            close_windows_with_keyword(windows, keywords, 'chrome')
        
        time.sleep(3)  # Check every 3 seconds (adjust as needed)

search_keywords = ["exampleWord1", "exampleWord2", "exampleWord3"]
close_firefox_and_chrome_windows(search_keywords)
