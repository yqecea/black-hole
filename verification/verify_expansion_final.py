
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Launch browser without font pixel check to avoid timeout waiting for external fonts
        browser = p.chromium.launch(headless=True, args=['--disable-font-subpixel-positioning'])
        page = browser.new_page()

        # Load via HTTP server but don't wait for 'load', just 'domcontentloaded'
        try:
            page.goto("http://localhost:8000/index.html", timeout=30000, wait_until="domcontentloaded")
            print("Page DOM loaded.")
        except Exception as e:
            print(f"Failed to load page: {e}")
            browser.close()
            return

        # Force a short wait for initial render
        page.wait_for_timeout(1000)

        # 1. Hero
        try:
            page.screenshot(path="verification/hero.png", animations="disabled", caret="hide")
            print("Hero screenshot taken.")
        except Exception as e:
            print(f"Hero screenshot failed: {e}")

        # 2. History
        try:
            # Scroll slightly to trigger scroll-linked animations if any
            page.evaluate("window.scrollBy(0, 1000)")
            page.wait_for_timeout(500)
            page.locator("#history").scroll_into_view_if_needed()
            page.wait_for_timeout(500)
            page.screenshot(path="verification/history.png", animations="disabled", caret="hide")
            print("History screenshot taken.")
        except Exception as e:
            print(f"History screenshot failed: {e}")

        # 3. Anatomy
        try:
            page.locator("#anatomy").scroll_into_view_if_needed()
            page.wait_for_timeout(500)
            page.screenshot(path="verification/anatomy.png", animations="disabled", caret="hide")
            print("Anatomy screenshot taken.")
        except Exception as e:
            print(f"Anatomy screenshot failed: {e}")

        browser.close()

if __name__ == "__main__":
    run()
