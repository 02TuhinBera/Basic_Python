# Take the user input post
post = input("Enter the post: ")

# Check if the word "harry" exists in the post
if post.find("harry") != -1:
    print("The post is talking about Harry.")
else:
    print("The post is not talking about Harry.")
