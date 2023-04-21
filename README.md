# AutoColdEmails
Generate cold emails automatically using AI

This code generates a cold email automatically using AI, given two webpages. One webspage should be the client's, particularly the webpage that best describes what the client's business does. Usually their homepage, though not always.

The other webpage should be that of your product - what you're trying to sell. Again, usually the homepage, though not always.

Change the code to put these in lines 6 and 7.

You'll also need to set the OPENAI_API_KEY environment variable with your API key from OpenAI for this to work.

Finally, note that the code references GPT 3.5 but works better if you put in gpt-4 instead on line 24. Of course, this will cost more since it's a more expensive model. But it's probably worth it for crafting a great sales email. I've noticed a substantial difference in email quality and much improved ability to do what the prompt requests with GPT 4.

You also get a longer context length with GPT 4 - 8k vs 4k tokens. If you use GPT 4, you can approximately double the numbers in lines 18 and 19. See the comments in the code to understand what those numbers are.

Finally you can choose between human-friendly output or JSON by commenting out the appropriate lines at the end of the code.
