Thanks for using my Twitter REST API!

Here are the steps to get it working on your system:

1. Install Postman or use the web version.

2. Open the terminal and type `cd app` 

3. Enter `python app.py` to start the server. Now it's ready to be queried!

4. Copy the URL that it is running on. It will look something like this `http://127.0.0.1:5000` At any time you can stop the server by pressing CTRL+C

5. Open Postman and click on "new" next to "import", then select `HTTP`

6. Paste the servers URL into the main text box (it will have a green "GET" word to its left). 

**NOTE: This API can only support GET requests**

7. Now you have `http://127.0.0.1:5000`, put a `/` on the end and end with one of these 4 options. if you just send this, the server will return these options:

    - `/all_tweets` Returns all tweets in the database with create time, ID, and the tweet's text

    - `/external_links` Returns all external links found in all of the tweets, and groups them by tweet ID

    - `/details` Returns details about a specific tweet.
        - `/<tweetID>` be sure to add the tweet's ID at the end of the query.

    - `/profile` Returns details about a specific profile.
        - `/<userID>` be sure to add the userID (aka screen name) at the end of the query.

8. When you are done, closed the server with CTRL+C

Thanks!
Zane Carlson