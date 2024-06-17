import requests
import json

# Set up your API key and database ID
NOTION_API_KEY = 'secret_RLBkGNtQJ9ARnOXHlZmXIoIDDXPqv85aqhHnjlUbqTY'
DATABASE_ID = '1a5ea1aecc9f45519e663d93d4f581f9'

# Set up the request headers
headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"  # Check for the latest version in Notion API docs
}

# Define the base URL for the Notion API
url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

# Function to query the database
def query_database(url, headers):
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

# Write main() function which takes a date as input
def main(date: str):
    # Get the data from the database
    data = query_database(url, headers)

    if data:
        # Get the results from the data
        results = data.get('results')

        # Find new results based on the input date
        new_results = [result for result in results if result['created_time'] > date]

        # Find modified results based on the input date
        modified_results = [result for result in results if result['last_edited_time'] > date and result not in new_results]

        # For each item in the filtered data, get
        # 'url': result['url']
        # '팀명(제품/서비스명)': result['properties']['팀명(제품/서비스명)']['title'][0]['plain_text']
        # '홈페이지': result['properties']['홈페이지']
        # '제품/서비스 개요': result['properties']['제품/서비스 개요']['rich_text'][0]['plain_text']
        # '대표': result['properties']['대표']['rich_text'][0]['plain_text']
        # '대표 연락처': result['properties']['대표 연락처']['phone_number']
        new_data = [
            {
                'link': result['url'],
                'name': result['properties']['팀명(제품/서비스명)']['title'][0]['plain_text'],
                'email': result['properties']['대표 이메일']['email'],
                'ceo_phonenumber': result['properties']['대표 연락처']['phone_number'],
                'ceo_name': result['properties']['대표']['rich_text'][0]['plain_text'],
                'product_description': result['properties']['제품/서비스 개요']['rich_text'][0]['plain_text'],
                'series_funding': result['properties']['투자단계']['multi_select'][0]['name'],
                'modified_date': result['last_edited_time']
            }
            for result in new_results
        ]

        modified_data = [
            {
                'link': result['url'],
                'name': result['properties']['팀명(제품/서비스명)']['title'][0]['plain_text'],
                'email': result['properties']['대표 이메일']['email'],
                'ceo_phonenumber': result['properties']['대표 연락처']['phone_number'],
                'ceo_name': result['properties']['대표']['rich_text'][0]['plain_text'],
                'product_description': result['properties']['제품/서비스 개요']['rich_text'][0]['plain_text'],
                'series_funding': result['properties']['투자단계']['multi_select'][0]['name'],
                'modified_date': result['last_edited_time']
            }
            for result in modified_results
        ]

    # Save the new_data and modified_data to a JSON file
    with open('new_data.json', 'w') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)

    with open('modified_data.json', 'w') as f:
        json.dump(modified_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    # Allow user to input a date
    date = input("Enter a date (YYYY-MM-DD): ")
    main(date)