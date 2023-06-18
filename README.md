# polyHack-demiurges

TECHNICAL IMPLEMENTATION:

1. Front-end:
- Analytics and Reporting (Dashboard): Developed a comprehensive dashboard with post and comment performance metrics.
- Social Media Integration (Accounts): Integrated Instagram, TikTok, and Twitter platforms for account management.
- Content Publishing (Posts): User-friendly interface for creating and uploading posts across multiple platforms.

2. Back-end & AI model:
- Message and Comment Management: Seamless management comments from social media.
- Content Moderation: Utilized AI models, such as the Perspective API for sentiment analysis and toxicity detection, and the Huggingface transformer library for comment paraphrasing.


ARCHITECTURE DESIGN:

- Frontend: HTML, CSS, JavaScript (Bootstrap for responsive design)
- Backend: Django framework
- Database: Firebase real-time database for data storage and management.


RUNNING THE CODE:

1. Environment Setup:

- Install Python and a code editor or IDE.
- Set up a virtual environment for managing dependencies.
- Use pip to install required libraries and frameworks: Django for the backend, HTML, CSS, JavaScript (with Bootstrap) for the frontend.

2. Project Configuration:
- Configure a Firebase real-time database and create necessary collections or tables.
- Obtain API credentials for social media platforms and set up authentication and authorization.
- Safely store sensitive information as environment variables.

3. Implementing Functionality:

- Develop a user-friendly frontend with HTML, CSS, JavaScript (using Bootstrap).
- Create a form for post creation and uploading, including options for social media platforms, captions, mentions, hashtags, and scheduling. Handle simultaneous publishing using platform APIs.
- Build a message and comment management system to fetch and display DMs and comments from different platforms, enabling effective management and response.
- Integrate AI-based content moderation using sentiment analysis, toxicity detection, and comment paraphrasing algorithms.
- Implement analytics and reporting by collecting data, calculating metrics, and generating comprehensive reports with a dashboard.


INPUT AND OUTPUT:

1. Input:
   
- User creates a new post (video, caption, Instagram platform, scheduled for tomorrow at 10:00 AM).
- User receives a positive DM on TikTok.
- User receives a negative comment on a YouTube video.
- User accesses analytics for an Instagram post.
- User wants to analyze sentiment and engagement of a YouTube video's comment section.

3. Output:
   
- Post is uploaded to Instagram and scheduled for publication.
- Positive DM is displayed in the SocialSync dashboard.
- Negative comment is filtered or rephrased based on user preferences.
- Analytics show likes, comments, impressions, and sentiment analysis for the Instagram post.
- YouTube comment section sentiment analysis reveals positive, negative, and neutral percentages.


LIMITATIONS AND FUTURE ENHANCEMENTS:

- Scalability: Enhance scalability to handle growing user base and data volumes.
- Performance: Optimize AI algorithms for faster processing using algorithmic improvements and caching.
- Known Issues: Continuously improve AI-based content moderation and sentiment analysis.
- Future Enhancements: Advanced analytics, enhanced AI models, user feedback system.

SUPPORTING MATERIALS:

- Frontend Screenshots: "frontend-ss" folder showcasing dashboard, account, and post screens.
- Backend Screenshots: "backend-ss" folder displaying YouTube API integration and filtered comments.
- Comparison AI Model: "comparison-ai-model" folder with original and filtered comment snippets.
