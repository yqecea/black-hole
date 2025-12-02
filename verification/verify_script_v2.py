from playwright.sync_api import sync_playwright
import os

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        cwd = os.getcwd()
        filepath = f"file://{cwd}/index.html"
        print(f"Loading {filepath}")

        try:
            page.goto(filepath)
            page.wait_for_selector('h1')

            # 1. Verify Scrolling
            body = page.locator('body')
            overflow_y = body.evaluate("element => getComputedStyle(element).overflowY")
            print(f"Body overflow-y: {overflow_y}")

            # 2. Verify Spotlight Effect
            # Scroll to the first glass card
            card = page.locator('.glass-card').first
            if card.count() > 0:
                print("Scrolling to first glass card...")
                card.scroll_into_view_if_needed()

                # Wait for GSAP animation to likely finish or at least start
                # GSAP duration is 1.0s
                print("Waiting for animations...")
                page.wait_for_timeout(2000)

                # Check opacity to ensure it's visible
                opacity = card.evaluate("element => getComputedStyle(element).opacity")
                print(f"Card opacity: {opacity}")

                # Hover
                box = card.bounding_box()
                if box:
                    print(f"Card box: {box}")
                    # Move mouse to center of card
                    page.mouse.move(box['x'] + box['width']/2, box['y'] + box['height']/2)

                    # Trigger a few moves to simulate movement and trigger raf
                    page.mouse.move(box['x'] + box['width']/2 + 10, box['y'] + box['height']/2 + 10)
                    page.wait_for_timeout(100)

                    # Get style attribute
                    style_attr = card.get_attribute('style')
                    print(f"Card style attribute: {style_attr}")

                    # Check computed style for CSS variables might be harder directly,
                    # but we can check if the style attribute contains them.
                    if "--mouse-x" in style_attr and "--mouse-y" in style_attr:
                        print("SUCCESS: Spotlight variables updated.")
                    else:
                        print("FAILURE: Spotlight variables NOT updated.")

                    # Take screenshot
                    page.screenshot(path="verification/spotlight_verified.png")
            else:
                print("No glass card found.")

        except Exception as e:
            print(f"Error during verification: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify()
