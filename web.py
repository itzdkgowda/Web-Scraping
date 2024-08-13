import instaloader

def scrape_instagram_profile(username):
    # Initialize an Instaloader instance
    loader = instaloader.Instaloader()
    
    try:
        # Retrieve profile information
        profile = instaloader.Profile.from_username(loader.context, username)
        
        # Print profile information
        print(f"Username: {profile.username}")
        print(f"Full Name: {profile.full_name}")
        print(f"Bio: {profile.biography}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Posts Count: {profile.mediacount}")
        
        # Print recent posts (optional)
        print("\nRecent Posts:")
        for post in profile.get_posts():
            print(f"Post URL: https://www.instagram.com/p/{post.shortcode}/")
            print(f"Likes: {post.likes}")
            print(f"Caption: {post.caption}")
            print("-------------")
            
    except Exception as e:
        print(f"Error: {e}")

# Example usage
username = input("Enter Instagram username to scrape: ")
scrape_instagram_profile(username)