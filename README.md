# polyHack-demiurges

TECHNICAL IMPLEMENTATION:

1. Front-end

- Analytics and Reporting (Dashboard):

We have developed a comprehensive dashboard that provides users with valuable statistics and insights regarding the performance of their posts and comment sections. This includes metrics such as the number of likes, sentiment analysis (positive/negative), paraphrased comments, engagement rates, post impressions, search appearances, and total followings and followers. Our system collects and aggregates data from the integrated social media platforms, allowing users to generate insightful reports for in-depth analysis of their content's performance. With this information at their fingertips, users can make data-driven decisions to optimize their content strategy and enhance their online presence.

- Social Media Integration (Accounts):

Through the utilization of APIs provided by various social media platforms, including Instagram, TikTok, and Twitter, we have successfully integrated these platforms into SocialSync. This integration enables users to establish connections between their accounts on these platforms and our system. By establishing these connections, SocialSync gains the capability to interact with the social media platforms on behalf of the users, facilitating seamless management of their accounts and empowering them to efficiently utilize our platform for content moderation and publication purposes.

- Content Publishing (Posts):

We have developed a user-friendly interface that enables users to effortlessly create and upload posts. Within this interface, users can upload their desired files, enter captions, select the social media platform for publishing, add mentions and hashtags, and even schedule the date and time for posting. To ensure seamless simultaneous publishing, our system implements a robust logic that leverages the APIs provided by each platform. Through these APIs, our system is able to upload the videos and associated metadata, guaranteeing a streamlined and efficient posting process across multiple social media platforms.

2. Back-end & AI model

- Message and Comment Management:

Our platform seamlessly integrates with popular social media platforms, such as Instagram and Twitter, through API integration. This enables us to fetch and manage direct messages (DMs) and post comments directly from our user-friendly dashboard and interface. Users can efficiently monitor and respond to comments across multiple platforms, all within the convenience of our system. By providing this functionality, SocialSync empowers users to effortlessly manage their online interactions and enhance their engagement with their audience.

- Content Moderation:

Our content moderation and management website leverages cutting-edge technologies to provide a comprehensive solution. By integrating the YouTube API and content scraping, we gather messages and comments from various sources. The data is then processed using AI-powered sentiment analysis, toxicity detection, and the Huggingface transformer paraphrasing chatbot. With pre-trained models trained on 38 million Twitter data samples, our system accurately identifies hate comments and rephrases them constructively, based on user preferences. Utilizing Firebase real-time database integration, we store and manage the filtered content. To continuously enhance our algorithms, we are developing a feedback system to gather user input on moderation effectiveness. We label negative comments as 0, positive as 1, and natural as 2, providing valuable insights to content creators. Our solution enables efficient content management, promotes a positive online environment, and enhances the overall user experience.

ARCHITECTURE DESIGN:

The architecture and system design of the platform follow a scalable and modular approach, separating the frontend from the backend components. The frontend is developed using HTML, CSS, and JavaScript, with Bootstrap for responsive design. For the backend, we have utilized the Django framework, which provides a robust and scalable foundation for server-side logic and API integrations. Additionally, Firebase real-time database is chosen as the database management system to store and manage user data, posts, comments, and analytics. The database schema is designed to efficiently store and retrieve the required information, ensuring optimal performance and data integrity. This architecture allows for flexibility, easy maintenance, and scalability, empowering the platform to handle increasing user demand and future enhancements.

RUNNING THE CODE:

1. Environment Setup:

- Install the necessary software: Make sure Python was installed, as well as a code editor or IDE such as PyCharm or Visual Studio Code.
- Set up a virtual environment: Create a virtual environment for the project to manage dependencies and maintain a clean development environment.
- Install the required dependencies: Use pip, the Python package manager, to install the required libraries and frameworks. This includes Django for the backend, and HTML, CSS, and JavaScript (utilizing Bootstrap for styling) for the frontend.

2. Project Configuration:

- Configure the database: Set up a Firebase real-time database and create the necessary collections or tables to store user data, posts, comments, and analytics.
- Integrate social media API access: Obtain API credentials for each social media platform (e.g., YouTube) and configure the necessary authentication and authorization.
- Manage environment variables: Safely store sensitive information (API keys, database connection details, secret keys) as environment variables, ensuring they are not hardcoded in the code for security purposes.

3. Implementing Functionality:

- Develop the user-friendly frontend: Create models, views, and templates using HTML, CSS, and JavaScript, with Bootstrap for responsive design, to provide a seamless interface for users to interact with the system.
- Implement content creation and uploading: Design and build a form that enables users to create and upload posts, select social media platforms, enter captions, add mentions and hashtags, and schedule posting date and time. Handle simultaneous publishing using the respective platform APIs.
- Build the message and comment management system: Develop the necessary logic to fetch and display direct messages (DMs) and post comments from different social media platforms. Allow users to manage and respond to DMs and comments effectively.
- Integrate AI-based content moderation: Utilize the AI models mentioned earlier to analyze sentiment and toxicity of messages and comments. Implement algorithms to filter out hate comments or rephrase them based on user preferences, while providing constructive criticism.
- Implement analytics and reporting: Collect data from social media platforms, calculate metrics such as likes, engagement rates, and sentiment analysis, and generate comprehensive reports. Create a dashboard that displays post performance, comment insights, and relevant analytics.

INPUT AND EXPRECTED OUTPUT:

1. Input:

- User creates a new post by uploading a video, entering a caption, selecting Instagram as the social media platform, and scheduling the post for tomorrow at 10:00 AM.
- User receives a DM on TikTok containing a positive message.
- User receives a comment on a YouTube video with negative sentiment.
- User accesses the analytics section of the SocialSync dashboard to view the performance of a recent Instagram post.
- User wants to analyze the sentiment and engagement metrics of the comment section on a YouTube video.

2. Expected Output:

- The post is successfully uploaded to Instagram, and the scheduled post will be published on the specified date and time.
- The positive DM is displayed in the user's SocialSync dashboard, allowing them to view and respond to it.
- The negative comment is filtered out or rephrased as constructive criticism based on user preferences, and the modified comment is displayed in the user's dashboard.
- The analytics section displays metrics such as the number of likes, comments, and impressions for the Instagram post. It also provides sentiment analysis of the comments, indicating the percentage of positive, negative, and neutral comments. Additionally, engagement rates, such as likes and comments per follower, are calculated and displayed.
- The analytics section presents sentiment analysis results for the YouTube video's comment section, showcasing the percentage of positive, negative, and neutral comments. This helps the user gauge the overall sentiment and understand the audience's reaction to the video.

LIMITATIONS

1. Scalability: Enhance the system's scalability to handle a growing user base and increased data volumes. Implement horizontal scaling techniques, load balancing, and distributed computing to ensure optimal performance even with high demand.

2. Performance: Optimize the performance of AI-based content moderation and sentiment analysis algorithms. Utilize algorithmic improvements, parallel processing, and caching to minimize processing times. Leverage cloud-based services for scalability and performance benefits.

3. Known Issues: Address any limitations or known issues related to AI-based content moderation and sentiment analysis. Continuously monitor and fine-tune the algorithms based on user feedback to improve accuracy and effectiveness.

FUTURE ENHANCEMENTS

1. Enhanced AI Models: Continuously develop and refine AI models for sentiment analysis and content moderation. Train the models on diverse datasets and incorporate user feedback to enhance performance and adaptability.

2. User Feedback System: Implement a user feedback system to gather input on content moderation effectiveness. Utilize feedback to fine-tune algorithms and improve user satisfaction.

3. Advanced Analytics: Expand the analytics module to provide comprehensive insights and visualizations. Include metrics like reach, engagement rates, follower growth, and audience demographics. Incorporate data visualization techniques and customizable reporting options for actionable insights.

SUPPORTING MATERIALS

1. Frontend Screenshots: In the "frontend-ss" folder, you will find screenshots depicting the user interface of SocialSync. These screenshots include the dashboard, account management, and post creation screens. These visuals provide a clear understanding of the user experience and interface design.

2. Backend Screenshots: The "backend-ss" folder contains screenshots showcasing the integration of YouTube API within SocialSync. These screenshots illustrate how the system interacts with the YouTube API to fetch comments and apply filtering and paraphrasing algorithms. This gives an insight into the backend implementation and API integration.

3. Comparison AI Model: Explore the "comparison-ai-model" folder to access snippets of original YouTube comments and their corresponding filtered and paraphrased versions. These samples demonstrate the effectiveness of the content moderation algorithms in transforming hate comments into constructive criticism. The comparison helps in understanding the difference and improvement achieved through the AI model integration.
