import wikipedia

def main():
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
