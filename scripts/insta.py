
import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'sandesh.n1')

print(type(profile))

print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)

posts = profile.get_posts()
print(posts)
print(posts.count)

# Iterate and download
for index, post in enumerate(posts, 1):
    print("Download ", index)
    bot.download_post(post, target=f"{profile.username}_{index}")