import requests
import openai
from bs4 import BeautifulSoup

# Make a request to the webpages and grab the HTML responses
page_client = requests.get("https://clientwebsite.com/").content #website of client
page_product = requests.get("https://productwebsite.com").content #product to be sold

# Pass the HTML responses to Beautiful Soup
soup_client = BeautifulSoup(page_client, 'html.parser')
soup_product = BeautifulSoup(page_product, 'html.parser')

# Extract only the human-readable text and remove blank lines
text_client = "\n".join(line.strip() for line in soup_client.get_text().split("\n") if line.strip())
text_product = "\n".join(line.strip() for line in soup_product.get_text().split("\n") if line.strip())

#Context Length limit is 4097 tokens for gpt 3.5. Allocating 1500 to each input and leaving the rest for prompts, and output, we need to limit the string lengths to around 6k characters. 1 token is around 4 characters. The code below just chooses the first 6k characters.
text_client = text_client[:6000]
text_product = text_product[:6000]

#print(text)

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "Your job is to write a concise cold sales email (not more than 5 sentences please) selling a product to a client. The email must be tailored to what the client's business does."},
        {"role": "user", "content": "Here is some information about the product to sell: " + text_product},
        {"role": "assistant", "content": "Thanks. Please also tell me about the client's business."},
        {"role": "user", "content": "Here is some information about what the client's business does: " + text_client}
    ]
)

#print(response) #use this for api-type json output

#use the below for printing output to screen
content = response["choices"][0]["message"]["content"]
print(content)
