from playwright.sync_api import sync_playwright

def verify_hero_and_interactivity():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Set viewport to standard desktop size
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        # Open via local server
        page.goto("http://localhost:8000/index.html")

        # Wait for the hero reveal animation (approx 3-4 seconds based on JS timeouts)
        # We wait 4 seconds to ensure everything is settled
        page.wait_for_timeout(4000)

        # Take a screenshot of the Hero section
        page.screenshot(path="verification/hero_reveal.png")
        print("Hero screenshot taken.")

        # Test Magnetic Buttons (Hover over "INITIATE SEQUENCE")
        # Selector: #hero-buttons a
        button = page.locator("#hero-buttons a")
        button.hover()
        # Wait a moment for magnetic effect (gsap tween)
        page.wait_for_timeout(500)
        page.screenshot(path="verification/hero_hover.png")
        print("Hero hover screenshot taken.")

        # Scroll to Dashboard (Anatomy) section to check Data Scrambling
        # Anatomy is #anatomy
        page.locator("#anatomy").scroll_into_view_if_needed()
        # Wait for ScrollTrigger to fire and scramble animation to finish (2000ms)
        page.wait_for_timeout(2500)
        page.screenshot(path="verification/dashboard_scramble.png")
        print("Dashboard screenshot taken.")

        browser.close()

if __name__ == "__main__":
    verify_hero_and_interactivity()
