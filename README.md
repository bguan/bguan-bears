# Starlette API Server to Classify Bears

Following Lesson 2 of FastAI Course1 v3... Just playing with dockerized Starlette ASGI server that can classify an image as Black, Grizzly or Teddy bear.

Either:
 * Point browser at https://bguan-bears.onrender.com and upload photo or URL pointing to photo and submit.  Or...
 * Programmatically hit the HTTP API directly.  See example below...

Note:
 * To protect server, image upload or submit by URL must not exceed 5MB 

## Example

https://bguan-bears.onrender.com/classify?url=https://n.nordstrommedia.com/id/sr3/8469a1d0-a660-49df-b4e5-96deb40cdbaf.jpeg
