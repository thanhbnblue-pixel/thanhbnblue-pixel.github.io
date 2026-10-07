import asyncio
from playwright.async_api import async_playwright
import os

async def generate_portfolio_pdf():
    html_path = os.path.abspath("index.html")
    pdf_path = os.path.abspath("Portfolio_BuiNgocThanh.pdf")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        file_uri = "file:///" + html_path.replace("\\", "/")
        await page.goto(file_uri)
        await page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
        )
        await browser.close()
        print(f"Portfolio PDF generated at: {pdf_path}")

if __name__ == '__main__':
    asyncio.run(generate_portfolio_pdf())
