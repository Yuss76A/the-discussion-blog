# Discussion Room

![Responsive Mockup](static/images/screenshots/responsive.png)


## Introduction

Discussion Room is a user-friendly forum application designed to facilitate engaging and structured discussions among users. Built with Django, this project serves as my Project 4 for the CodeInstitute Full Stack Software Development Diploma. It provides a platform where users can create, share, and discuss topics of interest, fostering a collaborative environment for exchanging ideas and knowledge.


## User Stories 

1. **User Login Functionality**
   - As a registered user, I want to log in to my account so that I can access my saved preferences and activities.
   
   **Acceptance Criteria:**
   - Users can log in with their username and password.
   - An error message is displayed for invalid login attempts.
   - Users are redirected to their dashboard upon successful login.

2. **User Registration and Authentication**
   - As a new user, I want to create an account so that I can participate in discussions and post comments.

   **Acceptance Criteria:**
   - Users must provide a valid email address and a unique username.
   - Passwords must adhere to security rules (e.g., minimum length, special characters).

3. **Post Creation Functionality**
   - As a registered user, I want to create a post so that I can share my knowledge or request help on a topic.

   **Acceptance Criteria:**
   - Users can create a post with a title and content.
   - The post is saved to the database upon submission.
   - Users receive a confirmation message upon successful publication.

4. **Post Editing Functionality**
   - As a user, I want to edit my posts so that I can correct mistakes or update information after it has been published.

   **Acceptance Criteria:**
   - Users can access their published posts for editing.
   - Changes are reflected immediately upon saving.
   - Users receive an update notification about their changes.

5. **Comment Deletion Functionality**
   - As a user, I want to delete comments I have made so that I can remove anything I no longer wish to be visible.

   **Acceptance Criteria:**
   - Users can delete a comment with a confirmation prompt.
   - The comment must be removed from the display below the respective post immediately after deletion.

6. **Post Deletion Functionality**
   - As a user, I want to delete my posts if I want to remove them from the platform entirely.

   **Acceptance Criteria:**
   - Users can delete a post with a confirmation dialog.
   - The post must be removed from all views immediately after deletion.

7. **Comment Editing Functionality**
   - As a registered user, I want to edit my comment so that I can clarify my thoughts or correct errors.

   **Acceptance Criteria:**
   - Users can access their comments for editing.
   - Edited comments indicate that they have been modified.

8. **User Account Management for Admins**
   - As an admin, I want to manage user accounts so that I can maintain community standards.

   **Acceptance Criteria:**
   - Admins can view a list of all users.
   - Admins can update user roles and delete accounts if necessary.
   - Changes made are logged for auditing purposes.

9. **Commenting Functionality**
   - As a registered user, I want to comment on posts so that I can engage in discussions and share my thoughts.

   **Acceptance Criteria:**
   - Users can add a comment to any post.
   - Comments are displayed in chronological order below the respective post.
   - Users receive a notification if someone replies to their comment.

10. **Password Reset Functionality**
   - As a registered user, I want to reset my password if I forget it so that I can regain access to my account.

   **Acceptance Criteria:**
   - Users can request a password reset link through their registered email.
   - The link should expire after a specified time after using it.
   - Users should be able to set a new password after following the link.

11. **User Profile Management Functionality**
   - As a registered user, I would like to access my account to modify my avatar picture, username, and email so that I can keep my profile up-to-date and personalized.

   **Acceptance Criteria:**
   - Users can navigate to their account settings to access their profile.
   - Users can upload a new avatar picture.
   - Users can change their username and email.
   - Changes are saved immediately upon submission.
   - Users receive a confirmation message after successfully updating their profile.

12. **Notification Functionality**
   - As a registered user, I would like to receive notifications if someone replies to my comment or post so that I can engage in the conversation and stay informed about the discussions.

   **Acceptance Criteria:**
   - Users receive a notification when someone replies to their comment, including a brief excerpt of the comment to which they are replying.
   - Users receive a notification when someone replies to their post, including a short version of the original comment made on the post.
   - Notifications include relevant details, such as the username of the replier and the content of the reply.
   - Notifications can be accessed through a dedicated notifications page.
   - Users can delete notifications if they no longer wish to keep them.

13. **Category Navigation Functionality**
   - As a user, I would like to navigate between several categories so that I can easily find discussions on topics that interest me.

   **Acceptance Criteria:**
   - Users can see a list of available categories on the main page.
   - Users can click on a category to view all posts associated with that category.
   - Posts should be displayed in chronological order within the selected category.
   - The selected category should be highlighted to indicate to users which category they are currently viewing.

   15. **Support and Collaboration Functionality**
   - As a user, I would like to access the Support and Collaboration page so that I can contact the forum team for any reason, such as collaboration inquiries, suggestions to improve the forum, or reporting activity that I find inappropriate.

   **Acceptance Criteria:**
   - Users can navigate to the Support and Collaboration page.
   - Users can fill in a form that includes fields for their name, email, and message.
   - Users receive a confirmation message after successfully submitting their inquiry or suggestion.
   - The Support form should include validation to ensure all required fields are completed properly.
   - Submitted messages are stored and can be reviewed by the forum team for follow-up actions.

### Admin Stories

1. User Account Management

* As an admin, I want to create user accounts so that new users can register and participate in discussions.
* As an admin, I want to view a list of all user accounts so that I can manage user access and activity.
* As an admin, I want to disable or delete user accounts so that I can remove users who violate community guidelines or no longer participate.

2. Post Management

* As an admin, I want to view all posts on the platform so that I can monitor discussions and ensure they align with community standards.
* As an admin, I want to delete posts that are inappropriate or violate community guidelines so that I can maintain a respectful discussion environment.
* As an admin, I want to edit posts to correct any misinformation or update content when necessary.

3. Comment Management

* As an admin, I want to view all comments made on posts so that I can ensure discussions remain constructive.
* As an admin, I want to delete comments that are offensive or inappropriate to keep the platform safe for users.
* As an admin, I want to manage reported comments or posts that users flag to investigate and take appropriate action.

4. Moderation Tools

* As an admin, I want to receive notifications about user reports on posts or comments so that I can respond promptly and uphold community standards.
* As an admin, I want to ban users for repeat offenses to protect the community from disruptive behavior.

#### Notes on User Stories

When conceptualizing the Discussion Room project, I identified these user stories as the core functionalities that are fundamental to the platform's purpose. These stories represent the key features that facilitate user interaction and engagement within the forum, forming the foundation upon which the rest of the application is built.

While the development process has allowed for the addition of smaller features and enhancements along the way, I believe that these main user stories encapsulate the most critical aspects of the project. Ensuring that users can effectively log in, register, create and manage posts and comments, and receive notifications about their activities is essential for fostering a vibrant and collaborative community.

By prioritizing these core functionalities, I aimed to create a user-friendly experience that encourages participation and supports knowledge sharing among users. As the project evolves, I will continue to enhance its features based on user feedback and emerging needs, but these foundational user stories will always remain at the heart of the Discussion Room.

Github User Stories : [Github User Stories](https://github.com/users/Yuss76A/projects/9/views/1)

### Website Goals

1. Foster Community Engagement:

* Create a welcoming space where users can freely discuss various topics, share ideas, and connect over shared interests.
* Encourage users to participate by providing tools for posting, commenting, and liking content.

2. Facilitate Knowledge Sharing:

* Provide a platform where users can ask questions and receive answers, promoting learning and understanding within the community.
* Highlight valuable contributions through features such as trending posts or top contributors.

3. Ensure User Safety and Moderation:

* Implement moderation tools and guidelines to maintain a respectful environment.
* Create mechanisms for users to report inappropriate content, helping to manage community standards effectively.

4. Enhance User Experience:

* Design a user-friendly interface that is easy to navigate, enabling users to quickly find discussions relevant to their interests.
* Optimize the site for responsiveness across various devices, ensuring accessibility for all users.

5. Support User Account Management:

* Allow users to easily register, log in, and manage their profiles, posts, and comments.
* Implement account security measures to protect user data and privacy.

6. Implement Robust Search and Filter Options:

* Provide powerful search functionality and category filtering to help users find specific discussions or topics quickly.
* Enhance user engagement by making content discovery intuitive and straightforward.

6. Promote Interaction through Notifications:

* Keep users informed about replies to their comments, likes, and new posts relevant to their interests, encouraging them to return to the site.
* Use notifications strategically to enhance user engagement and activity on the platform.


### Requirements 

* Landing page.
* About section.
* User registration and login.
* Post creation and management.
* Commenting functionality.
* Categories for filtering posts.
* Search functionality for posts.
* Trending posts section.
* User profile management.
* Admin dashboard access.
* CRUD functionality for posts and comments.
* User notifications system.
* Responsive design.
* Links to social media.


## Design Choices 

### Fonts

[Google Fonts](https://fonts.google.com/ "Google Fonts") The Discussion Room website utilizes [Poppins](https://fonts.google.com/specimen/Poppins) for headings, ensuring a modern and clean aesthetic, while Arial serves as the primary font for body text due to its simplicity and readability.


### Colours

![Colour Palette](static/images/screenshots/colorpalette1.png)
![Colour Palette](static/images/screenshots/colorpalette2.png)
![Colour Palette](static/images/screenshots/colorpalette3.png)


1. rgb(230, 230, 250)

Purpose: Background color for the body of the website, creating a soft and inviting atmosphere.

2. #444444

Purpose: Primary text color for headings (h1, h2, etc.) and paragraphs (p), ensuring good readability.

3. rgba(30, 15, 45, 1) and rgba(70, 50, 120, 1)

Purpose: Used in the background of the .bg-steel class, providing a linear gradient effect that adds visual interest.

4. #003366

Purpose: Background color for the custom navbar, giving it a deep, professional look.

5. #d1e7dd

Purpose: Color for navigation links in the navbar, creating a clear contrast against the navbar background.

6. #ffffff

Purpose: Hover color for navigation links, ensuring visibility and interaction clarity.

7. #fefefe

Purpose: Background color for sections with the .content-section class, creating a clean and light appearance for content areas.

8. #000000

Purpose: Primary color for article titles, providing a strong contrast that makes the titles stand out.

9. #908690

Purpose: Hover color for article titles, adding a subtle change to indicate interactivity.

10. #dcdcdc

Purpose: Border color for .article-metadata, providing a subtle division between metadata and content.

11. #f5f5f5

Purpose: Background color for comments, ensuring they are distinguishable from the main content area.

12. #007bff

Purpose: Color for links in notifications and other emphasized text, providing a vibrant, clickable appearance.

13. #6c757d

Purpose: Default color for navbar links, offering a neutral tone that fits well within the overall design.

14. #343a40

Purpose: Default button background color, providing a dark contrasting color that highlights interactive elements.

15. #495057

Purpose: Button hover color, slightly lighter than the default, enhancing the visual indication when a user interacts with buttons.

16. #e6e6fa

Purpose: Text color for welcome messages, contributing to a lighter overall tone for user greetings.

17. #121212 and #ffffff (used in dark mode styles)

Purpose: Background and text colors respectively for dark mode support, ensuring sufficient contrast and readability.

18. #f8f9fa

Purpose: Background color for the account section and highlights, contributing to a clean and modern look.

19. #03e9f4

Purpose: Color used for various hover effects and highlights, providing a vibrant shade that draws attention.

20. #b2c39c

Purpose: Hover color for authentication links, creating an appealing visual effect when interacted with.

21. #777575

Background for content sections in dark mode.

22. #28a745

Color used for likes, visually indicating positive feedback or approval.

23. #dc3545

Color used for dislikes, indicating negative feedback or disapproval.

24. #FFA500

Color used for Code Institute promotional links, drawing attention and encouraging user interaction.

## Dark Mode Specific Colors

1. #000000

This is used as the background color for the entire site when dark mode is activated

2. Primary Text Color:

#FFFFFF: This is the primary text color used in dark mode to ensure high contrast against the black background for legibility.

3. Comment Background:

#777575: This color is assigned to the background of comments when dark mode is active, distinguishing them from the main content.

4. Highlight Color for Effects:

#03e9f4: This color is often used for elements that require attention, such as links or buttons, maintaining visibility in dark mode.

5. Muted Text Color:

#E6E6FA: This is a subtle, softer color reserved for muted text in dark mode, providing a visual hierarchy without causing strain against the darker background.

## Color Choices 

Color Choices
In developing the Discussion Room project, I've carefully selected and noted the colors used to create an engaging and visually appealing website. The goal was to design a platform that not only facilitates discussions but also captures the attention of users through thoughtful color usage.

The colors chosen aim to provide a harmonious balance that enhances readability, establishes a welcoming atmosphere, and encourages interaction. Here is a comprehensive list of the colors used, along with their purposes.

While I have made an effort to document all the colors in use, it’s possible that a few may have been overlooked in the process. Should any colors be missing, they will be added to future updates as we continue to enhance the user experience and aesthetic appeal of the site.

By implementing this color scheme, I aspire to create a vibrant yet cohesive environment that invites users to explore, share, and engage in meaningful conversations within the community.

## Color Palette 

For the color palette, I used [Color Palette](https://coolors.co/).

## Icons

The icons used for the site were sourced from [Font Awesome](https://fontawesome.com/ "Font Awesome")

## Structure

The Discussion Room provides a simple yet engaging web platform, aiming to establish its unique color scheme and style. The navigation bar includes several links, offering quick access to various sections, such as About Us, Create a Post, Home Page, Logout, and the Notifications Page.

The footer features additional links for Highlights, Collaboration Requests, About the Team, and Admin Page, ensuring users can easily find important information. This footer is fixed at the bottom of the page, providing users with continuous access to these essential resources, enhancing navigation and overall user experience.

Additionally, the site includes a Trending Topics section that showcases random posts and a dedicated Advertisement Window for promotional content. Above the trending topics, users will find Categories to help them navigate discussions more effectively.

To fully engage with the content—whether by commenting or posting—users must register for an account, fostering a community of committed participants.


### Database Models

User Profile (Account):<br>

| Object             | Field           |
|--------------------|-----------------|
|      user          |  OneToOneField  |
|      avatar        | CloudinaryField |

Post:<br>

| Object         | Field           |
|----------------|-----------------|
|   title        |    CharField    |
|  content       |    TextField    |
|  author        |    ForeignKey   |
| date_posted    |   DateTimeField |
| category       |   ForeignKey    |

Comment:<br>

| Object         | Field           |
|----------------|-----------------|
|   content      |    TextField    |
|    post        |    ForeignKey   |
|    author      |    ForeignKey   |
|  created_at    |  DateTimeField  |
|   likes        |   IntegerField  |
|  dislikes      |   IntegerField  |
|   parent       |    ForeignKey   |

Notification:<br>

| Object         | Field           |
|----------------|-----------------|
|   user         |    ForeignKey   |
|  message       |    TextField    |
|  is_read       |    BooleanField |
| created_at     |    DateTimeField|
| comment        |    ForeignKey   |

Category:<br>

| Object         | Field           |
|----------------|-----------------|
|   name         |    CharField    |


## Entity-Relationship Diagram (ERD)

*Entity-Relationship Diagram (ERD)*<br>
![Entity-Relationship Diagram (ERD)](static/images/screenshots/erd.png)

1. User:

* id (Primary Key)

* username

* first_name

* last_name

* email

* password

2. Account:

* id (Primary Key)

* user_id (Foreign Key referencing User)

* avatar

3. Post:

* id (Primary Key)

* title

* content

* date_posted

* author_id (Foreign Key referencing User)

* likes

* dislikes

* category_id (Foreign Key referencing Category)

4. Comment:

* id (Primary Key)

* post_id (Foreign Key referencing Post)

* author_id (Foreign Key referencing User)

* content

* created_at

* likes

* dislikes

* parent_id (optional Foreign Key referencing Comment for replies)

5. Category:

* id (Primary Key)

* name

6. Notification:

* id (Primary Key)

* user_id (Foreign Key referencing User)

* message

* comment_id (optional Foreign Key referencing Comment)

* created_at

* is_read

7. CollaborateRequest:

id (Primary Key)

* name

* email

* message

* created_at

- Characteristics of the CollaborateRequest Entity

1. Lack of Relationships:

The CollaborateRequest model does not reference any other models via foreign keys. It contains attributes such as name, email, message, and created_at but does not have fields that link it to other entities, such as User or Post.
Because it does not relate to other entities, it functions independently within the application.

2. Purpose:

The primary purpose of the CollaborateRequest model is to collect and store collaboration inquiries from users. It gathers data without needing to connect directly to the user accounts or posts, making it self-contained.
It can be seen as a standalone input form that exists for specific functionality (collaboration inquiries), separate from the core user and content management of the application.

- Relationships

1. User

* 1-to-1 with Account (user_id in Account references id in User)

* 1-to-many with Post (author_id in Post references id in User)

* 1-to-many with Comment (author_id in Comment references id in User)

* 1-to-many with Notification (user_id in Notification references id in User)

2. Post

* Many-to-1 with User (author_id in Post references id in User)

* Many-to-1 with Category (category_id in Post references id in Category)

* 1-to-many with Comment (post_id in Comment references id in Post)

3. Comment

* Many-to-1 with Post (post_id in Comment references id in Post)

* Many-to-1 with User (author_id in Comment references id in User)

* Self-referencing for replies (parent_id in Comment references id in Comment)

4. Category

* 1-to-many with Post (category_id in Post references id in Category)

5. Notification

* Many-to-1 with User (user_id in Notification references id in User)

* Optional Many-to-1 with Comment (comment_id in Notification references id in Comment)

6. CollaborateRequest

* No relationships (independent entity)

## Wireframes

Wireframes have been created using [Balsamic](https://balsamiq.com "Balsamic"). These wireframes provided an initial blueprint for the layout of my forum project. However, the design evolved and adapted throughout the development process, resulting in some changes in the final product.

*Main Page Desktop Wireframe*<br>
![Main Page Desktop Wireframe](static/images/screenshots/mainpagedesktop.png)

*Main Page Mobile Wireframe*<br>
![Main Page Mobile Wireframe](static/images/screenshots/mainpagemobile.png)

*About Us Desktop Wireframe*<br>
![About Us Desktop Wireframe](static/images/screenshots/aboutuspagedesktop.png)

*About Us Mobile Wireframe*<br>
![About Us Mobiel Wireframe](static/images/screenshots/aboutuspagemobile.png)

*Create Post Desktop Wireframe*<br>
![Create Pos Desktop Wireframe](static/images/screenshots/createapostdesktop.png)

*Create Post Mobile Wireframe*<br>
![Create Post Mobile Wireframe](static/images/screenshots/createanewpostmobile.png)

*Account Page Desktop Wireframe*<br>
![Account Page Desktop Wireframe](static/images/screenshots/accountpagedesktop.png)

*Account Page Mobile Wireframe*<br>
![Account Page Mobile Wireframe](static/images/screenshots/accountpagemobile.png)

*Edit Your Profile Desktop Wireframe*<br>
![Edit Your Profile Desktop Wireframe](static/images/screenshots/edityourprofiledesktop.png)

*Edit Your Profile Mobile Wireframe*<br>
![Edit Your Profile Mobile Wireframe](static/images/screenshots/edityourprofilemobile.png)

*Logged Out Window Desktop Wireframe*<br>
![Logged Out Window Desktop Wireframe](static/images/screenshots/loggedoutdesktop.png)

*Logged Out Window Mobile Wireframe*<br>
![Logged Out Window Mobile Wireframe](static/images/screenshots/loggedoutmobile.png)

*Notifications Page Desktop Wireframe*<br>
![Notifications Page Desktop Wireframe](static/images/screenshots/notificationpagedesktop.png)

*Notifications Page Mobile Wireframe*<br>
![Notifications Page Mobile Wireframe](static/images/screenshots/notificationsmobile.png)

*About Me Page Desktop Wireframe*<br>
![About Me Page Desktop Wireframe](static/images/screenshots/aboutmedesktop.png)

*About Me Page Mobile Wireframe*<br>
![About Me Page Mobile Wireframe](static/images/screenshots/aboutmemobile.png)

*Support Page Desktop Wireframe*<br>
![Support Page Desktop Wireframe](static/images/screenshots/supportpagedesktop.png)

*Support Page Mobile Wireframe*<br>
![Support Page Mobile Wireframe](static/images/screenshots/supportpagemobile.png)

*Highlights Page Desktop Wireframe*<br>
![Highlights Page Desktop Wireframe](static/images/screenshots/highlightspagedesktop.png)

*Highlights Page Mobile Wireframe*<br>
![Highlights Page Mobile Wireframe](static/images/screenshots/highlightspagemobile.png)

*Reading Post Desktop Wireframe*<br>
![Reading Post Desktop Wireframe](static/images/screenshots/readingpostdesktop.png)

*Reading Post Mobile Wireframe*<br>
![Reading Post Mobile Wireframe](static/images/screenshots/readingapostmobile.png)

*Login Page Desktop Wireframe*<br>
![Login Page Desktop Wireframe](static/images/screenshots/loginpagedesktop.png)

*Login Page Mobile Wireframe*<br>
![Login Page Mobile Wireframe](static/images/screenshots/loginpagemobile.png)

*Register Page Desktop Wireframe*<br>
![Register Page Desktop Wireframe](static/images/screenshots/registerpagedesktop.png)

*Register Page Mobile Wireframe*<br>
![Register Page Mobile Wireframe](static/images/screenshots/registermobile.png)

*Post Delete Desktop Wireframe*<br>
![Post Delete Desktop Wireframe](static/images/screenshots/postdeletepagedesktop.png)

*Post Delete Mobile Wireframe*<br>
![Post Delete Mobile Wireframe](static/images/screenshots/postdeletepagemobile.png)

*Update Comment Desktop Wireframe*<br>
![Update Comment Desktop Wireframe](static/images/screenshots/updatecommentdesktop.png)

*Update Comment Mobile Wireframe*<br>
![Update Comment Mobile Wireframe](static/images/screenshots/updatecommentmobile.png)

## Note

As with many forums and web pages, the mobile wireframe reflects the layout users will see when they interact with the site on smaller screens. When viewing the forum on mobile, users will need to scroll down to access all content on the page. The design shown in the mobile wireframe illustrates the initial view, while scrolling reveals the complete set of features and discussions.

The post edit wireframe is not presented as a standalone design because it utilizes the same layout and style as the create post section.


## Features 

### Navbar

The navbar is designed to be simple and user-friendly. When a user is logged out, the left side displays the name of the forum, Discussion Room, which serves as a direct link to the home page. On the right side, there are links for Home, About Us, Login, and Register sections. This straightforward layout ensures easy navigation without any complex features, allowing users to quickly access key areas of the website.

The navbar includes hover effects that enhance the user experience for all users, whether logged in or not. The title Discussion Room features a distinct hover effect that draws attention, while the links present in the navbar also have their own hover styles, providing clear visual feedback when users interact with the navigation elements.

*Navbar Logged Out*<br>
![Navbar Logged Out](static/images/screenshots/loggedoutnavbar.png)

### Navbar Logged In

When a user is logged in, the navbar retains the Discussion Room name on the left side, serving as a direct link back to the home page. In the center, a welcome message appears, greeting the user with "Welcome, User!" 

The navbar includes links to the Home and About Us pages, accessible to both logged-in and logged-out users. Additionally, it features a Create a New Post section that allows users to initiate discussions. 

Users can manage their profiles via the Account link, log out using the Logout button, and access the Notifications page to view replies to comments they have posted. This layout promotes ease of access and enhances the overall user experience.

*Navbar Logged In*<br>
![Navbar Logged In](static/images/screenshots/navbar.png)

### Mobile Navbar

The mobile version of the navbar features a collapsible design that enhances usability on smaller screens. When the user touches the navbar at the top of the screen, it expands downwards to reveal all sections. This functionality ensures that users can easily access important links, regardless of whether they are logged in or logged out.

Both logged-out and logged-in users will see the following sections:

Discussion Room: A link back to the home page.
* Welcome Message: Displayed for logged-in users.
* Home: Accessible to all users.
* About Us: Accessible to all users.
* Create a New Post: Available for logged-in users.
* Account: Access to user profile for logged-in users.
* Logout: Available for logged-in users.
* Notifications: Link to see replies to comments for logged-in users.
* This collapsible navbar format provides a clean and efficient navigation experience, making it easy for users to engage with the forum content.

*Navbar Logged Out Mobile*<br>
![Navbar Logged Out Mobile](static/images/screenshots/navbarmobile.png)

*Navbar Logged In Mobile*<br>
![Navbar Logged In Mobile](static/images/screenshots/loggedinnavbar.png)

### Maine Page (Home Button)

The main page of the Discussion Room is designed to display 8 posts per page, with pagination functionality to navigate between different sets of posts easily.

At the top of the page, there is a search bar that allows users to search for posts using random words, titles, or phrases, enhancing content discovery.

On the right side of the page, there is a Trending Posts window that showcases random posts from the forum. This section refreshes each time the user reloads the page or navigates to another page, creating an engaging experience by introducing different content continually. The Trending Posts window is visible both to logged-in users and guests; however, to access any post from this section, users must log in.

At the top of the Trending Posts window, there are categories allowing users to filter posts. There are 4 categories available, each linking to the posts associated with that category, making it easier for users to find content of interest. 

Below the Trending Posts window, an Advertisement Window is included, which serves as a potential future feature to help maintain the forum project. This section can display ads relevant to the user base, providing an opportunity for monetization or informative promotions. Although its implementation can be adjusted in the future, it currently serves as an example of what may enhance the user experience.

*Maine Page Desktop*<br>
![Main Page Desktop](static/images/screenshots/pagehomedesktop.png)

### Main Page Mobile (Home Button )

The mobile version contains the same features as the desktop version; however, users need to scroll down to access some functions, including the Trending Posts window, categories, and the Advertisement Window. This scrolling functionality is common in many forum projects.

*Maine Page Mobile*<br>
![Main Page Mobile](static/images/screenshots/pagehomemobile.png)

### About Us 

In the About Us section, you'll find information about the Discussion Room forum, including the community rules that guide our interactions. This window can be accessed by both logged-in and logged-out users. We aim to create a welcoming environment where individuals can engage in discussions on various topics with kindness and respect.

Participants are encouraged to share their thoughts, ask questions, and connect with others, fostering a vibrant community that values diverse perspectives.

Community guidelines ensure a positive experience for all users, with a strong emphasis on constructive dialogue and mutual respect. We are dedicated to maintaining an inclusive space for everyone.

*About Us Desktop*<br>
![About Us Desktop](static/images/screenshots/pageaboutusdesktop.png)

*About Us Mobile*<br>
![About Us Mobile](static/images/screenshots/pageaboutusmobile.png)

### Log In Page

The Login section of the application is designed to provide a user-friendly interface for accessing user accounts. It features:

* Title: A visually appealing title in dark blue reads "Log In to Your Account," clearly indicating the purpose of this section.

* Input Fields: Users are presented with two input fields:

Username: A field for the user to enter their username, styled with a soft white background for easy readability.
Password: A field for entering the password, also featuring a soft white design to maintain consistency.

* A prominent button labeled "Log In," styled in a blue that matches the navbar and footer, allowing users to submit their credentials and access their accounts seamlessly.

* In light mode, we also have a "Forgot Password" button positioned before the "Don't have an account? Sign up" section. This button features a nice blue color that complements the overall website theme, ensuring it stands out while maintaining a cohesive design. This enhances user experience by providing easy access to the password recovery option.

* Sign-Up Prompt: Below the login form, there's a friendly reminder for users who do not have an account, prompting them to "Sign Up" if they need to create a new one.

* Error Messaging: Should the user enter incorrect login information, an error message will be displayed to alert them, stating, "Please enter a correct username and password." It's important to note that both fields may be case-sensitive, which means users must enter their credentials precisely.

This design aims to ensure users have an intuitive experience while logging in, promoting both functionality and ease of use.

*Login Page Desktop*<br>
![Login Page Desktop](static/images/screenshots/pagelogindesktop.png)

*Login Page Mobile*<br>
![Login Page Mobile](static/images/screenshots/pageloginmobile.png)

### Register Page

The Registration page is designed to facilitate the account creation process for users. It features:

* Title: A striking dark blue title "Create Your Account" immediately captures the user's attention and clearly indicates the purpose of the page.

* Input Fields: Users are provided with six input fields, all styled with a soft white background for a pleasant aesthetic:

* Username: This field includes a requirements statement to ensure users understand the necessary criteria for creating a valid username.
* First Name: A field for users to input their first name.
* Last Name: A field for users to input their last name.
* Email: A field to enter a valid email address, highlighting the importance of accuracy for communication purposes.
* Password: This field includes specific rules that must be followed, ensuring the password meets required criteria.
* Password Confirmation: A field to re-enter the password for verification.
* Error Messaging: If users enter incorrect information in the password fields or if they attempt to register a username that is already taken, a warning message will appear below the respective input field. This feedback helps users correct their entries promptly.

* User Guidance: Users are encouraged to enter accurate information in all fields to facilitate effective communication from our team regarding updates or any issues that may arise.

* At the end of the form, there is a prominent "Register Now" button styled in an attractive blue that matches the navbar and footer, allowing users to submit their registration details easily.

* Login Prompt: Additionally, at the bottom of the registration page, a message is displayed stating, "Already have an account? Log in," providing users with an easy way to navigate to the login page if they have previously registered.

This design aims to provide a straightforward and effective registration process, ensuring users can create their accounts with minimal friction while being informed at each step.

*Register Page Desktop*<br>
![Register Page Desktop](static/images/screenshots/pageregisterdesktop.png)

*Register Page Mobile*<br>
![Register Page Mobile](static/images/screenshots/pageregistermobile.png)

### Create A New Post

In the Create a New Post section, users can easily compose and publish new posts. This simple and intuitive interface includes fields for the post title, content, and a choice of category. Once the post is ready, users can click the Publish button to share it with the community. 

For those who wish to cancel the action, there is an option to go back, allowing users to navigate away without creating a new post.

*Create A New Post Desktop*<br>
![Create A New Post Desktop](static/images/screenshots/pagecreatepostdesktop.png)

*Create A New Post Mobile*<br>
![Create A New Post Mobile](static/images/screenshots/pagecreatepostmobile.png)

### Account

In the Account Section, users are presented with a visually appealing window that displays their profile picture, name, and email address. This section also includes social media links, allowing users to navigate to their profiles or find inspiration for new posts and updates they wish to share.

Additionally, there is an Update Profile button that directs users to the profile editing page, enabling them to make changes to their account information as needed.

*Account Page Desktop*<br>
![Account Page Desktop](static/images/screenshots/pageaccountdesktop.png)

*Account Page Mobile*<br>
![Account Page Mobile](static/images/screenshots/pageaccountmobile.png)

### Edit Your Profile Window

The Edit Profile Page features a visually appealing soft white container with a prominent blue title that clearly conveys the page's purpose. Inside this container, users will encounter input fields for updating their username and email, set against a light grey background to enhance readability.

Additionally, there is a specific section designated for changing the avatar image. This section showcases the current profile picture, allowing users to easily view their existing image prior to making any updates.

At the bottom of the page, a "Save Changes" button is displayed with a vibrant blue that matches the footer and navbar, featuring white text to enable users to submit their updates. Adjacent to it, a straightforward blue link allows users to cancel and return, providing a convenient option to exit without applying changes.

Users are also shown a warning message when considering a username change, informing them that any changes made will be reflected in the system. Once updated, the new username will serve as their primary login identifier. Additionally, users are reminded to enter a valid email address, allowing our team to reach out concerning any significant updates or changes.

*Edit Your Profile Desktop*<br>
![Edit Your Profile Desktop](static/images/screenshots/pageeditprofiledesktop.png)

*Edit Your Profile Mobile*<br>
![Edit Your Profile Mobile](static/images/screenshots/pageeditprofilemobile.png)

### LogOut

When users click the Logout button, they will be logged out of their account. Following this action, they will see a window with a title in blue that says, "You Have Been Logged Out." Below the title, a subphrase reads, "We're sorry to see you go! Thank you for visiting our site," reinforcing a friendly atmosphere.

In this window, users will have two options:

* A button with a blue background and white letters labeled "Log In Again" to access their account.
* A second button with a dark grey background and white letters labeled "Return to Home" to navigate back to the main section of the forum.

*Logout Page Desktop*<br>
![Logout Page Desktop](static/images/screenshots/pagelogoutdesktop.png)

*Logout Page Mobile*<br>
![Logout Page Mobile](static/images/screenshots/pagelogoutmobile.png)

### Notifications

In the Notifications Page, users will see notifications for replies to comments they have posted on various forum posts. When users log in or when someone replies to their comment, a bell icon will appear next to the notification button, indicating that they have new notifications.

If there are no notifications, users will simply see a message stating that there are no notifications available, ensuring clear communication without unnecessary clutter.

*Notification Page Desktop*<br>
![Notification Page Desktop](static/images/screenshots/pagenotificationdesktop.png)

*Notification Page Mobile*<br>
![Notification Page Mobile](static/images/screenshots/pagenotificationmobile.png)

*Bell Icon*<br>
![Bell Icon](static/images/screenshots/bellicon.png)

*Delete Notification*<br>
![Delete Notification](static/images/screenshots/deletenotification.png)

On the Notifications Page, users will see notifications for interactions related to their comments on various forum posts. The notifications will inform users about two primary interactions: replies to comments they have posted and comments made on their posts. If a user has notifications, they will see messages formatted as follows:

1. Reply Notifications:

"User [username] replied to your comment: [main comment content]."
Each reply notification will include the date and time of the reply.

2. Comment Notifications:

"User [username] commented on your post: [post title or content]."
Each comment notification will also include the date and time of the comment.
Users will have options to Delete the notification or Go to the comment/post, allowing them to manage their interactions effectively.

*Notification Page with Notification Desktop*<br>
![Notification Page with Notification Desktop](static/images/screenshots/messagenotificationdesktop.png)

*Notification Page with Notification Mobile*<br>
![Notification Page with Notification Mobile](static/images/screenshots/messagenotificationmobile.png)

### About Me

In the About Me section, you'll learn about Yusein Ali, a 33-year-old with a diverse life journey. Born in Burgas, Bulgaria, he moved to Spain in 2001, pursued his passion for football in Turkey, and later returned to Bulgaria. In 2013, he moved to Luxembourg, where he continued to play football until relocating to Sweden in 2023.

Yusein has a border collie named Molly and is multilingual, speaking several languages including Bulgarian, Spanish, French, English, Turkish, Italian, Portuguese, and Luxembourgish, with Swedish currently being learned.

His passion for technology began in childhood, leading him to enroll in Code Institute in 2023 to enhance his programming skills. This forum, Discussion Room, is his fourth project out of five developed through Code Institute, inspired by the popular Spanish forum Forocoches.com.

Thank you for visiting and exploring the forum, where a welcoming space is provided for sharing and discussing ideas!

*About Me Page Desktop*<br>
![About Me Page Desktop](static/images/screenshots/pageaboutmedesktop.png)

*About Me Page Mobile*<br>
![About Me Page Mobile](static/images/screenshots/pageaboutmemobile.png)

### Support & Collaboration

In the Support and Collaboration section, users can easily get in touch with the administration team. They have the ability to report unusual activities or inappropriate behavior from users who disrespect others. Additionally, users can submit requests for collaboration or suggestions to enhance the forum.

The section includes fields for users to enter their name, email (to facilitate contact), and a message detailing their inquiry or report. Once completed, users can submit their information using the Submit button, ensuring their concerns and ideas are communicated effectively.

*Support & Collaboration Desktop*<br>
![Support & Collaboration Desktop](static/images/screenshots/pagesupportdesktop.png)

*Support & Collaboration Mobile*<br>
![Support & Collaboration Mobile](static/images/screenshots/pagesupportmobile.png)

### Admin Page (Control Panel)

The Admin Page (Control Panel) serves as the central control hub for administrators, granting them full rights to manage the forum effectively. Admins have the authority to monitor user activity, ensuring that community standards are upheld.

Through this page, admins can delete offensive posts and comments, as well as take necessary action against users who violate the forum rules. This functionality ensures a safe and respectful environment for all participants within the Discussion Room community.

*Admin Page Desktop*<br>
![Admin Page Desktop](static/images/screenshots/adminpagedekstop.png)

*Admin Page Mobile*<br>
![Admin Page Mobile](static/images/screenshots/adminpagemobile.png)

### Highlights

In the Thank You section, I want to express my heartfelt gratitude to Code Institute for making this project a reality. Their extensive resources and support have been instrumental in building my project and pursuing my passion for web development.

I extend special thanks to all the tutors who were always available to assist whenever I needed help. Your expertise and guidance greatly impacted my learning journey.

A special thank you goes to my amazing mentor, Iuliia Konovalova, for your unwavering support and mentorship. Your encouragement and insights helped me navigate through challenges and stay motivated.

I would also like to thank the GitHub team for providing an incredible platform that enabled effective collaboration and development of my project.

For more information about Code Institute, visit their website: https://codeinstitute.net/se/

*Highlights Page Desktop*<br>
![Highlights Page Desktop](static/images/screenshots/pagethankyoudesktop.png)

*Highlights Page Mobile*<br>
![Highlights Page Mobile](static/images/screenshots/pagethankyoumobile.png)

### Reading Post

Users will have the option to read posts in full detail, but this feature is only accessible to individuals who have an account and are logged in. On the right side of each post, there will be access to the Trending Posts window and available Categories, allowing users to easily explore related content.

Additionally, an Advertisement Window will be present, providing links to external advertisements. When a user clicks on an advertisement, a new page will open, directing them to the advertised content.

Each post container will include:

* A space for the user's image.
* The date and time of publication.
* The author's name.
* Like and dislike counters, along with a comment counter to track user engagement.
* Edit and delete options for the post, which will be visible only to the author of the post, indicated by pencil and trash icons.
At the top of the page, there will also be a search bar, enabling users to search for specific posts or keywords, enhancing content discovery and accessibility.

*Post Detail Page Desktop*<br>
![Post Detail Page Desktop](static/images/screenshots/pagepostdetaildesktop.png)

*Post Detail Page Mobile*<br>
![Post Detail Page Mobile](static/images/screenshots/pagepostdetailmobile.png)

### Update Post

When users access the update post option from the post they have published, indicated by the pencil icon, they will be brought to a dedicated window. In this section, users can view their existing post, where they can update the title and content as needed. Once they have made the necessary changes, they can republish the post, ensuring that their updates are reflected in the forum.

*Update Post Desktop*<br>
![Update Post Desktop](static/images/screenshots/pageeditpostdesktop.png)

*Update Post Mobile*<br>
![Update Post Mobile](static/images/screenshots/pageeditpostmobile.png)

### Delete Post

When users click on the trash icon associated with their published post, they will be prompted with a confirmation window. This window will ask if they are sure they want to delete the post, clearly stating that this action cannot be undone. Users will have the option to confirm the deletion, cancel the action to retain the post, or return to the home page, ensuring flexibility during the decision-making process.

*Delete Post Desktop*<br>
![Delete Post Desktop](static/images/screenshots/pagedeletepostdesktop.png)

*Delete Post Mobile*<br>
![Delete Post Mobile](static/images/screenshots/pagedeletepostmobile.png)

### Commenting Functionality

Users will have the option to comment on a post, reply to comments made by other users, and like or dislike those comments. In the comment window, users can see the name of the commenter, along with the date and time of the comment.

Each post will display 6 comments per page, with pagination activated to navigate through additional comments as needed.

*Commenting Functionality Desktop*<br>
![Commenting Functionality Desktop](static/images/screenshots/pagecommentdesktop.png)

*Commenting Functionality Mobile*<br>
![Commenting Functionality Mobile](static/images/screenshots/pagecommentsmobile.png)

### Update Comment Function

When users click the edit button for a comment, they are directed to a dedicated update window where they can modify their previous comment. This interface features an aesthetically pleasing container that enhances the user experience.

Within this container, the top section includes a bold blue title that reads "Update Comment," signaling the purpose of the page. Below the title, a subtitle prompts users with the phrase, "Edit your comment below to share your insights!" This encourages users to take their time to articulate their thoughts clearly.

In the main content area labeled "Comment Details," users can update their comment in a provided text area. Just below this input, there is a prominent "Update Comment" button styled in the same color as the navbar and footer, featuring white text to create a cohesive design.

Additionally, there is a straightforward link that states, "Need to go back? Return to Post," which appears in blue to offer users an easy way to navigate back to the previous page.

Finally, a closing motivational phrase, "Make your thoughts clear! Your voice matters!" serves to inspire users to engage thoughtfully within the forum.

*Update Comment Desktop*<br>
![Update Comment Desktop](static/images/screenshots/fileupdatecommentdesktop.png)

*Update Comment Mobile*<br>
![Update Comment Mobile](static/images/screenshots/fileupdatecommentmobile.png)

### Footer

The footer is fixed at the bottom of the page and features a design that matches the color of the navbar, providing a cohesive look throughout the website. It offers essential navigation options, including links to the Highlights page, Control Panel, Support and Collaboration, and About Me page.

These links are accessible to both logged-in and logged-out users, ensuring that everyone can explore the content. However, the Control Panel link is restricted to authorized personnel only and will open in a separate page, while the other links remain available to all users.

*Footer Page Desktop*<br>
![Footer Page Desktop](static/images/screenshots/footerdesktop.png)

*Footer Page Mobile*<br>
![Footer Page Mobile](static/images/screenshots/footermobile.png)

### Footer Message

At the bottom of the page, users will find the following message:
© 2024 Discussion Hub. All Rights Reserved.
This statement reinforces the ownership and copyright of the content on the site.

*Footer Message*<br>

![Footer Message](static/images/screenshots/footermessage.png)


## Dark Mode

The Discussion Room includes a Dark Mode feature inspired by the user-friendly design of https://en.wikipedia.org/wiki/Django_(web_framework). This mode provides an alternative color scheme to reduce eye strain in low-light environments. Users can easily switch to Dark Mode, which is beneficial for those who prefer working with a dark screen, like myself at times.

To switch back to light mode, users can find the toggle option located in the bottom left corner of the page. This flexibility allows users to choose their preferred viewing experience while engaging with the forum content.

This Dark Mode feature is currently in a testing phase. If we find that users are not satisfied with it, we will consider suspending the feature and removing it. Conversely, if users enjoy it, we will seek to refine and enhance the experience further.

* This means the page is in Dark Mode

*Dark Mode Option*<br>
![Dark Mode](static/images/screenshots/darkmode.png)

* This means the page is in Light Mode

*Dark Mode Option*<br>
![Dark Mode](static/images/screenshots/lightmode.png)

## Navbar (Dark Mode)
The navbar in Dark Mode maintains the same structure as outlined in the previous navbar section. Users will find the same essential links: Home, About Us, Login, and Register. Both the Home and About Us links are accessible to logged-in users and those who are not registered.

The navbar also features hover effects for enhanced interactivity. The title Discussion Room has a unique hover effect, while the other links present different hover styles, creating an engaging and visually appealing navigation experience even in Dark Mode.

*Dark Mode Navbar*<br>
![Dark Mode Navbar](static/images/screenshots/darkhover.png)

*Dark Mode Navbar*<br>
![Dark Mode Navbar](static/images/screenshots/darkhoverlinks.png)

* The mobile version features a navbar that appears in a dark grey color. When users click on the navbar, it expands downwards to display all navigation links. This functionality is accessible to all users, whether logged in or not, ensuring that everyone can easily navigate to key areas of the forum without hassle.

*Dark Mode Mobile*<br>
![Dark Mode Mobile](static/images/screenshots/darkmodemobilenavbar.png)

## Main Page (Home Button Dark Mode)

The main page retains the same features discussed earlier and is enhanced with pleasant colors in dark mode for improved visibility. The navbar remains consistent, ensuring a familiar navigation experience.

* The search bar is styled in white, complemented by a dark grey search button featuring white text, creating a striking contrast.
* Post containers are displayed with a dark grey background, featuring titles in black and content in white for clear readability.
* User avatar images are presented within a white circular frame, adding a clean visual touch.
* User names and other data fields are displayed in white, maintaining legibility against the dark background.

On the right side, users will find:

* Categories highlighted in blue color, allowing for easy browsing of topics.
* Trending Posts showcased in a white container with black and grey text, ensuring that users can easily engage with popular discussions.
* An Advertisement Window featuring dark grey borders with a white background, providing a clear viewing area for promotional content.

At the bottom of the page, a white line visually separates the footer from the rest of the content. The footer is fixed at the bottom of the page and has the same color as the navbar, creating a cohesive look throughout the website. It includes essential links and a toggle switch for dark/light mode, allowing users to easily switch their viewing preference.

*Main Page Dark Mode*<br>
![Main Page Dark Mode](static/images/screenshots/darkmodemainpageversion.png)

*Main Page Dark Mobile*<br>
![Main Page Dark Mobile](static/images/screenshots/darkmodehome.png)

*Categories, Trending Posts and Advertisment*<br>
![Categories, Trending Posts and Advertisment](static/images/screenshots/darkmodetranding.png)

*Footer Dark Mode*<br>
![Footer Dark Mode](static/images/screenshots/darkmodefooter.png)

## Abous Us (Dark Mode)

The About Us page retains the same features as described previously, with a dark mode aesthetic. The container is set to a dark grey background, providing a comfortable viewing experience. The title is styled in a vibrant green color, complemented by white text for the body content, creating a visually appealing contrast that enhances readability in dark mode.

*About Us Dark Mode Desktop*<br>
![About Us Dark Mode Desktop](static/images/screenshots/darkmodeaboutusdesktop.png)

*About Us Dark Mode Mobile*<br>
![About Us Dark Mode Mobile](static/images/screenshots/darkmodeaboutusmobile.png)

## Login Page (Dark Mode)

The Login Page in dark mode features a sleek design that enhances user experience. It includes input fields for username and password, both displayed in white to provide a strong contrast against the dark background, ensuring readability.

The Log In button is styled with a green border, adding a visually appealing touch. Below the login fields, users who do not have an account can find a prompt to sign up, presented in a nice blue color for emphasis.

Also, we have a "Forgot Password" button positioned prominently before the "Don't have an account? Sign up" section. This button is designed in a blue color, aligning with the dark mode theme and matching the title and links. This design choice enhances visibility and accessibility, allowing users to easily find the option for password recovery.

A clean white line visually separates the footer from the login options. The footer is fixed at the bottom of the page and features a fixed design that matches the overall color theme. In the bottom left corner, there is a toggle for switching between dark and light modes, designed in blue to align with the overall color theme.

*Dark Mode Log In Page*<br>.
![Dark Mode Log In Page](static/images/screenshots/darkmodelogindesktop.png)

*Dark Mode Log In Mobile*<br>.
![Dark Mode Log In Mobile](static/images/screenshots/darkmodeloginmobile.png)

## Register Page(Dark Mode)

The Register Page in dark mode mirrors the structure of the Login Page, ensuring a consistent user experience. All input fields are displayed in white, with their corresponding labels also in white, creating a classic input style against the black background. 

* Password Requirements are also presented in white to maintain readability.
* The "Register Now" button features a nice grey color, providing a classic combination with white lettering for a visually appealing call-to-action.
* Below the registration fields, the message for users who already have an account is displayed in white, accompanied by a Log In link styled in a nice blue color.
* Error Messaging: If users enter incorrect information in the password fields or if they attempt to register a username that is already taken, a warning message will appear below the respective input field. This feedback helps users correct their entries promptly.

At the bottom of the page, the footer is fixed and features all essential links presented in white, maintaining the same color as the navbar for consistency. A clean design ensures that the footer remains visually cohesive with the overall layout, providing users with easy navigation options while enhancing the aesthetic of the site.

*Register Page Dark Mode Desktop*<br>
![Register Page Dark Mode Desktop](static/images/screenshots/darkmoderegisterdesktop.png)

*Register Page Dark Mode Mobile*<br>
![Register Page Dark Mobile](static/images/screenshots/darkmoderegistermobile.png)

## Footer Section ( Dark Mode)

The footer in dark mode features a classic line that separates it from the main content window, providing a clean visual distinction. It includes links for Highlights, Control Panel, Support, and About Me, all styled in white for visibility and consistency. The Control Panel link, which will open in a separate page, is reserved for administrative tasks and is only available to authorized personnel who can log in.

These links are accessible across all pages for both logged-in users and those without an account. At the bottom of the footer, there is an "All rights reserved" message, ensuring clarity regarding content ownership. Additionally, the toggle for switching between dark and light modes is present; in dark mode, the toggle appears in blue, while in light mode, it is styled in grey, maintaining consistency with the overall theme.

The navbar is fixed at the bottom of the page, providing users with easy access to navigation while enhancing the overall aesthetic of the website.

*Footer In Dark Mode Desktop*<br>
![ooter In Dark Mode Desktop](static/images/screenshots/footerdarkmodedesktop.png)

*Footer In Dark Mode Mobile*<br>
![ooter In Dark Mode Mobile](static/images/screenshots/footerdarkmodemobile.png)

## About Me (Dark Mode)

The About Me page in dark mode features an elegant grey window that creates a visually appealing backdrop. The titles are displayed in a vibrant green color, while the content is presented in white letters, ensuring excellent readability. This combination of colors enhances the overall aesthetic and provides a comfortable experience for users navigating the page.

*About Me Dark Mode Desktop*<br>
![About Me Dark Mode Desktop](static/images/screenshots/darkmodeaboutmedesktop.png)

*About Me Dark Mode Mobile*<br>
![About Me Dark Mode Mobile](static/images/screenshots/darkmodeaboutmemobile.png)

## Support & Collaboration Page (Dark Mode)

The Support and Collaboration page in dark mode opens with a nice blue title that creates an inviting atmosphere. Below the title, a submessage encourages users to contact the team for messages and various inquiries related to collaboration.

Input fields for name, email, and message are displayed in white, ensuring clarity against the dark background. The Submit button features a grey background with white letters, providing an appealing call-to-action for users submitting their queries.

*Support & Collaboration Dark Mode Desktop*<br>
![Support & Collaboration Mode Desktop](static/images/screenshots/darkmodesupportdesktop.png)

*Support & Collaboration Dark Mode Mobile*<br>
![Support & Collaboration Mode Mobile](static/images/screenshots/darkmodesupportmobile.png)

## Control Panel (Dark Mode)

The Admin Control Panel is presented against a dark background, featuring striking blue titles that enhance the visibility and hierarchy of information. The overall blue color scheme conveys a professional and authoritative appearance, suitable for administrative functions.

Within the control panel, users can expect to see various icons—such as "x" for deletion, pencil icons for editing, and plus signs for adding content—styled in a vibrant green color. This choice of color not only adds visual interest but also clearly indicates actions that can be taken within the panel.

The combination of blue titles, white text, and green action icons creates a cohesive and user-friendly interface, ensuring that administrators can manage the forum efficiently and intuitively while maintaining a pleasant visual environment.

*Control Panel Dark Mode Desktop*<br>
![Control Panel Dark Mode Desktop](static/images/screenshots/darkmodecontrolpaneldesktop.png)

*Control Panel Dark Mode Mobile*<br>
![Control Panel Dark Mode Mobile](static/images/screenshots/darkmodecontrolpanelmobile.png)

## Highlights Page (Dark Mode)

The Highlights Page is presented in a nice grey window with a prominent blue title and white content. This section expresses gratitude to Code Institute for providing the resources and support to bring this project to life. 

Special thanks to the tutors and my mentor, Iuliia Konovalova, for their invaluable guidance throughout my learning journey. I also appreciate the GitHub team for their collaboration platform.

For more information about Code Institute, visit their website: https://codeinstitute.net/se/, highlighted in an engaging orange color.

*Highlights Page Dark Mode Desktop*<br>
![Highlights Page Dark Mode Desktop](static/images/screenshots/darkmodehighlightsdesktop.png)

*Highlights Page Dark Mode Mobile*<br>
![Highlights Page Dark Mode Mobile](static/images/screenshots/darkmodehighlightsmobile.png)

## User Access (Logged In)
As a logged-in user, I will present the sections that can only be accessed when you are logged into the forum. All the sections outlined previously, including the main page, are available in your logged-in session. 

* The Home button brings you back to the main page, while the About Us section and the footer links remain accessible, providing a seamless and familiar navigation experience within the forum.

## Create a New Post (Dark Mode)

In the Create a New Post section in dark mode, users will find a visually appealing dark grey container featuring a vibrant blue title accompanied by a soft white subphrase for clarity.

This section includes three input fields styled in a soft cream white, allowing for a pleasant input experience:

* Title
* Content
* Category

The Publish button stands out with a dark grey background and white text, complemented by a nice green border, ensuring it is clearly visible. Additionally, there is a Go Back button available for users who wish to cancel the post creation process.

To inspire users, two motivational phrases are included, creating a positive atmosphere for composing new posts.

<*Create a New Post Page Dark Mode Desktop*<br>
![Create a New Post Page Desktop Dark Mode](static/images/screenshots/darkmodecreatepostdesktop.png)

<*Create a New Post Page Dark Mode Mobile*<br>
![Create a New Post Page Dark Mode Mobile](static/images/screenshots/darkmodecreateapostmobil.png)

## Account Page (Dark Mode)

The Account Page in dark mode features a visually appealing layout with a soft white background. Within this container, there is another internal container, also in white, which includes a bar with a background color matching the navbar and footer. The text "Your Account Overview" is displayed in white for better visibility against the blue background.

The user’s avatar is presented in a circular format, accompanied by the username displayed in blue and the email address in grey for clear differentiation. 

Additionally, the section includes “Connect with Us” text in blue, followed by links to social media profiles. These links feature hover effects for enhanced interactivity and user engagement.

At the bottom of the page, users will find a button for Update Profile, enabling them to make changes to their account details easily.

*Account Page Dark Mode Desktop*<br>
![Account Page Dark Mode Desktop](static/images/screenshots/darkmodeaccountdesktop.png)

*Account Page Dark Mode Mobile*<br>
![Account Page Dark Mode Mobile](static/images/screenshots/darkmodeaccountmobile.png)

## Edit Profile Page (Dark Mode)

The Edit Profile Page is designed with a pleasing soft white container that features a bold blue title, clearly indicating the purpose of the page. Within this container, users will find input fields for updating their username and email, set against a grey background for easy readability.

Additionally, there is a dedicated section for changing the avatar image. This section displays the current profile photo, allowing users to easily see what the existing image is before making changes.

At the bottom of the page, there is a Save Changes button with an attractive dark grey background and white text, enabling users to apply their updates. Next to it, a simple link in blue allows users to Cancel and go back, providing an easy option to exit without saving changes.

A warning message is displayed for users considering a username change, reminding them that if they change their username, it will be updated in the system. After the change, this new username will become their primary identifier for logging in. Furthermore, users are encouraged to provide a correct email address, as this enables our team to contact them regarding any important changes or updates.

*Edit Profile Dark Mode Desktop*<br>
![Edit Profile Dark Mode Desktop](static/images/screenshots/darkmodeeditprofiledesktop.png)

*Edit Profile Dark Mode Mobile*<br>
![Edit Profile Dark Mode Mobile](static/images/screenshots/darkmodeeditprofilemobile.png)

## Notifications Page (Dark Mode - Empty)

The Notifications Page in dark mode features a sleek black background that enhances the visual appeal. At the top of the page, the title Your Notifications is displayed in white letters, clearly indicating the purpose of the section.

If there are no notifications to show, a message will appear below the title saying You have no notifications, also in white. This clear communication ensures that users are aware of their current notification status without any confusion.

*Notifications Page Empty Dark Mode Desktop*<br>
![Notifications Page Empty Dark Mode Desktop](static/images/screenshots/darkmodenotificationsdesktopempty.png)

*Notifications Page Empty Dark Mode Mobile*<br>
![Notifications Page Empty Dark Mode Mobile](static/images/screenshots/darkmodenotificationsmobilempty.png)

## Notification Page With Notification(Dark Mode)

The Notifications Page in dark mode features a clean white title at the top that reads Your Notifications. Below the title, a white container displays the detailed information about any replies to the user's comments. Each notification includes:

User Name: The name of the user who replied.
Comment Reference: A message stating "User [name] replied to your comment: [your comment content]."
Date and Time of Reply: The date and hour when the reply was made.
Additionally, users will have two options for each notification:

Delete: To remove the notification and keep the notifications page clean and organized.
Go to Comment: This option will link the user directly to the specific comment they posted, allowing for easy navigation and engagement with the discussion.
Before arriving at this page, logged-in users will notice a bell icon next to the notifications link in the navbar, indicating that there are new notifications to check.

*Notifications Page Dark Mode Desktop*<br>
![Notifications Page Dark Mode Desktop](static/images/screenshots/darkmodenotificationdesktop.png)

*Notifications Page Dark Mode Mobile*<br>
![Notifications Page Dark Mode Mobile](static/images/screenshots/darkmodenotificationmobile.png)

## Post Detail Page (Dark Mode)

The Post Detail Page in dark mode features a well-structured layout designed for optimal readability and engagement.

At the top left corner of the post container, the user’s avatar is displayed in a nice circular format with a white border. Below the avatar, the posted by information indicates the username, followed by the date and the comment counter.

The title of the post stands out in black, presented with an elegant font, while the content is displayed in white using a clean and appealing font style.

Towards the bottom left of the post container, users will find the Edit button, which has a green background with a white icon, allowing users to modify their post. Next to it, the Delete button features a red background with a white icon, signaling caution for users when removing the post.

On the bottom right side of the post container, users can interact with the Like and Dislike buttons. The Like button has a green background with a blue icon, indicating positive interaction, while the Dislike button features a red background with a blue icon for easy visibility.

The Comment Section is designed in white, providing a clear area for users to add their thoughts. Pagination in this section is presented with a white background color, grey letters for the comments, and blue for the page numbers, enabling effortless navigation through comments.

Below the comment input, the Submit button has a grey background with white text, accented with a blue border, creating an attractive call-to-action.

At the top of the page, a search bar with a soft color scheme invites users to search for posts. The search button features a grey background and displays the text "Search for posts" in grey letters, with the actual button having white letters.

Additionally, the Categories Section is integrated within the Trending Posts window on the right side. The category links are showcased in a nice blue color, making them easily accessible.

The Trending Posts window features a title in blue, displaying random posts in a white container, with titles in black and content in grey. This window is surrounded by a grey border to delineate it visually from other sections.

Lastly, an Advertisement Window is framed with a grey border, containing a white container inside. This space can be utilized for relevant advertisements, ensuring a clean and organized layout.

*Post Detail Page Dark Mode Desktop*<br>
![Post Detail Page Dark Mode Desktop](static/images/screenshots/darkmodepostdetailpagedesktop.png)

*Post Detail Page Dark Mode Mobile*<br>
![Post Detail Page Dark Mode Mobile](static/images/screenshots/darkmodepostdetailmobile.png)

## Update Post Page(Dark Mode)

The Update Post Page features a nice dark grey container with an attractive blue title. This page uses the same layout as the Create a New Post section, which is why the title is Create a New Post. 

The main difference is that the input fields for title and content are pre-filled with the existing information from the post being updated, ensuring that users can see and modify the current content directly.

The input fields are styled in a soft cream white color, with the text within them (for both title and content) displayed in black for clear readability.

At the bottom of the page, the Publish button has a dark grey background with white letters that read Publish, accented by a nice green border to make it stand out. Additionally, there is a Go Back button styled with the same dark grey background and white letters as the Publish button, but without a border, allowing users to easily cancel the update and return to the previous page.

*Update Post Page Dark Mode Desktop*<br>
![Update Post Page Dark Mode Desktop](static/images/screenshots/darkmodeeditpostdesktop.png)

*Update Post Page Dark Mode Mobile*<br>
![Update Post Page Dark Mode Mobile](static/images/screenshots/darkmodeditpostmobil.png)

## Update Comment (Dark Mode)

In dark mode, the Update Comment section features a visually appealing container with a soft grey background, providing a pleasant contrast for the user. At the top of this container, a prominent blue title reads "Update Comment," clearly indicating the purpose of the page.

Beneath the title, a white subtitle prompts users with the phrase, "Edit your comment below to share your insights!" This encourages thoughtful engagement from users.

The main content area includes a "Comment Details" section where users can update their comment in a designated input area. Just below the input, there is an "Update Comment" button styled with a dark grey background and white text, ensuring good visibility against the grey container.

Additionally, a straightforward link is displayed in white text that states, "Need to go back? Return to Post," appearing in blue to offer users an easy way to navigate back to the previous page.

At the end of the section, two motivational phrases, "Make your thoughts clear!" and "Your voice matters!" inspire users to express themselves confidently within the forum.

*Update Comment Dark Mode Desktop*<br>
![Update Comment Dark Mode Desktop](static/images/screenshots/darkmodeupdatecomment.png)

*Update Comment Dark Mode Mobile*<br>
![Update Comment Dark Mode Mobile](static/images/screenshots/darkmodeupdatecommentmobile.png)

## Delete Post Page (Dark Mode)

The Delete Post Page features a clean white container that clearly communicates the importance of the action being taken. At the top, a bold Confirm Post Deletion title is displayed in red, indicating that this is a serious action.

Below the title, a subheading reads Delete Post in black, setting the context for users. A phrase follows, asking, "Are you sure you want to delete the post titled: [Post Title]?" This emphasizes the specific post being addressed. Additionally, it informs users that "This action cannot be undone," reinforcing the gravity of the decision.

At the bottom of the container, users are presented with two choices:

A Delete button with a dark grey background, white letters, and a red border, providing a clear call-to-action for proceeding with the deletion.
A Cancel button styled similarly—dark grey background and white letters— but with blue text, allowing users to back out of the deletion process.
There’s also a section that provides the option to Return to Home Page, directing users back to the main area of the forum if they choose to navigate away.

While the Categories Links remain visible for easy navigation, the Trending Posts section will not be displayed on this page. However, the Advertisement Window will still be present, allowing users to view any ongoing promotions or relevant content.

*Delete Post Page Dark Mode Desktop*<br>
![Delete Post Page Dark Mode Desktop](static/images/screenshots/darkmodedeletepostdesktop.png)

*Delete Post Page Dark Mode Mobile*<br>
![Delete Post Page Dark Mode Mobile](static/images/screenshots/darkmodedeletepostmobil.png)

## Logout Page (Dark Mode)

When a logged-in user chooses the option to log out, they will see the following window. The Logout Section is presented in a nice white container that contrasts effectively with the black background, providing a clean and inviting appearance. At the top of the container, a bold blue title reads, "You Have Been Logged Out," clearly indicating the user’s status.

Beneath the title, a message in grey letters states, "We're sorry to see you go! Thank you for visiting our site," conveying appreciation and warmth to the user.

Within this section, there are two buttons for user navigation:

* The first button, Log In Again, features a blue background with letters in light blue, offering a clear call to action for users wishing to re-enter their accounts.
* The second button, Return to Home, has a dark grey background with letters in light blue, allowing users to easily navigate back to the main page of the forum.

*Logout Page Dark Mode Desktop*<br>
![Logout Page Dark Mode Desktop](static/images/screenshots/darkmodelogoutpagedesktop.png)

*Logout Page Dark Mode Mobile*<br>
![Logout Page Dark Mode Mobile](static/images/screenshots/darkmodelogoutmobile.png)

## Reset Password Option (Forgot Password)

Also, I decided to create a section for resetting the password that explains everything in detail, including pictures for both light and dark mode within the same section. When we click on the "Forgot Password" button, we will be directed to a page where we need to enter the email address we used when we registered for the forum. After submitting your email, you will see a message prompting you to check your inbox or spam folder. This email will contain instructions on how to reset your password.

*Reset Password Light Mode Desktop*<br>
![*Reset Password Light Mode Desktop](static/images/screenshots/resetpassworddesktop.png)

*Reset Password Light Mode Mobile*<br>
![*Reset Password Light Mode Mobile](static/images/screenshots/resetpasswordmobile.png)

*Reset Password Dark Mode Desktop*<br>
![*Reset Password Dark Mode Desktop](static/images/screenshots/resetpassworddarkmodedekstop.png)

*Reset Password Dark Mode Mobile*<br>
![*Reset Password Dark Mode Mobile](static/images/screenshots/resetpassworddarkmodemobile.png)

*Password Request Confirmation Desktop*<br>
![Password Request Confirmation Desktop](static/images/screenshots/passwordresetdesktopsent.png)

*Password Request Confirmation Mobile*<br>
![Password Request Confirmation Mobile](static/images/screenshots/resetpasswordmobile.png)

*Password Request Confirmation Dark Mode Desktop*<br>
![Password Request Confirmation Dark Mode Desktop](static/images/screenshots/passwordresetsentdarkmodedesktop.png)

*Password Request Confirmation Dark Mode Mobile*<br>
![Password Request Confirmation Dark Mode Mobile](static/images/screenshots/resetpassworddarkmodemobile.png)

Once we receive the message, we will see a text saying, "You're receiving this email because you requested a password reset for your user account at discussion-room-828675a77e1b.herokuapp.com." Following that, there will be a prompt: "Please go to the following page and choose a new password." Additionally, the email will remind us of the username we registered with, in case we forgot it.

*Email*<br>
![Email](static/images/screenshots/email.png)

Once we click the link in the email, we will be redirected to a page where we can enter our new password and confirm it by entering it again in the "Confirm Password" field. After filling in both fields, we simply need to click the "Update Password" button to finalize the process.

Additionally, we will have a list of password requirements displayed on the page. It is important that users carefully read these instructions to ensure that their new password meets the necessary criteria. This will help maintain account security and prevent any issues during the password update process.

*Change Password Window Light Mode*<br>
![Change Password Window Light Mode](static/images/screenshots/enternewpassdesktop.png)

*Change Password Window Light Mode Mobile*<br>
![Change Password Window Light Mode Mobile](static/images/screenshots/enternewpassmobilelightmode.png)

*Change Password Window Dark Mode*<br>
![Change Password Window Dark Mode](static/images/screenshots/enternewpassworddarkmodedesktop.png)

*Change Password Window Dark Mode Mobile*<br>
![Change Password Window Dark Mode Mobile](static/images/screenshots/enternewpassmobile.png)

Once we click the "Update Password" button, our request will be processed, and the password will be updated. We will see the following phrase: "Your password has been set. You may go ahead and log in now."
There will also be a "Log In" button that will redirect us to the login page, allowing us to access our account with the newly set password.

*New Passowrd Confirmation*<br>
![New Password Confirmation](static/images/screenshots/passconfirmationdesktop.png)

*New Passowrd Confirmation Mobile*<br>
![New Password Confirmation Mobile](static/images/screenshots/passconfirmationmobile.png)

*New Passowrd Confirmation Dark Mode*<br>
![New Password Confirmation Dark Mode](static/images/screenshots/passconfirmationdarkmodedesktop.png)

*New Passowrd Confirmation Dark Mode Mobile*<br>
![New Password Confirmation Dark Mode Mobile](static/images/screenshots/passconfirmationdarkmodemobile.png)

Once we use the link to change our password, it will no longer be valid, and we will need to request a new password reset email if we need to change our password again.

*Not Valid Link*<br>
![Not Valid Link](static/images/screenshots/notvalidlinklightmode.png)

*Not Valid Link Mobile*<br>
![Not Valid Link Mobile](static/images/screenshots/notvalidlinkmobilelightmode.png)

*Not Valid Link Dark Mode*<br>
![Not Valid Link Dark Mode](static/images/screenshots/notvalidlinkdarkmode.png)

*Not Valid Link Dark Mode Mobile*<br>
![Not Valid Link Dark Mode Mobile](static/images/screenshots/notvalidlinkmobiledarkmode.png)

* Note : 
The screenshots for "New Password Confirmation" and the "Not Valid Link" sections were taken using the Safari tools option. I encountered an issue with my Google Dev Tools, which prevented me from using the responsive option as it was consistently blocking access. Therefore, I decided to use Safari tools to capture the screenshots for both desktop and mobile versions.

## Small Details (Features)

In this section, I will explain the small details and features that I have added to the Discussion Room project. Most of these aspects were touched upon in the features section and can be seen in the accompanying images, showcasing both light and dark mode.

Here, I will provide a deeper insight into these features, including the thoughtful design choices and functionalities that enhance the user experience. From responsive elements to interactive components, these small details contribute significantly to the overall functionality and aesthetic of the forum.

## User Action Messages

In the Discussion Room, users receive informative messages based on their actions to enhance their experience and provide feedback. Here are the messages users can expect:

* Post Creation: When a user creates a post, a message will appear stating, "Your post has been created successfully."

* Viewing a Category: If a user visits a specific category, they will see a message indicating, "You are viewing posts in the category: [Category Name]."

* Post Update: Upon updating a post, the message "Your post has been updated successfully." will be displayed to confirm the action.

* Comment Addition: When a user adds a comment, they will see the message "Your comment has been added."

These messages will appear for 10 seconds before automatically disappearing, ensuring users are informed of their actions without cluttering the interface.

*User Action Messages*<br>
![User Action Messages](static/images/screenshots/messagecars.png)

*User Action Messages*<br>
![User Action Messages](static/images/screenshots/messagecinema.png)

*User Action Messages*<br>
![User Action Messages](static/images/screenshots/messagecomment.png)

*User Action Messages*<br>
![User Action Messages](static/images/screenshots/messagepostcreated.png)

*User Action Messages*<br>
![User Action Messages](static/images/screenshots/messagerandompost.png)

*User Action Messages*<br>
![User Action Messages](static/images/screenshots/messagesport.png)

*User Action Messages*<br>
![User Action Messages](static/images/screenshots/messageupdatedpost.png)

## Trending Posts

The Trending Posts window, previously mentioned in the features section, displays 5 random posts from all the posts in the forum. If there are a total of 200 posts available, every time the user visits or refreshes the page, a new set of 5 random posts will be shown, ensuring fresh content is always highlighted.

This trending window is prominently displayed on the main page, making it easy for users to discover engaging discussions. It also appears while users are reading a post, providing continued access to trending content. However, when visiting other pages of the site, the trending window will be visible but will not display any posts, maintaining a clean layout without redundancy.

*Trending Posts Window*<br>
![Trending Posts Window](static/images/screenshots/trendingpostswindow.png)

## Categories

The Categories feature, previously mentioned in the features section, allows users to explore 4 distinct categories: Cinema, Cars, Sport, and Random Content. Each category offers a specific theme for users to write about.

All posts will be displayed on the main page, but users can easily navigate to their favorite category by clicking on the corresponding link. For instance, clicking on the Sport category will present all posts associated with that topic, allowing for focused browsing.

Currently, the forum features these 4 categories; however, we will monitor user feedback and reactions to determine if there is interest in adding new categories in the future. User suggestions for improving the category section are welcomed, as we strive to enhance the overall user experience.

*Categories*<br>
![Categories](static/images/screenshots/sectioncategory.png)

*Categories Dark Mode*<br>
![Categories Dark Mode](static/images/screenshots/categoriesdarkmode.png)

## Advertisement Window

The Advertisement Window has been implemented as a feature for future advertising opportunities. This section will allow us to display relevant ads based on user interest and forum content. If we receive positive feedback regarding the forum's performance, we can utilize the advertisement window to showcase additional advertisements.

When users click on the advertisement window, it will open a new separate window, directing them to the advertised content. We will actively monitor user feedback about this section to assess its effectiveness and make improvements as necessary.

*Advertisement Section*<br>
![Advertisement Section](static/images/screenshots/sectionadvertisement.png)

## Pagination

The Discussion Room implements pagination for both posts and comments to enhance user experience.

* Posts Pagination: A maximum of 8 posts will be displayed per page. This setup allows users to browse through content effectively without being overwhelmed by too much information at once.

* Comments Pagination: The comment section will feature 6 comments per page. Replies to comments will not count in this pagination, ensuring that the main comments remain easily accessible and organized for users.

This pagination design not only improves performance by reducing load times but also helps maintain a clean and user-friendly interface.

*Pagination*<br>
![Pagination](static/images/screenshots/sectionpagination.png)

## Comment Section

Users can add comments to posts, fostering engagement and discussion within the forum. Each comment allows others to reply directly, creating a threaded conversation that enhances interactivity among users.

Additionally, users have the ability to like or dislike comments, providing a simple way to express their opinions on the contributions of others. This feature encourages constructive feedback and enhances the overall community experience by allowing members to support each other's insights or share differing viewpoints.

Overall, the commenting functionality adds a dynamic layer to the forum, promoting active participation and community building.

*Comment Section*<br>
![Comment Section](static/images/screenshots/sectioncommentslightmode.png)

*Comment Section Dark Mode*<br>
![Comment Section Dark Mode](static/images/screenshots/sectioncommentsdarkmode.png)

## Edit and Delete Post Buttons

The Edit Post functionality is represented by a pencil icon, which is styled in green to signify the action of updating content positively. This color choice reflects the constructive nature of editing, allowing users to enhance their posts with ease.

Conversely, the Delete Post action is represented by a trash icon, styled in red. This color indicates caution and represents a significant action, as deleting a post is a serious decision that removes content permanently.

Both icons are easily accessible in the post interface, allowing users to manage their content efficiently while maintaining clear visual cues about the actions they represent.

*Edit and Delete Post Buttons*<br>
![Edit and Delete Post Buttons](static/images/screenshots/sectioneditlightmode.png)

*Edit and Delete Post Buttons Dark Mode*<br>
![Edit and Delete Post Buttons Dark Mode](static/images/screenshots/sectioneditdarkmode.png)

## Like and Dislike Functionality

Users have the option to like and dislike both posts and comments, fostering interaction and feedback within the community. Each post and comment features a counter next to the respective icons, displaying the number of likes and dislikes received.

* Like Icon: Represented by a thumbs-up symbol in green, this icon signifies a positive action, allowing users to express appreciation for valuable content.

* Dislike Icon: Represented by a thumbs-down symbol in red, this icon indicates a negative action, allowing users to signal discontent or disagreement with the content.

These visual indicators and their accompanying counters enhance the user experience by providing immediate feedback on the community's response to posts and comments, encouraging thoughtful participation in discussions.

*Like and Dislike Functionality*<br>
![Like and Dislike Functionality](static/images/screenshots/sectionlikedislikelightmode.png)

*Like and Dislike Functionality Dark Mode*<br>
![Like and Dislike Functionality Dark Mode](static/images/screenshots/sectionlikedislikedarkmode.png)

## Search Bar Functionality
At the top of the main page, there is a search bar that allows users to search for posts easily. Users can enter random keywords or specific titles, and the search functionality will return posts that contain the searched words or titles, making it simple to find relevant content.

This search bar is not only present on the main page but also accessible when users are reading a post, ensuring that they can continue exploring the forum without interruption. This feature enhances content discoverability and allows users to engage with topics that interest them swiftly.

*Search Bar Functionality*<br>
![Search Bar Functionality](static/images/screenshots/sectionsearchpostslightmode.png)

*Search Bar Dark Mode*<br>
![Search Bar Dark Mode](static/images/screenshots/sectionsearchpostsdarkmode.png)

## Social Account Links
On the Account Page, users will find links to their social media accounts, including Facebook, Twitter, LinkedIn, and Dribbble. These links are conveniently positioned to encourage users to connect and engage with their networks.

By clicking on any of these links, users can easily navigate to their respective social media profiles, fostering interaction and sharing within the community. This integration allows users to showcase their contributions and connect with others, enhancing the overall experience of the Discussion Room.

Whether users wish to share posts, collaborate on projects, or simply stay updated, these social media links provide a useful avenue for expanding their online presence beyond the forum.

*Social Account Links*<br>
![Social Account Links](static/images/screenshots/sectionsociallinks.png)

## Post Detail Bar
At the top of the container where each post is displayed, the Post Detail Bar provides essential information about the post. This bar includes:

* User Name: Clearly indicating who authored the post, allowing readers to see the contributor's identity.
* Date and Time: Displaying when the post was published, providing context for its relevance.
* Comment Counter: Showing how many comments the post has received, encouraging user interaction and engagement.
* Like and Dislike Counters: Displaying the number of likes and dislikes the post has garnered, which helps attract attention to the content.

This Post Detail Bar is prominently visible on the main page, where all posts are displayed, and is also present when a user is reading an individual post (without showing like and dislike counts). By providing this key information upfront, users can quickly gauge the popularity and engagement of a post, enhancing their browsing experience.

*Post Detail Bar*<br>
![Post Detail Bar](static/images/screenshots/sectionpostdetailsbar.png)

## Default Image For New Users

When new users register on the forum, they are automatically assigned a default avatar image. This ensures that every user has a profile picture upon joining, creating a more visually engaging community.

For those who wish to customize their presence further, users can upload a personal avatar. To do this, they need to navigate to their account settings and select the "Update Account" option. From there, users can easily upload a new image from their computer to replace the default avatar.

This feature allows users to personalize their profiles, enhancing their overall experience on the forum.

*Default Image For New Users*<br>
![Default Image For New Users](static/images/screenshots/newusersimage.jpeg)

## Manual Testing Table

| Element Tested               | Element Description                           | Testing Completed                                           | Expected Outcome                                                                  | Result       |
|------------------------------|----------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------|--------------|
| Navigation Links             | Links to various sections of the forum      | Clicked all available navigation links                    | All links should navigate to the correct sections of the forum                    | As expected. |
| User Registration            | User sign-up       | Registered a new account                                                           | Users should be able to create an account and access their profile securely       | As expected. |
| Logout Functionality         | Log out feature for users                   | Clicked the logout button                                 | User should be logged out and redirected to the appropriate page                  | As expected. |
| Post Creation                | Ability to create new posts                  | Created a new post through the post creation form        | The post should be saved and displayed on the main page                           | As expected. |
| Post Editing                 | Ability to edit existing posts               | Edited a previously created post                           | Changes should be reflected on the post detail page                               | As expected. |
| Post Deletion                | Ability to delete posts                      | Deleted a post from the admin dashboard                   | The post should be removed from the database and no longer displayed              | As expected. |
| Comment Functionality        | Adding comments to posts                     | Added comments to a post                                 | Comments should appear under the respective post                                  | As expected. |
| Like/Dislike Feature         | Users can like or dislike posts/comments      | Clicked like and dislike buttons on posts and comments    | Like/dislike counters should update correctly                                      | As expected. |
| Trending Posts Window        | Display of random posts in trending section  | Observed the trending posts section                       | Trending posts should refresh and display new random posts each time             | As expected. |
| Search Functionality         | Ability to search for posts                  | Used the search bar to find posts                         | Results should display posts matching the search criteria                         | As expected. |
| User Notification            | Notifications for replies to comments        | Received notifications and accessed them                  | Notifications should properly inform users of activity on their comments          | As expected. |
| Categories Navigation        | Links to categories for filtering posts      | Clicked on category links                                  | Redirect to posts associated with the selected category                          | As expected. |
| Footer Links                 | Links in the footer for additional resources  | Clicked all footer links                                   | Footer links should open the corresponding social media pages in new tabs         | As expected. |
| User Login                   | User login capabilities                      | Successfully logged into the user account                    | Users should be able to securely log into their existing accounts without issues.   | As expected. |
| Update Existing Comment      | Capability for users to update their existing comments | Successfully updated the comment                   | Users should be able to modify their comments easily and securely. | As expected. |
| Reply to Existing Comment |  Capability for users to reply to existing comments | Successfully submitted a reply to the comment            | Users should be able to respond to comments effortlessly, enhancing engagement and discussion. | As expected. |
| Delete Existing Reply Comment | Capability for users to delete their replies to comments | Successfully removed the reply comment          | Users should be able to delete their replies without any issues, ensuring control over their contributions. |  As expected. |
| Delete Existing Comment | Capability for users to delete their comments | Successfully removed the comment                                 | Users should be able to delete their comments seamlessly, ensuring they have control over their posted content. | As expected. |
| Social Links on Account Page | Social media links allowing users to connect with various platforms | Successfully opened links in separate pages for each social media account | Users should be able to click on the social links to navigate to the respective social media platforms seamlessly. | As expected. |
| Dark Mode                    | Enable dark mode for a more comfortable viewing experience in low-light environments | Successfully switched to dark mode, altering background and text colors appropriately | Users should be able to toggle dark mode on and off, ensuring readability and reducing eye strain. | As expected. |
| Pagination Functionality     | Capability to navigate through multiple pages of content | Successfully navigated between pages of posts or comments | Users should be able to use pagination controls to efficiently browse through content without issues. | As expected. |
| Advertisement Window         | Display of advertisements that link to external resources or partners | Successfully redirected users to a separate page when clicking on the advertisement link | Users should be able to click on the advertisement to navigate to the specified external page without issues. | As expected. |
| Button and Link Testing | Verification of functionality for all buttons and links across the application, including "Return Home" | Successfully tested each button and link, confirming proper navigation and functionality | All buttons and links should direct users to their respective pages and perform their defined actions correctly without any errors. | As expected. |
| Reset Password Functionality | Verification of the password reset process, including email sending, password entry, and confirmation. | Successfully tested the entire password reset flow, ensuring users can request a password reset, set a new password, and confirm completion. | All steps in the password reset process work as intended, directing users through email verification, new password entry, and completion stages without errors. | As expected. |
| Categories Functionality | Created a post and assigned it to a specified category. | Successfully tested the process of creating a new post and assigning it to an existing category. | The post is correctly assigned to the chosen category and is displayed accordingly on the site. | As expected. |

- Note
All buttons, links, pages, and features implemented have been tested manually, and everything worked as expected. However, as I always say, something can always happen. If any issues arise, we kindly ask our users to communicate with us quickly through our support page so that we can address and fix the issue promptly. Additionally, the page will be continuously monitored to prevent any potential problems.

## Potential Features to Add

As I reflect on the project, I see numerous opportunities for enhancement and expansion. Some of the features I'd like to introduce include:

1. More Categories: Expanding the categories available for discussions would allow users to navigate topics more easily and engage in a wider range of conversations.

2. Chat Room Functionality: Implementing a chat room feature would provide a real-time communication space for users, fostering more dynamic interactions and enhancing community engagement.

3. Private Messaging: Adding an option for users to send private messages to one another would facilitate personal communication and help build connections within the community.

4. User Feedback Integration: Like any successful application, the growth and evolution of this project will greatly depend on user feedback and preferences. I plan to incorporate surveys and polls to understand what users like, what features they prefer, and how I can improve their experience.

Overall, I believe that every application should evolve over time, adapting to the needs and desires of its users. I'm excited about the potential to enhance this project based on the input I receive from the community!

### Validator Testing

To validate all python code used in this project, each file was evaluated using the [CI Python Linter](https://pep8ci.herokuapp.com/).

User Files

*Users/Views.py*<br>
![Users/Views.py](static/images/screenshots/usersviewspy.png)

*Users/Models.py*<br>
![Users/Models.py](static/images/screenshots/usersmodelspy.png)

*Users/Forms.py*<br>
![Users/Forms.py](static/images/screenshots/usersformspy.png)

*Users/Signals.py*<br>
![Users/Signals.py](static/images/screenshots/userssignalspyfile.png)

*Users/Urls.py*<br>
![Users/Urls.py](static/images/screenshots/usersurlspyfile.png)

*Users/Admin.py*<br>
![Users/Admin.py](static/images/screenshots/usersadminpyfile.png)

*Users/Apps.py*<br>
![Users/Apps.py](static/images/screenshots/usersappspyfile.png)

Blog Files

*Blog/View.py*<br>
![Blog/Views.py](static/images/screenshots/blogviews.png)

*Blog/Models.py*<br>
![Blog/Models.py](static/images/screenshots/blogmodelspy.png)

*Blog/Forms.py*<br>
![Blog/Forms.py](static/images/screenshots/blogformspy.png)

*Blog/Apps.py*<br>
![Blog/Apps.py](static/images/screenshots/blogappspyfile.png)

*Blog/Urls.py*<br>
![Blog/Urls.py](static/images/screenshots/blogurlspyfile.png)

*Blog/Admin.py*<br>
![Blog/Admin.py](static/images/screenshots/blogadminpyfile.png)

Discussion Blog

*Discussion Blog/Urls.py*<br>
![Discussion Blog/Urls.py](static/images/screenshots/discussionblogurlspyfile.png)

*Settings.py File*<br>
![Settings.py File](static/images/screenshots/settingspyfile.png)

Note on AUTH_PASSWORD_VALIDATORS:

- You may notice that the Python linter raises warnings regarding the AUTH_PASSWORD_VALIDATORS list, indicating that the lines are long. However, these lines are generated by Django and are essential for enforcing secure password policies. 

You can safely leave these validators as-is in your settings file, as they are a standard part of Django's security features and do not pose any issues.

## CSS Validator

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate the CSS in this project. The validator returned no errors.

In this project, I took a different approach to writing my CSS code. First, I separated the dark mode styles from the light mode styles to enhance clarity. At the beginning of the dark mode section, I included a comment that clearly indicates where the dark mode CSS starts, making it easy to navigate between the two modes.

Additionally, in my past projects, I used comments to separate various parts of the project, such as using a comment for the navbar with all related styles grouped below it. This time, however, I took it a step further by adding comments for each class in the CSS file. These comments specify exactly which element each class targets and often include where to find that element in the HTML markup.

This method greatly helped me quickly identify the CSS rules I was looking for, as I could immediately see what each class was targeting. Having comments for every class made my workflow smoother and more efficient, allowing me to focus on making the necessary adjustments with confidence.

Overall, I found this organized approach to be very effective in managing my CSS code.

*CSS Validation*<br>
![CSS Validation](static/images/screenshots/cssfilevalidation.png)

## HTML Validation Issues and Resolutions

*HTML Validation Issues and Resolutions*<br>
![HTML Validation Issues and Resolutions](static/images/screenshots/sectionissuesfile.png)

1. Duplicate IDs
Issue:
The validation revealed duplicate IDs within the HTML. Specifically, the IDs auth-links and latest-gist were used multiple times. When I was adding the auth-links, I was so focused on what I could add more to the project that I completely forgot that IDs must be unique.

Explanation:
In HTML, IDs must be unique within a page. Using the same ID for different elements can lead to unexpected behavior and validation errors.

Certainly! Here’s the revised text with your added context regarding the auth-links IDs:

HTML Validation Issues and Resolutions
During the HTML validation process, several common issues were identified related to the use of IDs, attributes, and structural elements. Below is a breakdown of each issue along with explanations and suggested fixes.

2. Unnecessary Role Attribute
Issue:
A warning was detected regarding the role attribute being unnecessary for the <main> element.

Explanation:
The <main> element inherently represents the main content of a document, making the role="main" attribute redundant.

3. Bad Value for href Attribute
Issue:
An error was found related to a bad value in the href attribute for an <a> element. Specifically, the URL contained spaces, which are illegal characters. This error occurred because I wrote category=random post. I left the space because I am using the exact name filter, meaning that the name must match what I have written, such as category, and my category is specifically random post. Therefore, I could not simply add a dash or underscore.

Explanation:
Spaces in URLs can disrupt their structure.

Summary of Changes Needed
* Ensure all IDs are unique throughout the HTML document.
* Remove the role attribute from the <main> element.
* Fix URLs in href attributes by encoding spaces appropriately.

*All Issues Fixed*<br>
![All Issues Fixed](static/images/screenshots/sectionhtmlfile.png)

- Rest of the HTML Files

*About Us Validator*<br>
![About Us Validator](static/images/screenshots/aboutusvalidator.png)

*About Me Validator*<br>
![About Me Validator](static/images/screenshots/aboutmevalidator.png)

*Support Page Validator*<br>
![Support Page Validator](static/images/screenshots/supportvalidator.png)

*Highlights Validator*<br>
![Highlights Validator](static/images/screenshots/highlightsvalidator.png)

*Logout Validator*<br>
![Logout Validator](static/images/screenshots/logoutvalidator.png)

*Post Delete Validator*<br>
![Post Delete Validator](static/images/screenshots/postdeletevalidator.png)

*Create New Post Validator*<br>
![Create New Post Validator](static/images/screenshots/createnewpostvalidator.png)

*Account Page Validator*<br>
![Account Page Validator](static/images/screenshots/accountvalidator.png)

*Account Update Page Validator*<br>
![Account Update Page Validator](static/images/screenshots/accountupdatevalidator.png)

*Notification Page Validator*<br>
![Notification Page Validator](static/images/screenshots/notificationvalidator.png)

*Post Update Page Validator*<br>
![Post Update Page Validator](static/images/screenshots/postupdatevalidator.png)

*Comment Update Validator*<br>
![Comment Update Validator](static/images/screenshots/commentupdatevalidator.png)

*Post Detail View Validator*<br>
![Post Detail View Validator](static/images/screenshots/postdetailviewvalidator.png)

*Login Page Validator*<br>
![Login Page Validator](static/images/screenshots/loginvalidator.png)

*Password Reset Sent Validator*<br>
![Password Reset Sent Validato](static/images/screenshots/passwordresetsentvalidator.png)

*Set New Password Validator*<br>
![Set New Password Validator](static/images/screenshots/setnewpasswordvalidator.png)

*Password Complete Validator*<br>
![Password Complete Validator](static/images/screenshots/passwordcompletevalidator.png)

*Password Reset Page Validator*<br>
![Password Reset Page Validator](static/images/screenshots/passwordresetvalidator.png)

## JavaScript Testing

- The JavaScript code has been validated using [JSHint](https://jshint.com/ "JSHint") and produced the following results.

- The theme-toggle.js file was originally created with the primary purpose of managing the dark mode style for the website. Initially, there were no plans to include additional functionalities within this file. However, to ensure that the project worked properly, I utilized the file to accommodate some small additional functionalities. I decided to retain the original name to reflect its initial purpose, even though it now encompasses a broader range of operations. 

Importantly, these changes do not affect or create any issues with the existing code. The file remains well-structured, maintaining clarity and functionality. The integration of the additional functionalities has been executed in a way that improves the overall user experience without compromising the original purpose of the file.

* Theme-toggle.js*<br>
![JSHint result](static/images/screenshots/jstestfile.png)

- JSHint Warnings and Code Metrics Explained

When you run JSHint on this project, you might see warnings about ES6 features. Don't worry – these aren't errors in your code. They just show that we're using modern JavaScript.

These warnings mention things like 'const', 'let', arrow functions (=>), and the spread operator (...). All of these are part of ES6, which is a newer version of JavaScript.

JSHint is telling us that we're using these new features. If you're building for modern browsers or recent versions of Node.js, you can ignore these warnings. Your code will work fine.

Important Note: Despite these warnings, the code is functioning correctly and as intended. There's no need for intervention or changes based on these JSHint warnings alone. The code is working well in its current state.

## LightHouse Test

- In this section, I will paste the images for the Lighthouse test outcomes. These tests were conducted on both desktop and mobile versions of the application, as well as in both light and dark modes. The images will provide insights into the performance, accessibility, best practices, and SEO scores of the application, highlighting areas of strength and opportunities for improvement.

* We can see from the Lighthouse test results in light mode that the performance score for desktop is 94, while for mobile it is 96. The best practices score is 100, and the SEO score is 91. The accessibility score stands at 85 for both platforms, which is a manageable level that does not significantly hinder the user experience. Overall, the project is performing well, and given that the submission deadline is approaching, these scores will remain as they are for now since they do not impede the functionality of the page.

*Lighthouse Test Desktop Light Mode*<br>
![Lighthouse Test Desktop Light Mode](static/images/screenshots/lighthousedesktoplightmode.png)

*Lighthouse Test Mobile Light Mode*<br>
![Lighthouse Test Mobile Light Mode](static/images/screenshots/lighthousemobiletest.png)

* In the Lighthouse test results for dark mode, we see that the performance score for desktop is 92, while mobile achieves an impressive 98. The accessibility score for both platforms is 90, with best practices scoring a perfect 100. Additionally, the SEO score stands at 91 for both desktop and mobile. 

These scores suggest that the application is functioning exceptionally well across different modes and devices. Given that our submission deadline is fast approaching, we feel confident in maintaining these current configurations, as they do not interfere with the usability and performance of the application.

*Lighthouse Test Desktop Dark Mode*<br>
![Lighthouse Test Desktop Dark Mode](static/images/screenshots/darkmodelighthousetestdesktop.png)

*Lighthouse Test Mobile Dark Mode*<br>
![Lighthouse Test Mobile Dark Mode](static/images/screenshots/darkmodemobilelighthousetest.png)

## BUGS that I Faced

- During the development of the trending posts feature, I encountered an issue with the responsiveness of the trending posts container. Initially, the container was displayed as intended, but when I checked its responsiveness across different screen sizes, I noticed that it was overflowing in some cases, causing layout problems and negatively impacting the user experience.

*Trending Posts Container Overflowing*<br>
![Trending Posts Container Overflowing](static/images/screenshots/trendingpostsoverflowing.png)

- To address this issue, I implemented the following CSS adjustments:

*Solution*<br>
![Solution](static/images/screenshots/overflowingsolution.png)

- Navbar BUGS 

In the initial stages of development, the navbar functioned as expected; however, I later discovered that it did not respond properly to some responsive screen sizes. During my testing, I noticed that the notification link and the bell icon (used to indicate new notifications) were missing on certain screen sizes. 

The issue was caused by the placement of the welcome user message, which was displayed next to the "Discussion Room" title. This placement was taking up too much space in the navbar. Given the time constraints and limited opportunity to implement a completely new navbar design or functionality, I decided to move the welcome message below the "Discussion Room" title. 

While this adjustment was not part of the original project plan, it effectively resolved the issue and improved the responsiveness of the navbar without requiring significant redesign.

I apologize for the line on the screen; I just wanted to clearly illustrate where the issue is exactly.

*Navbar Desktop Issue*<br>
![Navbar Desktop Issue](static/images/screenshots/navbardesktopissue.png)

*Navbar Mobile Issue*<br>
![Navbar Desktop Issue](static/images/screenshots/navbarmobileissue.png)

* BUGS Fixed

As we can see in the following images, the navbar has been fixed for small, medium, and large screens. I specifically added the navbar-expand-lg class to enhance its responsiveness for larger devices. Additionally, I implemented media query code to slightly push the main content down, ensuring that the user welcome message appears below the title. With this adjustment, the navbar is slightly taller, and the main content no longer sticks to the navbar.

*Navbar Fixed Desktop*<br>
![Navbar Fixed Desktop](static/images/screenshots/navbarfixeddesktop.png)

*Navbar Fixed Mobile*<br>
![Navbar Fixed Mobile](static/images/screenshots/navbarfixedmobile.png)

* Note on Create Post Page:

*Google DevTools*<br>
![Google DevTools](static/images/screenshots/devtoolscreatepost.png)

*Different Browser*<br>
![Different Browser](static/images/screenshots/createpostanotherbrowser.png)

* During my final checks before submission, I noticed an issue while testing the create post page in mobile mode using Google DevTools. The category dropdown appeared at the top of the page in that specific testing environment. However, when I tested the same functionality in another browser, such as Safari, it worked as expected.

* Additionally, I tested the create post page on several personal devices, and it functioned correctly across those platforms as well. This suggests that the behavior might be related to the specific browser or the Google DevTools settings being used.

* Since everything works well in other environments, we will leave it as is for now. If any complaints arise regarding this issue, the team will investigate to determine if there is a real problem within the project.

## Technologies Used

In this section, I will present the technologies used in the project

## Languages

* [HTML](https://en.wikipedia.org/wiki/HTML "HTML")
* [CSS](https://en.wikipedia.org/wiki/CSS "CSS")
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JavaScript")
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")

## Libraries & Framework

* [Django](https://en.wikipedia.org/wiki/Django_(web_framework) "Django")
* [Bootstrap](https://getbootstrap.com/ "Bootstrap")
* [Google Fonts](https://fonts.google.com "Google Fonts")

## Databases
 * [PostgreSQL](https://www.postgresql.org/ "PostgreSQL")
 * [ElephantSQL](https://www.elephantsql.com/ "ElephantSQL")

## Tools

* [GitHub](https://github.com "GitHub")
* [Gitpod](https://gitpod.io "Gitpod")
* [Balsamic](https://balsamiq.com "Balsamic")
* [Coolors](http://coolors.co "Coolors")
* [DevTools](https://developer.chrome.com/docs/devtools "DevTools")
* [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn "Gitpod")
* [Cloudinary](https://cloudinary.com/ "Cloudinary")
* [Heroku](https://heroku.com "Heroku")
* [Psycopg](https://wiki.postgresql.org/wiki/Psycopg "Psycopg")
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Crispy Forms")

## Development and Deployment

## Development

#### Cloudinary

1. Navigate to [Cloudinary](https://cloudinary.com/ "Cloudinary") and create an account.
2. Log in.
3. Navigate to your dashboard and copy the API Enviroment variable.
4. Keep a note of this variable as you will need to add it to your env.py file in your project.

#### env File

You need to create an env.py file in the root folder of your repository. This is where you assign hidden variables for security reasons. This file must be added to your list of ignored files in git.ignore to ensure it does not get pushed up to your repository on GitHub as it would then be publicly accessible.

*env.py*<br>
![env.py](static/images/screenshots/sectionenvpy.png)

*Dynamic DEBUG Setup*<br>
![Dynamic DEBUG Setup](static/images/screenshots/debugdynamicsectup.png)

In my env.py file, I have set a variable named DEVELOPMENT to "1". This indicates that the application is currently running in a development environment.

When DEVELOPMENT is set to "1", the application allows for detailed error messages and debugging information to be displayed in the browser. This is essential during development, as it aids in troubleshooting and testing by providing immediate feedback about any issues encountered.

However, it's crucial to note that in a production environment, DEVELOPMENT should not be set, or it should be set to a value that represents deployment, such as "0". This ensures that detailed debugging information is suppressed, thereby preventing any sensitive information from being exposed to users and improving the overall security of the application.

By managing the DEVELOPMENT variable in this way, I ensure a smooth transition between development and production environments while maintaining security and functionality in both contexts.

1. DATABASE_URL
Description: 

This string typically represents the connection details for your database. It generally includes the database type, user credentials, host, and database name in a format like:

Where to Get It:
PostgreSQL: If you're using a PostgreSQL service (like ElephantSQL, Heroku, or Neon), you can usually find the DATABASE_URL in the dashboard of your database service provider. After creating your database, they typically display a connection string.
Locally: When developing locally, you can define this connection string based on your local PostgreSQL setup.

2. CLOUDINARY_URL
Description:

This URL allows you to connect to your Cloudinary account to manage media uploads and transformations. It includes your Cloudinary cloud name, API key, and API secret.
Where to Get It:

Cloudinary: You can obtain your CLOUDINARY_URL by signing up on Cloudinary's website and navigating to the Dashboard. In the Dashboard, you’ll find your cloud name and API credentials. Cloudinary provides a default URL format, which you can adapt by substituting your account credentials into the URL as needed.

3. SECRET_KEY
Description:

The SECRET_KEY is a string that Django uses for cryptographic signing. It’s crucial for various security features in Django (like session cookies, password resets, etc.).
Where to Get It:

For development purposes, you can generate a new secret key manually or use Django's built-in method for generating a secret key.

In production, never hard-code your secret key in your source code. Instead, use an environment variable to manage sensitive data securely. You can generate a secure key using online tools such as Django Secret Key Generator or by using Django's method mentioned above.

#### Requirements

The requirements for this particular project are as follows:<br>

asgiref==3.8.1
cloudinary==1.36.0
dj-database-url==0.5.0
dj3-cloudinary-storage==0.0.6
Django==4.2.17
django-crispy-forms==1.14.0
gunicorn==20.1.0
pillow==11.0.0
psycopg2-binary==2.9.10
sqlparse==0.5.3
urllib3==1.26.20
whitenoise==6.5.0

To update your requirements.txt file, you can use the following command in your IDE's terminal:
pip freeze > requirements.txt
This command is useful to remember, especially when you install new libraries that need to be reflected in your requirements.

If you want to install all the required packages listed in requirements.txt, you can run this command in your IDE's terminal:
pip3 install -r requirements.txt

Note: Be sure to consult the Python documentation for the appropriate terminal command, as it may vary based on your operating system.

## Deployment

This project was deployed using [Heroku](https://www.heroku.com "Heroku") by following the steps detailed below.

1. Navigate to Heroku website and sign up or log in.
2. Navigate to your dashboard, select **New** and then **Create New App**.
3. Assign a unique name to your project, select your region and click **Create app**.
4. Navigate to **Settings** tab.
5. You need to add specific config vars to be able to deploy the project properly on Heroku. This is done by clicking on **Reveal Config Vars**, and adding them here. The config vars needed are listed below: <br>
CLOUDINARY_URL = Same as your CLOUDINARY_URL in your env.py.<br>
DATABASE_URL =  Same as your DATABASE_URL in your env.py.<br>
SECRET_KEY = Same as your SECRET_KEY in your env.py.<br>
Make sure that the secret key matches the one you are using in your local development environment to avoid any discrepancies when deploying your project.
EMAIL_HOST_USER = Your email address used for sending emails.<br>
EMAIL_HOST_PASS = EMAIL_HOST_PASS = A Gmail API key, as my address and configuration use Gmail settings.<br>


## Deploying from a Github Repository

1. Go to the Deploy tab in your Heroku dashboard.
2. Under the deployment method options, select GitHub - Connect. You will need to log in to your GitHub account through the prompt to authorize the connection.
3. If your GitHub account is not already selected, choose it from the dropdown menu.
4. Use the search function to find the GitHub repository you want to deploy and click Connect next to the corresponding repository in the results list.
5. In the Deploy tab, you will find deployment options further down for both Automatic Deploys and Manual Deploy. Enabling Automatic Deploys will allow Heroku to automatically update your app each time your GitHub repository receives changes.
6. Select your preferred deployment method and specify the branch you wish to deploy.
7. Click Enable Automatic Deploys if you opted for Automatic Deploys. If you chose Manual Deploy, then click Deploy Branch.
8. Heroku will initiate the deployment process. Once the deployment completes successfully, you will see a message stating Your app was successfully deployed, along with a button to view your newly deployed application.

## Migration from Gitpod Enterprise to VS Code

During the course of this project, there was a requirement to switch from Gitpod Enterprise to VS Code due to the impending shutdown of Gitpod services. I carefully followed the provided instructions to migrate my project to VS Code.

Upon completing the migration, I thoroughly tested my code multiple times to ensure that everything was functioning as expected. Fortunately, all aspects of the project worked smoothly.

However, as is the case with any software deployment, issues may arise post-launch. I encourage users to report any problems they encounter promptly. This feedback is invaluable in helping us address and resolve any issues as quickly as possible.

## Personal Reflection

I had a lot of fun working on this project! Initially, I didn’t have a forum project in mind, but after exploring forocoches.com, a Spanish forum where you can find discussions on virtually any topic, I got inspired. What started as a simple idea for a discussion room has evolved, and I still see it as a straightforward concept with immense potential for improvement.

As I coded, I found myself constantly wanting to add new features—thinking, “Now I need to include this, and then that to complement it.” There were times when I felt overwhelmed, nearly giving up when things didn’t go as planned. I experienced frustration when I would start on something and then switch to another section, leaving some tasks half-finished.

However, I realized that this wasn’t a productive approach. I learned the importance of focusing and committing to finishing what I started. Overall, I am proud of what I accomplished, especially as someone who has never formally studied coding. Building projects like this one has been a rewarding experience, and I just wanted to share my thoughts on this fourth project.

## Not About Readme File

During the development of this project, I made a concerted effort to keep track of all the elements and features I added. However, as the project progressed and I approached completion, I encountered several bugs, which I have detailed in the Bugs section of this document.

Throughout this process, the README file underwent multiple revisions to reflect the latest changes made to the project. While I strived to document everything thoroughly, it's important to acknowledge that in large projects like this, it's possible that some details may have been overlooked or omitted unintentionally. Please understand that any such omissions were not intentional, and I appreciate your consideration as you navigate the documentation.

Thank you for your understanding!



## Image Used For Advertisment Window

The image used for the advertisement window comes from the following page name: Fite Fuaite.

*Used Advertisment Image<br>
![Used Advertisment Image](static/images/screenshots/fitefuaiteimage.png)

## Favicon Image 

The favicon image was created using Favicon.io by Joh Sorrentino. You can visit the favicon page at the following link: https://favicon.io/

*Favicon Image*<br>
![Favicon Image](static/images/screenshots/favicon.png)

## Main Idea

At the beginning of my project, I wasn’t entirely sure what direction to take. However, after discussions with my mentor, I started to explore the idea of creating a forum as my project. I quickly recalled one of my favorite forums from my time in Spain called https://forocoches.com/foro/. Although it's a closed forum where registration is limited to invitations, it became a vibrant community that featured discussions and posts on a wide range of topics. 

Inspired by FOROCOCHES, I envisioned building a similar platform where users could engage in meaningful conversations and share insights about various subjects. While my project is currently small, I am committed to enhancing its features over time based on user feedback and suggestions. This iterative approach will help me create a forum that is not only functional but also reflective of the community's interests and needs.

I look forward to developing this project further and turning it into a welcoming space for discussions and knowledge sharing.

## Registered Users 

Users registered to test the project will notice several posts on the main page from different users. Yuss7six is the primary user, while Mett26 has been registered as an external user to assess the functionality of the project. Additionally, Fate is my wife, who registered herself to participate in the testing.

You will also find comments and replies from these users on the posts, showcasing how the commenting system operates. Features such as likes and dislikes have been thoroughly tested as part of this experience.

## Credits

- I extend my heartfelt thanks to [CodeInstitute](https://codeinstitute.net/ "Code Institute") and its vibrant Slack community of tutors and mentors. Your unwavering support, expert advice, and constant encouragement have been instrumental in my educational journey and in successfully completing this project. The dedication shown has significantly enriched my learning experience.

- I also wish to express my gratitude to my wonderful wife, Fatty, and my little brother, Mett, for their crucial testing and feedback.

- A special thank you to my mentor, [Iuliia Konovalova](https://github.com/IuliiaKonovalova), for your invaluable guidance and support throughout this project. Your mentorship has made a tremendous impact!

- I would like to sincerely acknowledge the creators of [GitHub](https://github.com/). Their platform has revolutionized collaboration and learning in coding, serving as more than just a tool—it has been a crucial factor in my development as a coder.