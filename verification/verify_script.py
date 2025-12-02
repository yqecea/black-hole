from playwright.sync_api import sync_playwright
import os

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the file directly since it's a static HTML file
        cwd = os.getcwd()
        filepath = f"file://{cwd}/index.html"
        print(f"Loading {filepath}")

        try:
            page.goto(filepath)

            # Wait for content to load
            page.wait_for_selector('h1')

            # 1. Verify Scrolling
            # Remove Lenis check: we just check if we can scroll natively.
            # We can check body overflow style.
            body = page.locator('body')
            # Check computed style for overflow-y. It should be auto or visible, definitely not hidden unless set by us (we removed Lenis).
            overflow_y = body.evaluate("element => getComputedStyle(element).overflowY")
            print(f"Body overflow-y: {overflow_y}")

            # Take a screenshot of the top
            page.screenshot(path="verification/top.png")

            # Scroll down
            page.mouse.wheel(0, 500)
            page.wait_for_timeout(500)
            page.screenshot(path="verification/scrolled.png")
            print("Scrolled screenshot saved.")

            # 2. Verify Spotlight Effect
            # Find a glass card
            card = page.locator('.glass-card').first
            if card.count() > 0:
                print("Testing spotlight on first glass card...")
                # Get initial style
                initial_style = card.get_attribute('style') or ""

                # Hover
                box = card.bounding_box()
                if box:
                    # Move mouse to center of card
                    page.mouse.move(box['x'] + box['width']/2, box['y'] + box['height']/2)
                    page.wait_for_timeout(200) # Wait for potential raf update

                    # Get new style
                    new_style = card.get_attribute('style')
                    print(f"Card style after hover: {new_style}")

                    if "--mouse-x" in new_style and "--mouse-y" in new_style:
                        print("Spotlight variables updated successfully.")
                    else:
                        print("Spotlight variables NOT updated.")

                    # Take screenshot of hover state
                    card.screenshot(path="verification/spotlight_hover.png")
            else:
                print("No glass card found.")

        except Exception as e:
            print(f"Error during verification: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify()
