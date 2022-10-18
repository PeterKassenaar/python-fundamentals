# Belongs to workshop-14. This file demonstrates that we 
# can import the workshop and run it from this file, 
# instead of (just) from the command line

# 1. Import the module
countries = __import__('workshop-14')

# 2. Call the main function with an arbitrary string
countries.main('united')