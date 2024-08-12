# Instructions :
# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# The Pagination class will accept 2 parameters:

# items (default: None): It will contain a list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.
# So for example we could initialize our pagination like this:

# alphabetList = list("abcdefghijklmnopqrstuvwxyz")

# p = Pagination(alphabetList, 4)


# The Pagination class will have a few methods:

# getVisibleItems() : returns a list of items visible depending on the pageSize
# So for example we could use this method like this:

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]
# You will have to implement various methods to go through the pages such as:
# prevPage()
# nextPage()
# firstPage()
# lastPage()
# goToPage(pageNum)

# Here’s a continuation of the example above using nextPage and lastPage:

# alphabetList = list("abcdefghijklmnopqrstuvwxyz")

# p = Pagination(alphabetList, 4)

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]

# p.nextPage()

# p.getVisibleItems()
# # ["e", "f", "g", "h"]

# p.lastPage()

# p.getVisibleItems()
# # ["y", "z"]


# Notes

# The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
# The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
# If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).\


class Pagination:
    def __init__(self, items=None, pageSize=10):
        # Initialize the Pagination class with a list of items and page size
        self.items = items if items is not None else []  # Handle default items as an empty list
        self.pageSize = int(pageSize)  # Ensure pageSize is an integer
        self.currentPage = 1  # Start at the first page
        # Calculate total pages based on the number of items and page size
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)

    def getVisibleItems(self):
        """
        Get the list of items visible on the current page.
        :return: A list of items for the current page.
        """
        # Calculate start and end indices for slicing the items list
        start_index = (self.currentPage - 1) * self.pageSize
        end_index = start_index + self.pageSize
        # Return the sliced list representing the current page's items
        return self.items[start_index:end_index]

    def nextPage(self):
        """
        Move to the next page if possible.
        :return: self (to allow method chaining)
        """
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self  # Return self to allow chaining

    def prevPage(self):
        """
        Move to the previous page if possible.
        :return: self (to allow method chaining)
        """
        if self.currentPage > 1:
            self.currentPage -= 1
        return self  # Return self to allow chaining

    def firstPage(self):
        """
        Move to the first page.
        :return: self (to allow method chaining)
        """
        self.currentPage = 1
        return self  # Return self to allow chaining

    def lastPage(self):
        """
        Move to the last page.
        :return: self (to allow method chaining)
        """
        self.currentPage = self.totalPages
        return self  # Return self to allow chaining

    def goToPage(self, pageNum):
        """
        Go to a specific page number.
        :param pageNum: The page number to go to.
        :return: self (to allow method chaining)
        """
        # Ensure pageNum is an integer and within valid bounds
        pageNum = max(1, min(self.totalPages, int(pageNum)))
        self.currentPage = pageNum
        return self  # Return self to allow chaining



# Example usage of the Pagination class

# Create a list of alphabet letters
alphabetList = list("abcdefghijklmnopqrstuvwxyz")

# Initialize the Pagination with a page size of 4
p = Pagination(alphabetList, 4)

# Print the visible items on the first page
print(p.getVisibleItems())  # Outputs: ["a", "b", "c", "d"]

# Move to the next page and print visible items
p.nextPage()
print(p.getVisibleItems())  # Outputs: ["e", "f", "g", "h"]

# Move to the last page and print visible items
p.lastPage()
print(p.getVisibleItems())  # Outputs: ["y", "z"]

# Move to a specific page and print visible items
p.goToPage(2)
print(p.getVisibleItems())  # Outputs: ["e", "f", "g", "h"]

# Move to the previous page and print visible items
p.prevPage()
print(p.getVisibleItems())  # Outputs: ["a", "b", "c", "d"]

# Move to the first page and print visible items
p.firstPage()
print(p.getVisibleItems())  # Outputs: ["a", "b", "c", "d"]

# Test edge case: go to a page out of range
p.goToPage(10)
print(p.getVisibleItems())  # Outputs: ["y", "z"] (because there are only 7 pages)

p.goToPage(-5)
print(p.getVisibleItems())  # Outputs: ["a", "b", "c", "d"] (because the minimum page is 1)
