# Testing User Stories

#### As a Customer:

  - Website experience:
    1. I want to see what products are being sold on the website.

    - The navbar offers 2 way to access the product product catalogue: 
        - By selecting the category.
        - By selecting the brand.

        <IMAGE>

    - The homepage is feature with 3 links to access the product catalogue filtering by category.

        <IMAGE>

    - In the footer's 'Shop' section the user can access the product catalogue by clicking on the desired product category link.

        <IMAGE>

    2. I want to be able to navigate the website intuitively.

    - The navbar and footer provide the user with all the links necessary to access the main sections of the webiste:
        - Home page
        - Products catalogue 
        - Blog
        - Contact page
        - Account features
        - Shopping cart

        <IMAGE>
    
    - Throughout the website, pages like Product details, Shopping cart, Checkout offer the user the option to be redirected to the previous page. 

        <IMAGE>

    3. I want to be able to contact the seller.

    - The navbar provides a link to the 'Contacts' page where the user can contact the store administration via message. 

        <IMAGE>

    - The footer provides the user with a phone number and email details to contact the store administration, in addition to a link to the 'Contacts' page.

        <IMAGE>

    4. I want to stay up to date with the latest developments in the sector.

    - Though the navbar or the dedicated section in the home page, the user can access the store blog and read the latest blog posts added by the store admin. 

        <IMAGE>

    5. I want to be able to read and add comments on blog posts.

    - The 'Post blog' page offers the user the possibility to add and delete their own comments to the blog post (feature available only for signed in users).

        <IMAGE>
  
  - Searching for products:
    6. I want to see all the products the website offers.

    - Through the navbar, by clicking the the 'Categories' link, the user can access the complete products catalogue by clicking on 'All products'.

        <IMAGE>

    7. I want to be able to search by category.

    - Through the respective links on the navbar, footer and the home page, the user can select the specific category of products to view.

        <IMAGE>

    8. I want to be able to seatch by brand.

    - Though the respective links on the navbar the user can select the products to view of a specific by brand.

        <IMAGE>

    9. I want to be able to search with a search bar.

    - Via the search bar in the navbar the use can type a query and see what products match based on product name, category, brand or description.

        <IMAGE>

    10. I want to be able to sort products by price, name, brand and category.

    - The 'Products' page offers the option to sort products in alphabetical order, price, category and brand (in ascending or descending order)

        <IMAGE>

  - Shopping experience:
    11. I want to see the products' price and description.

    - The user can each sigle product's price in both the 'Products' and 'Products details', while the description can be seen the 'Products details' page.

    12. I want to see other users' reviews and ratings on the products.

    - The 'Products details' page offers the user the option to see other users's ratings and reviews for the product, in addition to the average rating. 

    13. I want to be able to add my review on products.

    - In the'Products details' page, the user can add their own review on the product by clicking on the 'Add review' button and filling the form in the review modal.
    - The user can also delete their own comments by clicking on the 'Delete' button. 

    14. I want to be able to add products to the shopping cart.

    - In the 'Products details' page, the user can chose the desired quantity of the specific product they want to purchase and add it to the cart bt clicking on the 'Add to cart' button. 

    15. I want to be notified when I complete an operation.

    - A message pop-up would appear on the screen every time a user complete an operation such as adding products to the cart, completing a checkout. 
    - Pop-up messages can include: Success, info, warnings and errors messages.

    16. I want to be able to edit the content of my shopping cart.

    - In the 'Cart' page the user can change the quantity or a particular product or remove it completely from the cart.

    17. I want to be able to checkout easily.

    - If there is at least one product in the cart, the user can click on the 'Secure checkout' button to be directed to the 'Checkout' page.
    - In the 'Checkout page' the user can fill the form their shipping and card details (with the option for signed in users to save their shipping details in their profile).
    - If form is valid the checkout process will then be complete.

    18. I want to receive confirmation of my order.

    - If the user completes an order successfully they will be directed to the 'Order confirmation' page where they can review the order details.
    - In addition, a confirmation email containing the order details will be sent to the user.

  - Account:

    19. I want to save my details to a user profile.

    - Signed in users, can access their profile by navigating to 'My Account' > 'My Profile' from the navbar and fill in the profile form with their shipping details.
    - Alternatively the user can save their information from the 'Checkout' page as illustrated on the user story (17) above.

    20. I want to be able to see my previous order details.

    - Signed in users, can access past orders by accessing the ' My Profile' page and clicking on the order number of the desidered order from the order history. 

#### As the owner of the Website:

  1. I want to be able to add products with ease.

  - Superusers can add products by navigating to 'My Profile' > 'Product management', where they can add a new product by filling the form with valid information.  

  2. I want to be able to edit and delete products.

  - Superusers can edit or delete products via the links prodivded in the 'Products' and 'Product details' page. By clicking the 'Edit' button the superuser is directed to the 'Edit product' page.

  3. I want to have access to an admin page. 

  - Superusers can access the admin section by adding '/admin' to the root URL, from the admin interface the superuser can add, edit and delete records from the database.

  4. I want to be able to add, edit and delete posts on the website blog.

  - Superusers can add a blog post by clicking on the '+' icon from the 'Blog' page, which will redirect them to the 'Add blog post' page.
  - Posts can be edited by clicking on the 'Edit' button in the 'Blog post' page, which will redirect the superuser to the 'Edit blog' page. 
  - Posts can be delete by by clicking on the 'Delete' button in the 'Blog post' page

  5. I want to be able to delete inappropriate product reviews and blog comments.

  - Superusers can delete product reviews and blog posts comments by clicking on the 'Delete' button from the respetive review/comment. 

  6. I want to be able to check contact messages that have been sent from site users and mark them as read once they have been taken care of. 

  - From the admin interface, the superuser can check all the message received by navigating to the messages folder and mark read messages by clicking on the 'Read' checkbox. 


# Manual Testing


## Navigation

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| Navbar ||  ||
| 01 | Store Logo/Home link | Directs the user to the home page | ✓ |
| 02 | Categories link | Opens the categories dropdown menu. All categories links work | ✓ |
| 03 | Brands link | Opens the brands dropdown menu. All brands links work | ✓ |
| 04 | Blog Link | Directs the user to the 'Blog' page | ✓ |
| 05 | Contacts Link | Directs the user to the 'Contact us' page | ✓ |
| 06 | Search bar | Directs the user to the 'Products' page showing products that match the query | ✓ |
| 07 | My Account Icon | Opens the account links dropdown menu | ✓ |
| 08 | Sign in link (unsigned users)| Directs the 'Sign in' page | ✓ |
| 09 | Sign up link (unsigned users)| Directs the 'Sign up' page | ✓ |
| 10 | Sign out link (signed in users)| Directs the 'Sign out' page | ✓ |
| 11 | My Profile (signed in users) | Directs the user to the profile page | ✓ |
| 12 | Product management (superuser) | Directs the user to the 'Product management' page | ✓ |
| 13 | Cart Icon | Directs the user to their shopping cart page | ✓ |
| 14 | Burger menu | Burger menu opens the side navbar with the appropriate links work based on what type of user is signed in | ✓ |
| Footer ||  ||
| 15 | Contact us link | Directs the user to the 'Contact us' page | ✓ |
| 16 | Shop Links | Direct the user to the 'Products' page with the correct category filters in place | ✓ |
| 17 | Account Links (unsigned users) | Direct the users to the appropriate pages | ✓ |
| 18 | Account Links (signed in users) | Direct the users to the appropriate pages | ✓ |
| 19 | Social media links | Open the respective social network page in a new tab | ✓ |


## Home Page
|  Reference  |  Test Object  |  Expected Result  |  Pass  
|:---:|------| ---------------- |:---:|
| 01 | Products by category links | Direct the user to the 'Products' page with the correct category filters in place | ✓ |
| 02 | Blog link | Directs the user to the 'Blog' page | ✓ |
| 03 | Blog posts links | Direct the user to the selected blog post's page | ✓ |
| 04 | Blog posts slideshow | By clicking the right and left chevron icons or sliding sideways with the trackpad, the user browse though the blog posts | ✓ |

## Products Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Product Count | Product Count updates in accordance with the number of products displayed and search term displays if a user has entered a search query  | ✓ |
| 02 | View all products link | Redirects to the 'Products' page showing the entire catalogue of products (visible only when products catalogues is filtered) | ✓ |
| 03 | Sort By Dropdown | Sort by dropdown displays all the options available and sorts the products in accordance with the selection | ✓ |
| 04 | Product Cards | Clicking on a product card directs the user to the correct 'Product details' page | ✓ |
| 05 | Edit Product link (superuser) | Directs the superuser to the edit product form | ✓ |
| 06 | Delete Product link (superuser) | Triggers the confirmation modal | ✓ |
| 07 | Delete Product Modal | Clicking the 'Cancel' button closes the modal and clicking the 'Ok' button deletes the product successfully | ✓ |

## Product Detail Page 

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Product Details link | Closes the reviews tab and displays the product details section | ✓ |
| 02 | Product Reviews link | Closes the details tab and displays the reviews section | ✓ |
| Product Details tab ||  ||
| 03 | Technical Details link | Directs the user to the product's manifacturer page on a new tab | ✓ |
| 04 | Quantity Selectors | Allows the user to adjust the quantity by clicking the plus and minus icons. Limits the quantity to min: 1 and max: 9 | ✓ |
| 05 | Keep Shopping link | Redirects the user back to the 'Products' page | | ✓ |
| 06 | Add to Cart link | When at least a product is added to the cart, a toast to confirm the action is displayed, and the amount below the cart icon in the navbar is updated to reflect the price of the items in the cart | ✓ |
| Product Details tab ||  ||
| 07 | Log In and Sign Up Links (usigned users) | The sign in and sign up links are displayed and redirect the user to the relevant page | ✓ |
| 08 | No Reviews message | Displays when no reviews are present | ✓ |
| 09 | Add review button | Open the product review modal | ✓ |
| 10 | Product review modal | Allows user to post a review, given that all the required fields on the form are filed, by clicking on the 'Submit' button. Adjusts the average rating accordingly | ✓ |
| 11 | Delete Comment link (superuser and reviewer) | Triggers the confirmation modal | ✓ |
| 12 | Delete Comment Modal | Clicking the 'Cancel' button closes the modal and clicking the 'Ok' button deletes the comment successfully. Adjusts the average rating accordingly | ✓ |

## Shopping Cart Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Quantity Selectors | Allows the user to adjust the quantity by clicking the plus and minus icons. Limits the quantity to min: 1 and max: 9 | ✓ |
| 02 | Update Link | Updates the quantity for the selected product | ✓ |
| 03 | Remove Link | Removes the selected product from the cart | ✓ |
| 04 | Price totals | The subtotal of each product, cart total and grand total are updated whenever the cart's content is changed | ✓ |
| 05 | Delivery Cost | Delivery costs adjusts based on product price with minimum of 35€ and max of 75€ | ✓ |
| 06 | Keep Shopping Button | Redirects the user to the Products page | ✓ |
| 07 | Secure Checkout Button | Directs the user to the checkout page | ✓ |
| 08 | Cart is empty message | Displays when there are no products in the cart. Below 'Keep shopping' button is displayed and redirects the user to the Products page | ✓ |

## Checkout Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Order Summary | Order summary information renders correctly. Price totals match the contents of the bag | ✓ |
| 02 | Checkout Form | Form only submits when all the required fields are filled | ✓ |
| 03 | Pre-populated fields | When a user is signed in and their shipping details have been saved on their profile, the corresponding fields are pre-populated | ✓ |
| 04 | Save details checkbox | When the delivery information checkbox is checked the user's profile is updated with the correct information after the form submmission | ✓ |
| 05 | Log In and Sign Up Links (unsigned users) | The sign in and sign up links are displayed and redirected the user to the relevant page | ✓ |
| 06 | Card errors | Card errors message displays in case of: invalid card number, insufficient funds, etc. | ✓ |
| 07 | Card Charge notification | Is displayed to let the user know how much their card will be charged to verify that the figure matches the total in the order summary section | ✓ |
| 08 | Adjust Cart button | Redirects the user to the shopping cart | ✓ |
| 09 | Complete Order button | Triggers the loading overlay before redirecting the user to the Checkout Success page | ✓ |

## Checkout Success Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Toast success message | When the user is redirected to the Checkout Success page a confirmation toast with the order number and a message to let the user know a confirmation email has been sent to their email is displayed | ✓ |
| 02 | Confirmation Email | The user receives a confirmation email to the address entered on the checkout page | ✓ |
| 03 | Order Summary | Renders correctly with a list of the purchased product | ✓ |
| 04 | Order and Billing Info | Match the information entered on the checkout form and displays correct totals | ✓ |
| 05 | Continue Shopping link | Redirects the user to the Products page | ✓ |
| 06 | Back to profile link (if user accessed page from Profile) | Displays when users are looking at past orders from their profile, and when clicked it redirect the user back to the Profile page | ✓ |

## Contacts Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Form Validation | The form cannot be submitted without all the required fields being filled | ✓ |
| 02 | Cancel Button | Redirects the user back to the home page | ✓ |
| 03 | Submit Button | Once clicked the form is cleared and a success message displays to inform the user that their message has been sent | ✓ |

## Blog Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Add post icon (superuser) | Directs the user to the 'Add Blog Post' page | ✓ |
| 02 | Blog Post links | Direct the user to the correct 'Blog Post' page | ✓ |

## Blog Post Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Back to Blog Link | Redirects the user back to the main 'Blog' page | ✓ |
| 02 | Edit Post Link (superuser) | Directs the superuser to the 'Edit blog' page | ✓ |
| 03 | Delete Post Link | Triggers the delete blog modal | ✓ |
| 04 | Delete Post Modal | Clicking the 'Cancel' button closes the modal and clicking the 'Ok' button deletes the post successfully | ✓ |
| 05 | Log In and Sign Up Links (usigned users) | The sign in and sign up links are displayed and redirect the user to the relevant page | ✓ |
| 06 | No Comments message | Displays when no comments are present | ✓ |
| 07 | Add comment button | Open the post comment modal | ✓ |
| 08 | Post Comment modal | Allows user to post a comment, given that all the required field on the form are filed, by clicking on the 'Submit' button | ✓ |
| 09 | Delete Comment link (superuser and commenter) | Triggers the confirmation modal | ✓ |
| 10 | Delete Comment Modal | Clicking the 'Cancel' button closes the modal and clicking the 'Ok' button deletes the comment successfully | ✓ |

## Profile Page 

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Delivery Information Form | User's shipping information is displaying in the relevant fields if they have previously made an order and clicked the save to profile checkbox | ✓ |
| 02 | Update Information button | Saves changes to the user's profile if form is valid and a success message displays to confirm this to the user | ✓ |
| 03 | Previous orders | Displays in the order history section with the latest order at the top | ✓ |
| 04 | Previous order confirmation | Clicking the order number takes the user to the checkout success page for the selected order | ✓ |

## Add Product (Product Management) Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Required Fields | Form does not submit unless required fields are correctly filled | ✓ |
| 02 | Dropdown Fields | All the categories/brands options appear in the dropdown fields | ✓ |
| 03 | Select Image Link | Allows the user to upload an image from their device, and a message displays to the user the images' name | ✓ |
| 04 | Cancel Button | Redirects the user back to the products page | ✓ |
| 05 | Add Product Button | Redirects the user to the 'Product details' page for the new product with the correct information displayed | ✓ |

## Edit Product Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Form Fields | Form fields are pre-populated with the product information stored in the database | ✓ |
| 02 | Cancel Button | Redirects the user back to the 'Products' page | ✓ |
| 03 | Update Product Button | Updates any of the product information and redirects the user to the 'Product details' page for the edited product with the correct information displayed | ✓ |

## Add Blog Post Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 02 | Required Fields | Form does not submit unless required fields are correctly filled | ✓ |
| 03 | Select Image Link | Allows the user to upload an image from their device, and a message displays to the user the images' name | ✓ |
| 04 | Cancel Button | Redirects the user back to the 'Blog' page | ✓ |
| 05 | Add Post Button | Redirects the user to the 'Blog Post' page for the new post with the correct information displayed | ✓ |

## Edit Blog Post Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Form Fields | Form fields are pre-populated with the post information stored in the database | ✓ |
| 02 | Cancel Button | Redirects the user back to the 'Blog' page | ✓ |
| 03 | Update Post Button | Updates any of the post information and redirects the user to the 'Blog Post' page for the edited post with the correct information displayed | ✓ |

## Sign In Page 

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Sign Up Link | Directs the user to the sign up page | ✓ |
| 02 | Home Link | Directs the user to the home page | ✓ |
| 03 | Forgot Password Link | Directs the user to the Password Reset page | ✓ |
| 04 | Sign In Link | If the details are correct the user is redirected to the home page | ✓ |

## Sign Out Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Sign Out button | Signs the user out of their account and redirects to the home page | ✓ |

## Sign up Page

|  Reference  |  Test object  |  Expected Result  |  Pass  |
|:---:|------| ---------------- |:---:|
| 01 | Sign In Link | Directs the user to the sign in page | ✓ |
| 02 | Back to Login Link | Redirects the user to the sign in page | ✓ |
| 03 | Sign Up Link | If the form is valid directs the user to the verify email address page and a confirmation email is sent to the user | ✓ |


# Security & Defensive programming 

### Security

- Environment variables 
    - In Production, environment variables are stored on Heroku's 'config variables' section. 
    - In Development, environment variables are store in an env.py file.

- User account
    - Django all auth has been used to handle securely user's accounts their credentials.
    
### Defensive Programming.
        
- Measures have been taken and tested to ensure only authorised users can perform certain actions such as adding, deleting or editing:
    - Products, reviews, posts and comments.
- By means of:
    - @login_required decorators for views.
    - Conditional statements such as 'if request.user.is_superuser' or 'if user.is_authenticated' for views and templates.

- A confirmation modal has been set up to ensure the user does not delete products, reviews, posts and comments accidentally.


## Code Validation 

- #### CSS
    - All the website's CSS code has been passed through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and it has passesd.

- #### Javascript

     - All JavaScript has been passed through the [JSHint Validator](https://jshint.com/) and it has passesd.

     - <div float="left">
        <img src="readme-images/testing/jshint.png" alt="Image of jshint" width="500px" height="180px" />
        </div>

- #### Python

     - All Python code has been passed though the [PEP8 online check](http://pep8online.com/) with the following results:

     - <div float="left">
        <img src="readme-images/testing/pep8.png" alt="Image of pep8 results" width="500px" height="280px" />
        </div>

- #### Html

     - My Html code was passed through the [W3C Markup Validator](https://validator.w3.org/)  and it has passed.

     - <div float="left">
        <img src="readme-images/testing/html-validation.png" alt="Image of pep8 results" width="500px" height="280px" />
        </div>