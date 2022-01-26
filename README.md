# User experience

## User Stories

- As a Customer:

  - Website experience:
    - I want to see what products are being sold on the website.
    - I want to be able to navigate the website intuitively.
    - I want to be able to contact the seller.
    - I want to stay up to date with the latest developments in the sector.
    - I want to be able to read and add comments on the blog posts.
  
  - Searching for products:
    - I want to see all the products the website offers.
    - I want to be able to search by category.
    - I want to be able to seatch by brand.
    - I want to be able to search with a search bar.
    - I want to be able to sort products by price, name, brand and category.

  - Shopping experience:
    - I want to see the products' price and description.
    - I want to see other users' reviews and ratings on the products.
    - I want to be able to add my review on products.
    - I want to be able to add products to the shopping cart.
    - I want to be notified when I complete an operation.
    - I want to be able to edit the content of my shopping cart.
    - I want to be able to checkout intuitively.
    - I want to receive confirmation of my order.

  - Account:
    - I want to save my details to a user profile.
    - I want to be able to see my previous order details.

- As the owner of the Website:

  - I want to be able to add products with ease.
  - I want to be able to edit and delete products.
  - I want to have access to an admin page. 
  - I want to be able to add, edit and delete posts on the website blog.
  - I want to be able to delete inappropriate product reviews.
  - I want to be able to delete inappropriate blog comments.
  - I want to be able to check contact messages that have been sent site users and mark them as read once they have been taken care of. 


## Features

- #### All apps 

    - Interactive Navbar features:
        - The site contains the navigation section that is collapsed on smaller size screens in the form of a side navbar accessed by clicking on the hamburger icon.
        - The navbar contains:
          - Webiste logo (which directs to the homepage) on large screen sizes and a 'home' link in the side navbar in smaller screen sizes.
          - Search bar to insert queries and look for specific products
          - Links to the products page (filtering by: category and brand), blog and contact pages
          - Links for account management including: 
            - Profile and Sign out links (for signed in users) 
            - Sign in and sign up links (for unsigned users)
            - Product management, to add new products to the website (for superuser).
          - Link to the shopping cart
          - <p align="center"><img src="readme-images/features/navigation.png" alt="Image of navigation menu" height="250px" width="300px"/></p>
    
    - Footer features:
        - The footer is split into different sections:
            - Contact: provides company's phone, email contacts and a link to the contact page to message the store owner directly.
            - Shop: provides links to access product list by category.
            - Account: provides links to access blog, profile and signout links (for signed in users) or sign in and sign up links (for unsigned users).
            - Socials: provides links to social medias. 

    - Toast Messages:
        - Toast message pop-ups are used throughout the site to display feedback to the users as a result of interacting with the site. These messages have a title and a specific color attached to signify different message types:

            - Green: Success
            - Yellow: Warning
            - Blue: Info
            - Red: Errors
    
    - If the user selects to delete a product, comment or review, a modal will show to ask for confirmation to prevent accidental deletion.
        -  <p align="center"><img src="readme-images/features/item-delete.png" alt="Image of item page delete modal" height="180px" width="350px"/></p>

- #### Home App

    - Hero-image section features:
        - Upon opening the site the user is greeted with the main hero section that illustrate the purpuse of the website.
            - <p align="center"><img src="readme-images/features/hero-section.png" alt="Image of hero section" height="180px" width="320px"/></p>
        
    - Product Categories section features:
        - The product categories sections with three links to access the product page filtering products by specific category.
            - <p align="center"><img src="readme-images/features/home-categories.png" alt="Image of new items slider" height="200px" width="400px"/></p>
        
    - Blog section features:
        - Slideshow with all blog posts that users can browse through by scrolling sideways or by clicking on the right/left chevron icons.
        - The user can click on the 'Flame' logo to be led to the blog page and click on the post titles to be led to the specific blog post page.
            - <p align="center"><img src="readme-images/features/blog-landing.png" alt="Image of newsletter section" height="200px" width="450px"/></p>

- #### Products App

    - All Products page features:
        - Shows all the products available in the store 
        - The user can filter the product displayed by clicking the respective links in the navigration bar or by searching for product: name, brand, category or description though the search bar.
            - <p align="center"><img src="readme-images/features/all-items.png" alt="Image of all items view" height="220px" width="400px"/></p>
        - Select-input in the top right corner of the page that allows users to sort through products.
            - <p align="center"><img src="readme-images/features/sort-items.png" alt="Image of items selector" height="200px" width="400px"/></p>

    - Product detail page features:
        - Product image 
        - Product detail section consisting of:
          - Product description (admin will also be able to edit and delete products by clicking on the respective links)
          - Quantity selector and an add to cart button
          - Link to go back to the products page
        - Product reviews section consisting of:
          - Average rating by users 
          - Button to add a review (for signed in users) or link to sign in/ sign up for unsigned Users
          - List of reviews and ratings by users
          - Button only visible on a user's own reviews to delete them
            -  <p align="center"><img src="readme-images/features/item-page.png" alt="Image of item page" height="200px" width="350px"/></p>
        - Related products section that allows the user to browse through the related products' slideshow (in the same category of the selected product) by scrolling through or clicking on the left/right chevron arrows.
    
    - Adding products to the Cart:
        - The user has the option to add items to the cart from the products page by clicking on the respective button.
        - The user will then be shown a toast message showing that the product has been placed in the cart with a list of all items already present in the cart and a link to redirect to the cart page.
        -  <p align="center"><img src="readme-images/features/add-to-cart.png" alt="Image of add to cart message" height="280px" width="420px"/></p>

    - Restricted to superuser:
        - The 'all products' and 'product detail' page provides links to the edit page or to delete a product.
            -  <p align="center"><img src="readme-images/features/superuser-item-links.png" alt="Image of item page superuser links" height="220px" width="350px"/></p>
        
        - The review section in the 'product detail' page provides buttons to delete any review 

        - Via link in the 'my account' section on the navbar, the user has access to the product administration page to add items directly from the website.
            -  <p align="center"><img src="readme-images/features/stock-control.png" alt="Image of stock control page" height="300px" width="350px"/></p>

- #### Cart App

    - Cart Page features:
        - List of products that have been placed in their cart.
            - The user can adjust the quantity of each product, or remove it from the cart.
        - Total, delivery price, and grand total.
        - Buttons that link to checkout page (1) and back to the product page to continue shopping (2).
            -  <p align="center"><img src="readme-images/features/cart.png" alt="Image of cart page" height="220px" width="500px"/></p>

- #### Checkout app

    - Checkout page features:
        - Checkout form (with save-info option for signed in users).
        - Order summary with: 
            - Products image
            - Product name
            - Price per unit
            - Quantity
            - Subtotal
        - Buttons to complete checkout (1) and return to shopping cart (2)
            -  <p align="center"><img src="readme-images/features/checkout.png" alt="Image of checkout page" height="220px" width="500px"/></p>
    
    - Order confirmation page features:
        - Once the order has been confirmed the user is directed to the order confirmation page that will display the order details and order number.
        - An email of confirmation will be sent to the user.
            -  <p align="center"><img src="readme-images/features/order-confirmation.png" alt="Image of order confirmation" height="220px" width="500px"/></p>

- #### Profiles app
    - Profile page features:
        - Users' shipping details to pre-fill checkout forms.
        - List with past orders. 
            -  <p align="center"><img src="readme-images/features/previous-ref.png" alt="Image of previous order numbers" height="150px" width="500px"/></p>
        - When the users click on an order number from the profile page, they are directed to the order's detail page (same as the one created after a successful checkout).
            -  <p align="center"><img src="readme-images/features/previous-order.png" alt="Image of review form" height="280px" width="550px"/></p>

- #### Blog app

    - Blog page features: 
        - The main blog page shows all the blog posts created with a link to each specific blog post.
            - <p align="center"><img src="readme-images/features/all-posts.png" alt="Image of all blog posts"  height="320px" width="550px"/></p>

    - Blog post page features: 
        - Post with description and link to be redirected to the main blog page 
        - Comment section to which signed in users can add comments.
    
    - Restricted to superuser:
        - The blog page provides the user with a link (a plus icon) that redirects to the form page where the superuser can add a new post.
        - The blog post page provides buttons to edit (1) and delete (2) the post. 
            - <p align="center"><img src="readme-images/features/add-post.png" alt="Image of add post page"  height="320px" width="550px"/></p>

- #### Contact App

    - Contact page features:
        - Contact form that allows users to send a message to the store owner directly from the website (with email field pre-filled for signed in users).

- ### Allauth features
    - The sign in, sign up, sign out, password reset, email confirmation and other authentication related features, have been provided by Django allauth and edited to fit with the style and functionality of the website.


# Deployment

## Set up project locally

First, ensure the following are set up on your IDE:
- [PIP3](https://pypi.org/project/pip/) Python package installer. 
- [Python 3.6](https://www.python.org/downloads/release/python-360/) or higher.
- [Git](https://git-scm.com/) version control.

To clone the project up locally you can follow the following steps: 

1. Navigate to the repository - [Flame Repository](https://github.com/Hidnish/Milestone-Project-4-Flame)

2. Click the code dropdown button and copy the url. 

3. Open the terminal in your IDE and enter the following code: 
    - ```
        git clone https://github.com/Hidnish/Milestone-Project-4-Flame.git
        ```

4. Install the dependencies needed to run the application by typing the following command into the terminal: 
    - ```
        pip3 install -r requirements.txt
        ```

5. Create a Stripe account,if you do not have one yet, to allow online purchases in your website. 

6. Set up the environment variables: 
    - Create an env.py file (make sure to add the file to .gitignore to avoid exposure of sensitive data) by typing the following command into the terminal:
        - ```
            touch env.py
            ```
    - Inside the env.py file add the following code:
        - ```
            import os

            os.enviorn["DEVELOPMENT"] = True
            os.environ["SECRET_KEY"] = "Your secret key"
            os.environ["STRIPE_PUBLIC_KEY"] = "Your stripe public key"
            os.environ["STRIPE_SECRET_KEY"] = "Your stripe secret key"
            os.environ["STRIPE_WH_SECRET"] = "Your stripe webhook secret key"
            ```

    - Your stripe variables can be found on your stripe dashboard. 
    - You can generate the "SECRET_KEY" at [Djcrety](https://djecrety.ir/)

7. To set up the database migrate the database models by typing the following commands into the terminal: 
    - ```
        python3 manage.py showmigrations
        python3 manage.py makemigrations
        python3 manage.py migrate
        ```

8. To load the product fixtures into the database type the following commands into the terminal:
    - ```
        python3 manage.py loaddata products
        python3 manage.py loaddata categories
        python3 manage.py loaddata brands
        ```

9. Create a superuser to have access to the django admin dashboard type the following commands into the terminal:
    - ```
        python3 manage.py createsuperuser
        ```
    - Then set up the account by adding your username, email and password. 

10. Finally, run the app locally by typing the following command into the terminal: 
    - ```
        python3 manage.py runserver
        ```


## Deploy to Heroku

1. Create a Heroku app: 
    - Go to [Heroku](https://www.heroku.com/) and create an account if you do not have one yet. 
    - From the dashboard click on 'new app' button, name your app and choose the region closest to you. 
    - On the resources tab set up a new Postgres database by searching for 'Postgres'.
2. On your IDE, install 'dj_database_url' & 'psycopg2' to enable the use of the Postgres database: 
    - In the terminal type the following commands:
        - ```
            pip3 install dj_database_url
            pip3 install psycopg2-binary
            ```
3. Add the downloaded dependencies to the requirements file:
    - ```
        pip3 freeze > requirements.txt
        ```
4. To setup the new database go to to settings.py, import 'dj_database_url', comment out the default database configuration and replace the default database with the following: 
    - ```
        import dj_database_url

        DATABASES = {
            'default': dj_database_url.parse("The URL of your Heroku Postgres database")
        }
        ```
5. Run all migrations to the new Postgres database by entering the following command in the terminal:
    - ```
        python3 manage.py migrate
        ```
6. Load the product data from the fixture files into the new database: 
    - ```
        python3 manage.py loaddata products
        python3 manage.py loaddata categories
        python3 manage.py loaddata brands
        ```
7. Create a superuser by typing the following command into the terminal:
    - ```
        python3 manage.py createsuperuser
        ```
    - Then set up the account by adding your username, email and password. 
8. In settings.py set up the following to use the Postgres database when the app is running on Heroku and the SQLite3 when the app is running locally:
    - ```
        if 'DATABASE_URL' in os.environ:
            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
        else:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
        ```
9. Install Gunicorn (which will act as our webserver) by typing the following commands into the terminal:
    - ```
        pip3 install gunicorn
        pip3 freeze > requirements.txt
        ```
10. Create a procfile by typing the following command into the terminal:
    - ```
        touch Gunicorn
        ```
11. Type the following into the procfile: 
    - ```
        web: gunicorn flame.wsgi:application
        ```
12. Log in into the Heroku terminal:
    - ```
        heroku login -i
        ```
13. Disable collectstatic to prevent Heroku from collecting static files when deployed, by typing the following command into the terminal: 
    - ```
        heroku config:set DISABLE_COLLECTSTATIC=1 --app "heroku_app_name"
        ```
14. In settings.py add the hostname of the Heroku app, and allow localhost: 
    - ```
        ALLOWED_HOSTS = ['"heroku_app_name".herokuapp.com', 'localhost']
        ```
15. Deploy to Heroku by typing the following commands into the terminal: 
    - ```
        heroku git:remote -a "heroku_app_name"
        git push heroku master
        ```
16. To set up automatic deployments in Heroku when pushing code to github:
    - On the deploy tab, connect to github by searching for the repository name and clicking 'Connect'.
    - Click 'Enable Automatic Deploys" 
17. Generate a django secret key at [Djcrety](https://djecrety.ir/) and add it to 'Settings' > 'Config variables' in Heroku.
18. Update the settings.py file to collect the secret key from the environment, and use an empty string as default: 
    - ```
        SECRET_KEY = os.environ.get('SECRET_KEY', '')
        ```
19. Set debug to be true only if there's a variable called "DEVELOPMENT" in the environment. 
    - ```
        DEBUG = 'DEVELOPMENT' in os.environ
        ```

## AWS - Static files storage

### Create a New Bucket

1. Go to to [Amazon AWS](https://aws.amazon.com/) and sign in/sign up. 
2. From the 'Services' tab on the AWS Management Console, search 'S3' and select it.
3. Click the 'Create a new bucket' button: 
    - Enter a bucket name (recommended to be the same name as the Heroku App) and a region (enter the region that is closest to you)
    - Uncheck the "Block all public access" checkbox and confirm that the Bucket will be public.
    - Click the "Create bucket" button. 
4. Change settings by clicking on the bucket that appears: 
    - Click the 'Properties' tab and turn on static website hosting.
    - Fill in index.html and error.html as default.
    - Click the 'permission' tab and make the following changes:
        1. Set the CORS configuration to: 
            - ```
                [
                    {
                        "AllowedHeaders": [
                            "Authorization"
                        ],
                        "AllowedMethods": [
                            "GET"
                        ],
                        "AllowedOrigins": [
                            "*"
                        ],
                        "ExposeHeaders": []
                    }
                ]
                ```
        2. Go to the Bucket Policy tab and click 'Edit' > 'Policy Generator':
            - Select the following options:
                - Policy Type: "S3 Bucket Policy"
                - Principal: "*"
                - Actions: "GetObject"
                - ARN: Copy the ARN from the permissions tab
            - Copy the JSON document from the new policy into the Bucket Policy editor. 
            - Add a "/*" to the end of the resource key to allow access to all resources in this bucket.
            - Click the "Save" button. 
        3. Go to the 'Access Control List' section, and set the object permission to 'Everyone'.

### Create AWS Groups, Policies and Users

1. From the services menu go to IAM.
2. From the Access Management dropdown select 'User Groups'. 
    - Click the 'Create New Group" button
    - Name your group (associated with the S3 Bucket name)
    - Click 'Next' until the last page, then click the 'Save' button. 
3. From the Access Management dropdown select 'Policies'
    - Click the 'Create Policy' button: 
        - Go to the JSON tab and click 'Import Managed Policy'
        - Search for S3 then select 'AmazonS3FullAccess' and click "Import".
        - Get the ARN from the S3 bucket policy page and paste it in the "Resource" field as a list. Add two ARN's, one for the bucket itself and another for all files and folders in the bucket ("/*" at the end of the string): 
            - ```
                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Action": [
                                "s3:*",
                                "s3-object-lambda:*"
                            ],
                            "Resource": [
                                "arn:aws:s3:::milestone-project-4-flame",
                                "arn:aws:s3:::milestone-project-4-flame/*"
                            ]
                        }
                    ]
                }
                ```
        - Click the "Review Policy" button and give the policy a name and description and click the "Create Policy" button.
4. Go back to the "User Groups" page:
    - Click the group you want to attach the policy to and click "Attach policy" 
    - Search for the policy that has been created and attach it.
5. From the Access Management dropdown click "Users" > "Add Users" : 
    - Enter a user name and select the "Programmatic access' checkbox and select next
    - On the next page add the user to the group that was created and click through the end to create the user. 
    - Once the user is created download the CSV file containing the user's access key and secret access key (needed to authenticate the user from the Django app). 

### Connect Django to S3

1. To connect the S3 bucket to django install the following packages and add them to the requirements file:
    - ```
        pip3 install boto3
        pip3 install django_storages
        ```
       ```
        pip3 freeze > requirements.txt
        ```
    - Add (Django) storages to the list of INSTALLED_APPS in settings.py.

2. Update the settings.py file to tell Django which bucket it should be communicating with. To run this only on Heroku, add an if statement to check if theres an environment variable called USE_AWS: 
    - ```
        if 'USE_AWS' in os.environ:
            AWS_STORAGE_BUCKET_NAME = 'milestone-project-4-flame'
            AWS_S3_REGION_NAME = 'eu-north-1'
            AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
            AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

            STATICFILES_STORAGE = 'custom_storages.StaticStorage'
            STATICFILES_LOCATION = 'static'
            DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
            MEDIAFILES_LOCATION = 'media'

            STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
            MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
        ```
    - In Heroku update the config variables: 
        - USE_AWS =  True 
        - AWS_ACCESS_KEY_ID = From the IAM user's data CSV file
        - AWS_SECRET_ACCESS_KEY = From the the IAM user's data CSV file
    - Remove the DISABLE_COLLECTSTATIC variable to allow django to collect static files and upload them to S3. 
3. Create a custom_storages.py file to tell Django we want to use s3 to store our static and media files in production:
    - ```
        from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage


        class StaticStorage(S3Boto3Storage):
            location = settings.STATICFILES_LOCATION


        class MediaStorage(S3Boto3Storage):
            location = settings.MEDIAFILES_LOCATION
        ```
4. In the S3 bucket create a new folder called 'media':
    - Inside the media folder click "Upload" > "Add files" and select all the products, blog and other images
    - Select 'Grant public read access to these objects' 
    - Click through to 'upload'. 

## Connect Stripe to Heroku

1. Sign in/Sign up to [Stripe](https://stripe.com/gb) 
2. From the dashboard go to 'Developer' > 'API Keys'. Copy the public and secret keys and add them to Heroku config variables:
    - STRIPE_PUBLIC_KEY = Public key from Stripe
      STRIPE_SECRET_KEY = Secret ket from Stripe
3. Add a new webhook endpoint:
    - Go to 'Webhooks' in the developers menu on stripe and click the 'Add endpoint' button: 
    - Add the endpoint as the Heroku app's URL followed by "checkout/wh/", and select 'Receive all events': 
        - ```
            https://milestone-project-4-flame.herokuapp.com/checkout/wh/
            ```
4. Copy the signing secret for the webhook and add it to the heroku config variables: 
    - STRIPE_WH_SECRET = Secret webhook ket from Stripe 


