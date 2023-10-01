# Web Scraping with Python

This Python script performs web scraping on a website to extract links, emails, and WhatsApp links from the specified domain (stei.itb.ac.id). It uses the `requests` library to fetch web pages and `BeautifulSoup` for parsing HTML content.

## Usage

1. Ensure you have the required libraries installed:

   ```bash
   pip install requests beautifulsoup4
   ```

2. Modify the script to specify the target domain (`DOMAIN`), home URL (`HOME_URL`), and other settings as needed.

3. Run the script:

   ```bash
   python script.py
   ```

4. The script will perform the following actions:

   - Visit the home URL (`HOME_URL`) and extract all links from the specified domain (`DOMAIN`).
   - Collect email addresses (`mailto:` links) and WhatsApp links (`api.whatsapp.com`).
   - Save the extracted data to separate log files (`scrape-links-stei.log`, `scrape-email-stei.log`, `scrape-whatsapp-stei.log`).

5. The script will recursively follow links within the specified domain to gather additional URLs.

6. The extracted links, emails, and WhatsApp links will be saved in their respective log files.

## Customization

- You can modify the `HOME_URL`, `DOMAIN`, `TIMEOUT`, or other settings in the script to target different websites or adjust the scraping behavior.

- To specify a different starting URL, change the value of `HOME_URL` in the script.

## Output

- Extracted links from the specified domain are saved in `scrape-links-stei.log`.
- Extracted email addresses are saved in `scrape-email-stei.log`.
- Extracted WhatsApp links are saved in `scrape-whatsapp-stei.log`.

## License

This script is provided under the [MIT License](LICENSE).
```

Please adapt the script and README.md to your specific use case or requirements.
