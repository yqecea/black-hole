
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Disable font loading waiting to speed up screenshot
        browser = p.chromium.launch(headless=True, args=['--disable-font-subpixel-positioning'])
        page = browser.new_page()

        # Load the local index.html file via HTTP server
        try:
            page.goto("http://localhost:8000/index.html", timeout=60000, wait_until="domcontentloaded")
            print("Page loaded (domcontentloaded).")
        except Exception as e:
            print(f"Failed to load page: {e}")
            browser.close()
            return

        # 1. Take a screenshot of the Hero Section - Disable animations/fonts wait
        try:
            page.screenshot(path="verification/hero.png", animations="disabled", timeout=10000)
            print("Hero screenshot taken.")
        except Exception as e:
            print(f"Hero screenshot failed: {e}")

        # 2. Navigate to History (Scroll down)
        try:
            page.wait_for_selector("#history", state="attached")
            page.locator("#history").scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            page.screenshot(path="verification/history.png", animations="disabled", timeout=10000)
            print("History screenshot taken.")
        except Exception as e:
            print(f"History section error: {e}")

        # 3. Navigate to Anatomy (Dashboard)
        try:
            page.wait_for_selector("#anatomy", state="attached")
            page.locator("#anatomy").scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            page.screenshot(path="verification/anatomy.png", animations="disabled", timeout=10000)
            print("Anatomy screenshot taken.")
        except Exception as e:
            print(f"Anatomy section error: {e}")

        browser.close()

if __name__ == "__main__":
    run()
