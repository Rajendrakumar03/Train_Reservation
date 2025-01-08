# import re

# class ArticleManager:
#     def __init__(self, article_text, options=None):
#         if options is None:
#             options = {}
        
#         self.article_text = article_text
#         self.pages = []
#         self.words = []
#         self.options = {
#             'words_per_line': options.get('words_per_line', 12),
#             'lines_per_page': options.get('lines_per_page', 20),
#             'payment_structure': options.get('payment_structure', {
#                 1: 30,
#                 2: 30,
#                 3: 60,
#                 4: 60,
#                 'default': 100,
#             })
#         }

#     def split_into_pages(self):
#         words_per_line = self.options['words_per_line']
#         lines_per_page = self.options['lines_per_page']
        
#         # Split words using regex to handle multiple spaces
#         self.words = re.split(r'\s+', self.article_text.strip())
        
#         # Calculate total pages
#         words_per_page = words_per_line * lines_per_page
#         total_pages = -(-len(self.words) // words_per_page)  # Ceiling division

#         # Split into pages
#         for i in range(total_pages):
#             start_idx = i * words_per_page
#             end_idx = (i + 1) * words_per_page
#             page_words = self.words[start_idx:end_idx]
            
#             # Split each page into lines
#             page_lines = [
#                 ' '.join(page_words[j:j + words_per_line])
#                 for j in range(0, len(page_words), words_per_line)
#             ]
#             self.pages.append('\n'.join(page_lines))

#     def calculate_payment(self):
#         payment_structure = self.options['payment_structure']
#         total_pages = len(self.pages)

#         # Determine payment based on the payment structure
#         return payment_structure.get(total_pages, payment_structure['default'])

#     def display_pages(self):
#         payment = self.calculate_payment()

#         # Display summary
#         print(f"Total Pages: {len(self.pages)}")
#         print(f"Payment Due: ${payment}")

#         # Display each page
#         for index, page in enumerate(self.pages):
#             print(f"\nPage {index + 1}:\n{'-' * 20}\n{page}\n{'-' * 20}")

#     def process_article(self):
#         self.split_into_pages()
#         self.display_pages()

# # Example usage
# article_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore 
# et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
# commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
# pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
# laborum."""
# article_manager = ArticleManager(article_text)
# article_manager.process_article()
