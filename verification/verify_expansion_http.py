
from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local index.html file via HTTP server
        try:
            page.goto("http://localhost:8000/index.html", timeout=60000)
        except Exception as e:
            print(f"Failed to load page: {e}")
            browser.close()
            return

        # 1. Take a screenshot of the Hero Section
        page.screenshot(path="verification/hero.png")
        print("Hero screenshot taken.")

        # 2. Navigate to History (Scroll down)
        try:
            # wait for history section to be attached
            page.wait_for_selector("#history", state="attached")
            page.locator("#history").scroll_into_view_if_needed()
            page.wait_for_timeout(2000) # Wait for animations
            page.screenshot(path="verification/history.png")
            print("History screenshot taken.")
        except Exception as e:
            print(f"History section error: {e}")

        # 3. Navigate to Anatomy (Dashboard)
        try:
            page.wait_for_selector("#anatomy", state="attached")
            page.locator("#anatomy").scroll_into_view_if_needed()
            page.wait_for_timeout(2000)
            page.screenshot(path="verification/anatomy.png")
            print("Anatomy screenshot taken.")
        except Exception as e:
            print(f"Anatomy section error: {e}")

        browser.close()

if __name__ == "__main__":
    run()
