import sys
import json
import time

def fetch(url, wait_time=5000):
    try:
        import undetected_chromedriver as uc
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
    except ImportError:
        print(json.dumps({"success": False, "error": "未安装 undetected_chromedriver"}))
        return

    options = uc.ChromeOptions()
    options.headless = False # MUST run headed for stealth
    options.add_argument("--disable-dev-shm-usage")
    driver = None
    try:
        driver = uc.Chrome(options=options, version_main=144)
        driver.get(url)
        time.sleep(wait_time / 1000.0)
        
        # Twitter needs to execute JS, sometimes it redirects to /login?mx=2 if it detects automation too late
        # We scroll down to force lazy load
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
        time.sleep(2)
        
        html = driver.page_source
        title = driver.title
        
        print(json.dumps({
            "success": True,
            "html": html,
            "title": title
        }))
    except Exception as e:
        print(json.dumps({"success": False, "error": str(e)}))
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    url = sys.argv[1]
    wait_time = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
    fetch(url, wait_time)
