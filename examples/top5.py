#!/usr/bin/env python3
import lobsters

c = lobsters.Client()
for i, story in zip(range(5), c.frontpage()):
    print(f"{i + 1} - {story.title}")
    print(f"    {story.upvotes} upvotes / "
          f"{story.downvotes} downvotes / "
          f"{story.comment_count} comments")
