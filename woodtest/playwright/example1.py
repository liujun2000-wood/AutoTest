# -*- coding: UTF-8 -*-



# 异步打开多个浏览器
import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium,p.firefox,p.webkit]:
            browser = await browser_type.launch(headless=False)
            page = await browser.new_page()
            await page.goto('https://test.mg.kmelearning.com/shyz/shyz/login')
            # page.locator('//*[@id="account"]').fill('qatest1')
            page.fill('//*[@id="account"]', 'qatest1')
            page.fill('//*[@id="password"]', '11111')
            # 进入框架,单击按钮,上传图片
            page.frame_locator('//*[@id="**"]').locator('').\
                set_input_files(r'....')
            page.wait_for_timeout(3000)

            # 下拉框的处理
            page.select_option('//*[@id="**"]','2')
            page.click('//span[text()="12321"]/../../../..//a[text()="删除"'])

            # 获取多个元素
            ses = page.query_selector_all('//*[@id="**"]')
            for se in ses:
                print(se.text_content())
            # 鼠标悬停







           await browser.close()

asyncio.get_event_loop().run_until_complete(main())




