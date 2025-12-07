
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local index.html file
        # Since I'm in the sandbox, I can use the absolute path
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # 1. Take a screenshot of the Hero Section
        page.screenshot(path="verification/hero.png")
        print("Hero screenshot taken.")

        # 2. Navigate to History (Scroll down)
        # Wait for the timeline to be visible
        page.locator("#history").scroll_into_view_if_needed()
        page.wait_for_timeout(1000) # Wait for animations
        page.screenshot(path="verification/history.png")
        print("History screenshot taken.")

        # 3. Navigate to Anatomy (Dashboard)
        page.locator("#anatomy").scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path="verification/anatomy.png")
        print("Anatomy screenshot taken.")

        # 4. Navigate to Deep Dive (Glossary)
        page.locator("#deep-dive").scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path="verification/deep_dive.png")
        print("Deep Dive screenshot taken.")

        # 5. Navigate to Evidence (Parallax)
        page.locator("#evidence").scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path="verification/evidence.png")
        print("Evidence screenshot taken.")

        browser.close()

if __name__ == "__main__":
    run()
