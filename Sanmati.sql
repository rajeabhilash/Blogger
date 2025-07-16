SELECT table_schema || '.' || table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
AND table_schema NOT IN ('pg_catalog', 'information_schema');

Select * from blogger_post;

delete from blogger_post where id=1;

for post in posts:
print(f"ID: {post.id}")
print(f"Title: {post.title}")
print(f"Content: {post.body}") 
print(f"Created at: {post.created}")
print(f"Publish at: {post.publish}")
print(f"Slug for: {post.slug}")
print(f"Updated for: {post.updated}")
print(f"Status for: {post.status}")	
print('---------------------------')