# We Are Social - Social Entrepreneurship Hub - Project for Stream 3 - Code Institute

This project is a Full Stack Web Application - It is a Social Entrepreneurship Hub that connects digital entrepreneurs.
Users need to pay a 4.99 euros fee to join in. Payment is taken securely using Stripe. Then the website helps them
share and vote ideas on the forum, read Blog entries, buy products and subscribe to monthly magazines.

It has been created using Pycharm and:

- Django Framework 1.9.8
- Includes modules for:
  -   Email Authentication,
  -   Stripe payments,
  -   PayPal e-commerce,
  -   PayPal subscriptions,
  -   Blog,
  -   Forum and
  -   Polls.
- Uses Bootstrap and Font Awesome for responsiveness
- Uses jQuery for animations
- Tinymce JavaScript for creating posts on the forum

The design is simple and flat, responsive and easy to understand.

The user has a navigation bar that shows the main features of the website.
The basic links available to all users are: "Home", "About", "Contact", "Register" and "Log In".
"Contact" page uses Google API to locate the Global Offices of We Are Social.

If the user decides to Register then he needs to pay the 4.99 fee and then he needs to login. Payment is taken securely
using Stripe.

Then after the user Logs in then there is extra services coming up on the navigation bar.
"Products", "Subscriptions", "Blog" and "Forum" are added.

"Products" is the e-commerce page that shows a table of products the user can buy using a one time payment through PayPal.
"Subscriptions" shows a table with magazines that the user can subscribe trhough PayPal and set up monthly payments.
"Blog" shows the latest Blog Posts.
"Forum" is the networking page that connects the users. They can share ideas by Creating New Threads and ask other users
to vote on Polls. Posts can be updated or edited at any time.