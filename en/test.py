import yaml
import pandas as pd

# Define the base URL of the documentation space
BASE_URL = "https://mi.docs.wso2.com/en/4.4.0"

# Load mkdocs.yml
with open('mkdocs.yml', 'r') as file:
    mkdocs_config = yaml.safe_load(file)

# Extract pages from 'nav'
def format_url(path):
    """Convert the given file path into a proper URL."""
    path = path.replace(".md", "/")  # Replace '.md' with a trailing slash
    return path

# Extract pages from 'nav'
def extract_pages(nav, parent=''):
    pages = []
    for item in nav:
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, list):
                    pages.extend(extract_pages(value, f"{key}"))
                else:
                    page_url = f"{BASE_URL}/{format_url(value)}"
                    pages.append({'Page Name': key, 'Page URL': page_url})
        else:
            page_url = f"{BASE_URL}/{format_url(item)}"
            pages.append({'Page Name': item, 'Page URL': page_url})
    return pages

pages = extract_pages(mkdocs_config.get('nav', []))
df = pd.DataFrame(pages)

# Create a new column for Google Sheets-compatible hyperlinks
df['Hyperlink'] = df.apply(lambda row: f'=HYPERLINK("{row["Page URL"]}", "{row["Page Name"]}")', axis=1)

# Save to Excel
output_file = 'documentation_pages_google_sheets.xlsx'
df[['Hyperlink']].to_excel(output_file, index=False, header=False)

print(f"Documentation pages with hyperlinks exported to {output_file}")
