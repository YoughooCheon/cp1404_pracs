"""
function main
    print a message saying wikipedia search tool
    repeat forever
        ask the user to enter a page title
        if the title is empty
            print thank you and break the loop
        try to get the wikipedia page with the given title without auto suggestion
            print the page title, summary, and url
        if there is a disambiguation error
            tell the user to be more specific and show the options
        if there is a page error
            tell the user the page was not found
        if any other unexpected error occurs
            print the error message

if the program is run directly
    main()
"""
import wikipedia

def main():
    """
    Runs a Wikipedia search tool that fetches and displays page info based on user input.
    """
    print("Wikipedia Search Tool")
    while True:
        title = input("Enter page title: ")
        if title.strip() == "":
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(f"\n{page.title}\n{page.summary}\n{page.url}\n")

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()